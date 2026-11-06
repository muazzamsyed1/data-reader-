"""
app/shared/utils/url_validator.py
=================================
URL Security Validation — SSRF Protection.

What is SSRF?
  Server-Side Request Forgery — an attack where someone tricks the server
  into reading an internal URL like http://localhost/admin or
  http://192.168.1.1/router-config instead of a real website.

  Since our Web Reader fetches URLs provided by admins, we must validate
  every URL before fetching it.

This module:
  1. Checks the URL scheme is allowed (https/http)
  2. Blocks private/internal IP addresses
  3. Blocks dangerous hostnames (localhost, metadata servers)
  4. Optional: checks against an allowed-domain list
"""

from __future__ import annotations
import ipaddress
import socket
from urllib.parse import urlparse
from app.core.config import settings
from app.core.exceptions import URLValidationError


def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def validate_url(url):
    """
Validate and sanitize a URL before the Web Reader fetches it.

Args:
    url: The URL string to validate.

Returns:
    The validated URL (possibly with scheme added if missing).

Raises:
    URLValidationError: If the URL fails any security check.
"""
    pass  # TODO: bytecode-reconstructed placeholder

def __annotate__(format):
    pass  # TODO: bytecode-reconstructed placeholder

def is_valid_url(url):
    """
Non-raising version of validate_url.
Returns True if valid, False if not.
Useful for quick checks without try/except.
"""
    pass  # TODO: bytecode-reconstructed placeholder
