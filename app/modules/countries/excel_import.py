"""
app/modules/countries/excel_import.py
======================================
Re-runnable Excel -> PostgreSQL sync for the University Requirement Reader.

Use this whenever the source workbooks change. It re-extracts the
university / programme / requirement / link data and reloads the five
tables (countries, universities, programs, program_requirements,
program_links). Student/CRM sheets and columns are never read.

CLI:
    python -m app.modules.countries.excel_import
"""

from __future__ import annotations
import re
import unicodedata
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.countries import excel_extract
from app.modules.countries.models import Country


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _slug(t):
    """NFKD"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _nk(name):
    pass  # TODO: bytecode-reconstructed placeholder

def _cgpa_num(raw):
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def import_all(db, excel_dir):
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _cli():
    pass  # TODO: bytecode-reconstructed placeholder
