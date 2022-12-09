import logging

from .tatok import get_text_analyzer

logging.basicConfig(level=logging.INFO, format="%(message)s")

logger = logging.getLogger(__name__)

get_text_analyzer = get_text_analyzer
