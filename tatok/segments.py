from typing import List

from icu import BreakIterator, Locale

_break_iterator = None


def segment(text: str, language_code: str) -> List[str]:
    """Segment a text around the bounderies of its words in accordance with
    the rules specified by Unicode Standard Annex #29, Unicode Text
    Segmentation (https://www.unicode.org/reports/tr29/ )

    Parameters
    ----------
    text : str
        the text to be segmented
    language_code : str
        an ISO 639 language code

    Returns
    -------
    List[str]
        the list of "word segments". All characters (space and punctuation
        included) are preserved
    """
    _break_iterator = _get_break_iterator(language_code)
    _break_iterator.setText(text)

    i = 0
    segments = []
    for j in _break_iterator:
        segments.append(text[i:j])
        i = j

    return segments


def _get_break_iterator(language):

    global _break_iterator

    locale = Locale(language)
    if not _break_iterator or locale != _break_iterator.getLocale():
        _break_iterator = BreakIterator.createWordInstance(locale)

    return _break_iterator
