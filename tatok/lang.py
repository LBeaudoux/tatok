import logging

from iso639 import Lang
from iso639.exceptions import DeprecatedLanguageValue, InvalidLanguageValue

logger = logging.getLogger(__name__)


def get_iso639_lang(language: str) -> Lang | None:
    """Get a Lang instance that handle the ISO 639 codes of the
    passed language

    Parameters
    ----------
    language : str
        only ISO 639 language values are recogized

    Returns
    -------
    iso639.Lang | None
        a Lang instance of the language passed as aurgument when this
        one is recognized. None is returned otherwise.
    """
    try:
        lang = Lang(language)
    except InvalidLanguageValue:
        msg = f"'{language}' is not a valid ISO 639 language value"
        logger.warning(msg)
        return
    except DeprecatedLanguageValue as e:
        if e.change_to:
            lang = Lang(e.change_to)
            msg = f"{e.name} is deprecated and replaced by {lang.name}"
        else:
            lang = None
            msg = f"{e.name} is deprecated and has no replacement value"
        logger.warning(msg)

    return lang
