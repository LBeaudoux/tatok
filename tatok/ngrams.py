from typing import List, Optional


def get_ngrams(
    any_text: str, sep: str = "", max_len: Optional[int] = None
) -> List[str]:
    """Get all possible n-grams of a text

    Parameters
    ----------
    any_text : str
        any text in any language
    sep : str, optional
        the string that is used to split tokens, by default ""
    max_len : Optional[int], optional
        max length of an n-gram, e.g. 3 means 1-grams, 2-grams and 3-grams,
        by default None

    Returns
    -------
    List[str]
        all n-grams found ordered by ascending size and position in the text
    """

    tokens = list(any_text) if not sep else any_text.split(sep)
    ngrams = []
    m = max_len if max_len else len(tokens)
    for n in range(m):
        i = 0
        while i + n < len(tokens):
            ngrams.append(sep.join(tokens[i : i + n + 1]))
            i += 1

    return ngrams
