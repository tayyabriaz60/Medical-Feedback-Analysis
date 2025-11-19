"""
Rate limiting middleware to protect against abuse.
"""
from __future__ import annotations

import time
from typing import Callable
from collections import defaultdict

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.logging_config import get_logger

logger = get_logger(__name__)

# Rate limit configuration (requests per minute)
RATE_LIMIT_CONFIG = {
    "/feedback": 30,  # 30 requests per minute
    "/auth/login": 10,  # 10 login attempts per minute
    "/auth/register": 5,  # 5 registration attempts per minute
    "default": 100,  # 100 requests per minute for other endpoints
}


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limit requests per IP address."""

    def __init__(self, app):
        super().__init__(app)
        # Store request counts: {ip: {endpoint: [(timestamp, count)]}}
        self.request_counts = defaultdict(lambda: defaultdict(list))

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        client_ip = request.client.host if request.client else "unknown"
        endpoint = request.url.path

        # Find matching rate limit config
        limit = RATE_LIMIT_CONFIG.get("default", 100)
        for pattern, config_limit in RATE_LIMIT_CONFIG.items():
            if endpoint.startswith(pattern):
                limit = config_limit
                break

        # Clean up old requests (older than 60 seconds)
        current_time = time.time()
        self.request_counts[client_ip][endpoint] = [
            (ts, count) for ts, count in self.request_counts[client_ip][endpoint]
            if current_time - ts < 60
        ]

        # Count requests in the last minute
        request_count = sum(count for _, count in self.request_counts[client_ip][endpoint])

        # Check rate limit
        if request_count >= limit:
            logger.warning(
                f"Rate limit exceeded for {client_ip} on {endpoint} "
                f"({request_count}/{limit} requests/min)"
            )
            return Response(
                status_code=429,
                content={"error": "Too many requests. Please try again later."},
                media_type="application/json",
            )

        # Record this request
        self.request_counts[client_ip][endpoint].append((current_time, 1))

        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(limit)
        response.headers["X-RateLimit-Remaining"] = str(limit - request_count - 1)
        return response

