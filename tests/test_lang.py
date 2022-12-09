from iso639 import Lang
from iso639.exceptions import DeprecatedLanguageValue
from tatoebatools import tatoeba

from tatok.lang import get_iso639_lang


class TestGetISO639Lang:
    def test_ok(self):
        assert get_iso639_lang("fra") == Lang("fra")

    def test_not_iso639(self):
        assert get_iso639_lang("cycl") is None

    def test_none(self):
        assert get_iso639_lang(None) is None

    def test_depracated(self):
        assert get_iso639_lang("ppr") == Lang("lcq")

    def test_individual_default(self):
        assert get_iso639_lang("cmn") == Lang("cmn")

    def test_lang(self):
        assert get_iso639_lang(Lang("eng")) == get_iso639_lang("eng")

    def test_all(self):
        for lg in tatoeba.all_languages:
            lang = get_iso639_lang(lg)
            try:
                assert lang is None or lang == Lang(lg)
            except DeprecatedLanguageValue as e:
                assert (e.change_to and lang == Lang(e.change_to)) or (
                    not e.change_to and lang is None
                )
