from typing import Callable

import Stemmer as PyStemmer
from iso639 import Lang

from .exceptions import InvalidLanguageValue

STEMMER_ALGOS = {
    "ara": "arabic",
    "cat": "catalan",
    "dan": "danish",
    "deu": "german",
    "ell": "greek",
    "eng": "english",
    "eus": "basque",
    "fin": "finnish",
    "fra": "french",
    "gle": "irish",
    "hin": "hindi",
    "hun": "hungarian",
    "ind": "indonesian",
    "ita": "italian",
    "lit": "lithuanian",
    "nep": "nepali",
    "nld": "dutch",
    "nor": "norwegian",
    "por": "portuguese",
    "ron": "romanian",
    "rus": "russian",
    "spa": "spanish",
    "swe": "swedish",
    "tam": "tamil",
    "tur": "turkish",
}


def get_word_stemmer(lang: Lang) -> Callable[[str], str] | None:
    """Get a Snowball stemmer that returns the stem of a word

    In linguistic morphology, stemming is the process of reducing
    inflected (or sometimes derived) words to their word stem, base
    or root form. The stem need not be identical to the
    morphological root of the word; it is usually sufficient that
    related words map to the same stem, even if this stem is not in
    itself a valid root.

    Requirements: Cython, PyStemmer

    More information at https://snowballstem.org/
    """
    try:
        algo_name = STEMMER_ALGOS[lang.pt3]
    except AttributeError:
        return
    except KeyError:
        raise InvalidLanguageValue(lang, task="stemming")
    else:
        stemmer = PyStemmer.Stemmer(algo_name)

        return lambda tk: stemmer.stemWord(tk)
