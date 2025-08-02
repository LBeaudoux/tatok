import pytest
from iso639 import Lang

from tatok.exceptions import InvalidLanguageValue
from tatok.stems import get_word_stemmer


class TestStemmer:
    def test_eng_stemmer(self):

        stem_word = get_word_stemmer(Lang("eng"))
        assert stem_word and stem_word("loves") == "love"

    def test_fr_stemmer(self):

        stem_word = get_word_stemmer(Lang("fr"))
        assert stem_word and stem_word("aimes") == "aim"

    def test_kab_stemmer(self):

        with pytest.raises(InvalidLanguageValue):
            get_word_stemmer(Lang("kab"))
