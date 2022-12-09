from iso639 import Lang

from tatok.stems import get_word_stemmer


class TestStemmer:
    def test_eng_stemmer(self):

        stem_word = get_word_stemmer(Lang("eng"))
        assert stem_word("loves") == "love"

    def test_fr_stemmer(self):

        stem_word = get_word_stemmer(Lang("fr"))
        assert stem_word("aimes") == "aim"

    def test_kab_stemmer(self):

        stem_word = get_word_stemmer(Lang("kab"))
        assert stem_word is None
