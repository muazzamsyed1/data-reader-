"""
app/shared/models/base.py
=========================
SQLAlchemy Declarative Base and Timestamp Mixin.

All database models in the platform inherit from these classes.

What is a "Base"?
  SQLAlchemy needs a common base class to track all your table definitions.
  Every model does:  class MyModel(Base):
  Then Alembic can detect your models and generate migrations.

What is a "Mixin"?
  A mixin is a reusable set of columns you add to multiple models.
  TimestampMixin adds created_at and updated_at to every table automatically.

Usage:
  from app.shared.models.base import Base, TimestampMixin

  class Country(Base, TimestampMixin):
      __tablename__ = "countries"
      id = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
      name = mapped_column(String(100), nullable=False)
"""

from __future__ import annotations
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase


def Base():
    """Base"""
    pass  # TODO: bytecode-reconstructed placeholder

def TimestampMixin():
    """TimestampMixin"""
    pass  # TODO: bytecode-reconstructed placeholder
