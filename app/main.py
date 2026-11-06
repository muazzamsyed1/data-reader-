"""
app/main.py
===========
FastAPI entry point — University Requirement Reader.

Serves the country / university / programme / requirement / link data and
the admin dashboard (frontend/index.html). The database itself is built by
`database/rebuild.py` (schema.sql + seed.sql) or re-synced from Excel via
`python -m app.modules.countries.excel_import`.
"""

from __future__ import annotations
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.init_db import init_db
from app.modules.countries import scheduler
from app.modules.countries.router import router


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def lifespan(app):
    """Starting %s v%s (db_engine=%s)"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def create_application():
    """University Requirement Reader — countries, universities, programmes, eligibility requirements and source links for the study-abroad processing team."""
    pass  # TODO: bytecode-reconstructed placeholder
