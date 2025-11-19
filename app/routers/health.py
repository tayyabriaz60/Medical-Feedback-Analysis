"""
Health and diagnostics endpoints.
"""
from __future__ import annotations

from fastapi import APIRouter
from sqlalchemy import text
import time

from app.db import AsyncSessionLocal, get_pool_stats, check_db_connection
from app.utils.constants import DEPARTMENTS, URGENCY_LEVELS, SENTIMENT_TYPES, FEEDBACK_STATUSES

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health_check():
    """Return service and database health information - responds quickly for Render."""
    # Always return 200 OK immediately (Render's health check just needs quick response)
    # Detailed health check available at /health/ping
    return {
        "service": "medical-feedback-api",
        "status": "healthy",
        "message": "Service is running. Check /health/ping for detailed diagnostics."
    }


@router.get("/ping")
async def ping():
    """Simple ping endpoint with DB latency measurement."""
    latency_ms = None
    try:
        start = time.perf_counter()
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            result.scalar()
        latency_ms = (time.perf_counter() - start) * 1000
    except Exception:
        latency_ms = None
    return {"status": "ok", "db_latency_ms": latency_ms}


@router.get("/config")
async def get_config():
    """Get application configuration constants (departments, status options, etc.)."""
    return {
        "departments": DEPARTMENTS,
        "feedback_statuses": FEEDBACK_STATUSES,
        "urgency_levels": URGENCY_LEVELS,
        "sentiment_types": SENTIMENT_TYPES,
    }


