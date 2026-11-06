"""
app/shared/utils/normalizer.py
==============================
Value Normalization for Policy Information.

Problem:
  Different websites express the same value differently:
    "€11,904"        — German style
    "EUR 11904"      — ISO style
    "11,904 Euros"   — Plain text
    "11904.00 EUR"   — Decimal

  When comparing old vs. new policy values, we need to know these are
  the same value, NOT a policy change.

This module normalizes extracted values so comparisons are meaningful.
"""

from __future__ import annotations
import re
from decimal import Decimal


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def normalize_monetary(raw):
    """
Extract a numeric amount and ISO currency code from a monetary string.

Examples:
  "€11,904"       → (Decimal("11904"), "EUR")
  "EUR 11904"     → (Decimal("11904"), "EUR")
  "$1,234.56"     → (Decimal("1234.56"), "USD")
  "20 Euro"       → (Decimal("20"), "EUR")

Returns:
  Tuple of (amount, currency_code), or (None, None) if not parseable.
"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def normalize_hours(raw):
    """
Extract hours per week/month from a string.

Examples:
  "20 hours/week" → Decimal("20")
  "120 hours/month" → Decimal("120")
  "20h per week" → Decimal("20")
"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def values_are_equivalent(val_a, val_b, data_type):
    """
Compare two policy values semantically, not just as strings.

This prevents false positives where "€11,904" and "EUR 11904" would
be flagged as a change when they mean the same thing.

Args:
    val_a: First value (e.g., previous database value)
    val_b: Second value (e.g., newly extracted value)
    data_type: The type of data (MONETARY, HOURS, NUMBER, TEXT)

Returns:
    True if values represent the same information, False if they differ.
"""
    pass  # TODO: bytecode-reconstructed placeholder
