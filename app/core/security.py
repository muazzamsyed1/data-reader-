"""
app/core/security.py
====================
Authentication and Authorization.

Current implementation:
  Simple API key check via X-API-Key header.
  This is enough for a private admin system.

Future: Replace with JWT bearer tokens for full user accounts.

Usage in a route (requires admin API key):
  from app.core.security import require_admin
  from fastapi import Depends

  @router.post("/")
  async def create_something(_: None = Depends(require_admin)):
      ...
"""

from __future__ import annotations
from fastapi import Depends
from fastapi.security import APIKeyHeader
from app.core.config import settings


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def require_admin(api_key):
    """
FastAPI dependency that blocks access if the API key is missing or wrong.

Set your key in .env:  ADMIN_API_KEY=your-secret-key
Send it in requests:   Header: X-API-Key: your-secret-key

Returns None on success (FastAPI convention for auth dependencies).
Raises HTTP 403 on failure.
"""
    pass  # TODO: bytecode-reconstructed placeholder
