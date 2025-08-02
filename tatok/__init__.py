import logging

from .tatok import get_text_analyzer

logging.basicConfig(level=logging.INFO, format="%(message)s")

__all__ = ["get_text_analyzer"]
