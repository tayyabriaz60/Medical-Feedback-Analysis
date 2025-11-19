from datetime import datetime, timedelta
from typing import Optional, Tuple
import os
import secrets

import bcrypt
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.models.user import User
from app.logging_config import get_logger

logger = get_logger(__name__)

JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7


def get_secret_key() -> str:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY environment variable is not set. "
            "Generate one with: python -c \"import secrets; print(secrets.token_urlsafe(64))\""
        )
    if secret_key in {
        "change-this-in-production",
        "secret",
        "dev",
        "test",
        "your-secret-key-here",
    }:
        raise RuntimeError("SECRET_KEY uses a known insecure placeholder. Please set a secure value.")
    if len(secret_key) < 32:
        raise RuntimeError("SECRET_KEY must be at least 32 characters long.")
    return secret_key


def generate_secret_key() -> str:
    key = secrets.token_urlsafe(64)
    logger.info("Generated new secret key")
    return key


def hash_password(password: str) -> str:
    """
    Hash password using bcrypt with secure random salt.
    Bcrypt automatically handles the 72-byte limit internally.
    """
    if not isinstance(password, str):
        password = str(password)
    
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify password against bcrypt hash.
    """
    if not isinstance(password, str):
        password = str(password)
    
    try:
        password_bytes = password.encode('utf-8')
        password_hash_bytes = password_hash.encode('utf-8')
        return bcrypt.checkpw(password_bytes, password_hash_bytes)
    except Exception as e:
        logger.error(f"Password verification failed: {e}")
        return False


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, get_secret_key(), algorithm=JWT_ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, get_secret_key(), algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def get_user_count(db: AsyncSession) -> int:
    result = await db.execute(select(func.count(User.id)))
    return int(result.scalar() or 0)


async def create_user(db: AsyncSession, email: str, password: str, role: str = "staff") -> Tuple[Optional[User], Optional[str]]:
    existing = await get_user_by_email(db, email)
    if existing:
        return None, "User already exists"
    user = User(email=email, password_hash=hash_password(password), role=role)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user, None


async def ensure_admin_user(db: AsyncSession, email: Optional[str], password: Optional[str]) -> None:
    """
    Create an admin user if none exists and env ADMIN_EMAIL/ADMIN_PASSWORD provided.
    """
    if not email or not password:
        logger.info("Admin bootstrap skipped - ADMIN_EMAIL or ADMIN_PASSWORD not set")
        return
    count = await get_user_count(db)
    if count > 0:
        logger.info(f"Admin bootstrap skipped - {count} user(s) already exist")
        return
    logger.info(f"Creating initial admin user: {email}")
    user, error = await create_user(db, email=email, password=password, role="admin")
    if error:
        logger.error(f"Failed to create admin user: {error}")
        raise RuntimeError(f"Admin user creation failed: {error}")
    logger.info(f"Admin user created successfully: {email} (ID: {user.id})")


async def ensure_admin_user_exists(
    db: AsyncSession,
    email: str,
    password: str,
    role: str = "admin"
) -> Tuple[User, str]:
    """
    Simple admin user management:
    - If user doesn't exist: CREATE it
    - If user exists: DO NOTHING (return existing)
    
    IMPORTANT: This does NOT update passwords on startup!
    Passwords should only be changed via dedicated admin endpoint.
    
    Returns:
        Tuple[User, str]: (user_object, status) where status is "created" or "existing"
    """
    if not email or not password:
        logger.error("Admin email or password is empty")
        raise ValueError("Admin email and password are required")
    
    # Check if admin user with this email exists
    existing_user = await get_user_by_email(db, email)
    
    if existing_user:
        # User already exists - don't modify
        logger.info(f"Admin user already exists: {email} (ID: {existing_user.id})")
        return existing_user, "existing"
    
    # User doesn't exist - CREATE it
    logger.info(f"Creating admin user: {email}")
    new_user = User(
        email=email,
        password_hash=hash_password(password),
        role=role
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    logger.info(f"Admin user created: {email} (ID: {new_user.id})")
    return new_user, "created"


# Keep old function for backward compatibility but rename
async def ensure_or_update_admin_user(db, email, password, role="admin"):
    """Deprecated: Use ensure_admin_user_exists() instead."""
    return await ensure_admin_user_exists(db, email, password, role)


