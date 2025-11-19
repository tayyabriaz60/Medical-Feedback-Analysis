"""
Rate limiting configuration using slowapi library.
Protects API from abuse and DoS attacks.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request, status
from fastapi.responses import JSONResponse

# Initialize limiter
limiter = Limiter(key_func=get_remote_address)


# Error handler for rate limit exceeded
async def rate_limit_error_handler(request: Request, exc: RateLimitExceeded):
    """Custom error response for rate limit exceeded."""
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "error": {
                "code": "RATE_LIMIT_EXCEEDED",
                "message": f"Rate limit exceeded. {exc.detail}",
            }
        },
    )


# Rate limit configurations
FEEDBACK_SUBMISSION_LIMIT = "10/minute"  # 10 submissions per minute per IP
LOGIN_ATTEMPT_LIMIT = "5/minute"  # 5 login attempts per minute per IP
REGISTRATION_LIMIT = "3/minute"  # 3 registration attempts per minute per IP
GENERAL_LIMIT = "100/minute"  # 100 requests per minute for other endpoints

