"""
app/core/exceptions.py
======================
Custom Exception Classes for the Platform.

Why custom exceptions?
  Instead of raising generic `Exception("something went wrong")`,
  we raise specific exceptions that carry context:
    raise URLValidationError(url="http://localhost", reason="private IP blocked")

FastAPI exception handlers in main.py catch these and return proper
HTTP responses with helpful error messages.
"""

from __future__ import annotations


def PlatformError():
    """PlatformError"""
    pass  # TODO: bytecode-reconstructed placeholder

def URLValidationError():
    """URLValidationError"""
    pass  # TODO: bytecode-reconstructed placeholder

def WebReaderError():
    """WebReaderError"""
    pass  # TODO: bytecode-reconstructed placeholder

def EmptyContentError():
    """EmptyContentError"""
    pass  # TODO: bytecode-reconstructed placeholder

def LLMExtractionError():
    """LLMExtractionError"""
    pass  # TODO: bytecode-reconstructed placeholder

def DatabaseError():
    """DatabaseError"""
    pass  # TODO: bytecode-reconstructed placeholder

def ConfigurationError():
    """ConfigurationError"""
    pass  # TODO: bytecode-reconstructed placeholder
