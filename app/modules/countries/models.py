"""
app/modules/countries/models.py
================================
Canonical ORM models for the University Requirement Reader.

Data model:
    Country ──< University ──< Program ──< ProgramRequirement
                                       └──< ProgramLink

This module owns its own declarative Base/MetaData so it is fully
independent of the deprecated `italy` / `policy_reader` layers (which
defined a colliding `universities` table).
"""

from __future__ import annotations
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


def Base():
    """Base"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _uuid():
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def _now():
    pass  # TODO: bytecode-reconstructed placeholder

def Country():
    """Country"""
    pass  # TODO: bytecode-reconstructed placeholder

def University():
    """University"""
    pass  # TODO: bytecode-reconstructed placeholder

def Program():
    """Program"""
    pass  # TODO: bytecode-reconstructed placeholder

def ProgramRequirement():
    """ProgramRequirement"""
    pass  # TODO: bytecode-reconstructed placeholder

def ProgramLink():
    """ProgramLink"""
    pass  # TODO: bytecode-reconstructed placeholder

def ReaderRun():
    """ReaderRun"""
    pass  # TODO: bytecode-reconstructed placeholder

def LinkSnapshot():
    """LinkSnapshot"""
    pass  # TODO: bytecode-reconstructed placeholder

def LinkChange():
    """LinkChange"""
    pass  # TODO: bytecode-reconstructed placeholder

def ReaderSchedule():
    """ReaderSchedule"""
    pass  # TODO: bytecode-reconstructed placeholder
