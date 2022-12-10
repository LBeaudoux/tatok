import logging
from typing import Callable, List

from iso639 import Lang

from .config import BACKUP_LANG, NGRAM_LANGS, TATOEBA_STEMMER_LANGS
from .exceptions import InvalidLanguageValue
from .lang import get_iso639_lang
from .ngrams import get_ngrams
from .stems import get_word_stemmer
from .tokens import get_tokenizer

logger = logging.getLogger(__name__)


def get_text_analyzer(
    language: str, ngram: bool = False, stemming: bool = False
) -> Callable[[str], List[str]]:
    """Get a text segmenter that is suitable for this language

    Parameters
    ----------
    language : str
        an ISO 639 language value or a Tatoeba language code
    ngram : bool, optional
        as in the Manticore Search index, splits 1-grams, 2-grams
        and 3-grams instead of tokens for languages with no clear
        word bounderies, by default False. Not compatible with
        stemming option.
    stemming : bool, optional
        as in the Manticore Search index, stems tokens with Snowball
        stemmers when possible, by default False. Not compatible with
        ngram option.

    Returns
    -------
    Callable[[str], List[str]]
        the segmented text
    """

    lang = get_iso639_lang(language)

    # switch to a backup language when not ISO 639 language
    if not lang:
        backup_lang = Lang(BACKUP_LANG)
        logger.warning(
            f"{backup_lang.name} default tokenizer used for '{language}'"
        )
        return get_tokenizer(backup_lang)
    # as Manticore Search does for CJK languages, return 1-grams, 2-grams
    # and 3-grams when no clear word bounderies
    if ngram:
        if any(getattr(lang, pt) in NGRAM_LANGS for pt in ("pt3", "pt5")):
            analyze_text = lambda s: get_ngrams(s, sep="", max_len=3)
        else:
            raise InvalidLanguageValue(lang, task="n-gram sgementation")
    # macro languages tend to be better recognized by wordfreq
    # e.g. 'zho' favored over 'cmn'
    elif lang.macro():
        analyze_text = get_tokenizer(lang.macro())
    else:
        analyze_text = get_tokenizer(lang)
    # stem tokens only for Tatoeba languages also stemmed in Manticore index
    if stemming:
        stem_lang = Lang(TATOEBA_STEMMER_LANGS.get(language, language))
        if stem_word := get_word_stemmer(stem_lang):
            return lambda s: list(map(stem_word, analyze_text(s)))

    return analyze_text
