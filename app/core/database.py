"""
app/core/database.py
====================
Async Database Engine and Session Management.

This module sets up:
  1. The SQLAlchemy async engine (connection pool to MySQL)
  2. An async session factory
  3. A FastAPI dependency `get_db()` that gives each request its own session

What is a "session"?
  Think of it like a shopping cart — you can add/remove items (database
  operations) and only commit (save) everything at once at the end.
  If something goes wrong, you rollback (throw away all changes).

Usage in a FastAPI route:
  @router.get("/example")
  async def example(db: AsyncSession = Depends(get_db)):
      result = await db.execute(select(SomeModel))
      return result.scalars().all()
"""

from __future__ import annotations
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def get_db():
    """
FastAPI dependency that provides a database session per request.

Usage:
    from app.core.database import get_db
    from sqlalchemy.ext.asyncio import AsyncSession
    from fastapi import Depends

    @router.get("/")
    async def my_route(db: AsyncSession = Depends(get_db)):
        ...

The session is automatically closed after the request finishes,
even if an error occurred.
"""
    pass  # TODO: bytecode-reconstructed placeholder
