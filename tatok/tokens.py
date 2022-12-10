from typing import Callable, List

from iso639 import Lang
from wordfreq import tokenize as wf_tokenize


def get_tokenizer(lang: Lang) -> Callable[[str], List[str]]:

    wf_tokenize = _get_wordfreq_tokenizer(lang)

    def tokenize(any_text):

        # replace no-break and narrow no-break spaces because not taken
        # into account by the wordfreq tokenizer
        # Especially required for French.
        s = any_text.replace("\u00A0", " ").replace("\u202F", " ")
        # replace right single quotation marks by apostrophes because
        # the wordfreq tokenizer does not consider right single quotation
        # marks as word bounderies
        s = s.replace("\u2019", "\u0027")

        return wf_tokenize(s)

    return tokenize


def _get_wordfreq_tokenizer(lang: Lang) -> Callable[[str], List[str]]:

    langcode_tokenizer = next(
        (
            getattr(lang, a)
            for a in ("pt1", "pt3", "pt2b", "pt2t", "pt5")
            if getattr(lang, a)
        )
    )

    return lambda s: wf_tokenize(s, langcode_tokenizer)
