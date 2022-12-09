import logging
from typing import Callable, List

from iso639 import Lang

from .config import NGRAM_LANGS, TATOEBA_STEMMER_LANGS
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
        a language code as it appears on Tatoeba
    ngram : bool, optional
        as in the Manticore Search index, split 1-grams, 2-grams
        and 3-grams instead of tokens for languages with no clear
        word bounderies, by default False
    stemming : bool, optional
        as in the Manticore Search index, stem tokens with
        Snowball stemmers when possible, by default False

    Returns
    -------
    Callable[[str], List[str]]
        the segmented text
    """

    lang = get_iso639_lang(language)

    # the English tokenizer is used by default
    if not lang:
        return get_tokenizer(Lang("eng"))
    # as Manticore Search does for CJK languages, return 1-grams,
    # 2-grams and 3-grams when no clear word bounderies
    if ngram:
        if any(getattr(lang, pt) in NGRAM_LANGS for pt in ("pt3", "pt5")):
            return lambda s: get_ngrams(s, sep="", max_len=3)
        else:
            logger.warning(f"{lang.name} not supported by n-gram sgementation")
    # macro languages tend to be better recognized by wordfreq
    # e.g. 'zho' favored over 'cmn'
    if lang.macro():
        tokenize = get_tokenizer(lang.macro())
    else:
        tokenize = get_tokenizer(lang)
    # stem tokens only for Tatoeba languages also stemmed in
    # Manticore index
    if stemming and language in TATOEBA_STEMMER_LANGS:
        stem_lang = Lang(TATOEBA_STEMMER_LANGS[language])
        if stem_word := get_word_stemmer(stem_lang):
            return lambda s: list(map(stem_word, tokenize(s)))

    return tokenize
