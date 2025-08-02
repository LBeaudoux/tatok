from typing import Callable, List

import langcodes
import regex
from iso639 import Lang
from wordfreq.chinese import jieba_tokenize
from wordfreq.language_info import get_language_info
from wordfreq.mecab import mecab_tokenize
from wordfreq.preprocess import preprocess_text
from wordfreq.tokens import simple_tokenize

from .segments import segment

# Just identify punctuation
PUNCT_RE = regex.compile(r"[\p{punct}]+")


def get_tokenizer(lang: Lang) -> Callable[[str], List[str]]:
    """
    Get a tokenizer that's appropriate for this language

    The text will be run through a number of pre-processing steps that vary
    by language; see the docstring of `wordfreq.preprocess.preprocess_text`.

    For languages in scripts written without spaces, word boundaries can't
    usually be identified by a regular expression. Instead, there needs to be
    some language-specific handling:
    - in Chinese, we use the Jieba tokenizer with a custom word list
    - in Japanese and Korean, we use the MeCab tokenizer
    - in other languages that use spaceless scripts (e.g. Thai), we use a
      tokenizer that follows ICU rules and not the 'simple' tokenizer from
      wordfreq.
    """
    langcode = _pick_langcode(lang)
    language = langcodes.get(langcode)
    info = get_language_info(language)

    if info["tokenizer"] == "mecab" and isinstance(language.language, str):
        language_language = language.language

        def tokenize(text):
            text = _preprocess_text(text, language)
            tokens = mecab_tokenize(text, language_language)
            return [token for token in tokens if not PUNCT_RE.match(token)]

    elif info["tokenizer"] == "jieba":

        def tokenize(text):
            text = _preprocess_text(text, language)
            tokens = jieba_tokenize(text, external_wordlist=False)
            return [token for token in tokens if not PUNCT_RE.match(token)]

    elif info["tokenizer"] == "regex":

        def tokenize(text):
            text = _preprocess_text(text, language)
            tokens = simple_tokenize(text, include_punctuation=False)
            return tokens

    else:

        def tokenize(text):
            text = _preprocess_text(text, language)
            segments = segment(text, langcode)
            return [
                segment
                for segment in segments
                if not segment.isspace()
                and segment != "\u200b"  # not Zero Width Space
                and not PUNCT_RE.match(segment)
            ]

    return tokenize


def _pick_langcode(lang: Lang) -> str:

    return next(
        (
            getattr(lang, a)
            for a in ("pt1", "pt3", "pt2b", "pt2t", "pt5")
            if getattr(lang, a)
        )
    )


def _preprocess_text(text: str, language: langcodes.Language):

    # replace no-break and narrow no-break spaces because not taken
    # into account by the wordfreq tokenizer
    # Especially required for French.
    text = text.replace("\u00a0", " ").replace("\u202f", " ")
    # replace right single quotation marks by apostrophes because
    # the wordfreq tokenizer does not consider right single quotation
    # marks as word bounderies
    text = text.replace("\u2019", "\u0027")

    return preprocess_text(text, language)
