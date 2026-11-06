"""
app/modules/countries/link_checker.py
======================================
Fetches every stored university/programme link and records whether it is
actually reachable (HTTP status, alive flag, timestamp). This is the engine
behind "is the reader actually fetching data from the links?".
"""

from __future__ import annotations
import asyncio
from datetime import datetime
import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.countries.models import Country


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _check_one(client, url):
    """Return (http_status, is_alive). Tries HEAD, falls back to GET."""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def check_links(db):
    pass  # TODO: bytecode-reconstructed placeholder
