from unittest.mock import patch

import pytest
from iso639 import Lang

from tatok.exceptions import InvalidLanguageValue
from tatok.tatok import get_text_analyzer


class TestGetAnalyzer:
    def test_eng_default(self):

        language = "eng"
        my_text = "She loves me."

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["she", "loves", "me"]

    def test_en_default(self):

        language = "en"
        my_text = "She loves me."

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["she", "loves", "me"]

    def test_English_default(self):

        language = "English"
        my_text = "She loves me."

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["she", "loves", "me"]

    @patch("tatok.tatok.Lang")
    def test_cycl_default(self, m_Lang):

        m_Lang.return_value = Lang("eng")

        language = "cycl"
        my_text = "She loves me."

        analyze_text = get_text_analyzer(language)
        m_Lang.assert_called_with("eng")
        assert analyze_text(my_text) == ["she", "loves", "me"]

    def test_eng_with_stem(self):

        language = "eng"
        my_text = "She loves me."

        analyze_text = get_text_analyzer(language, stemming=True)
        assert analyze_text(my_text) == ["she", "love", "me"]

    def test_eng_with_ngram(self):

        language = "eng"

        with pytest.raises(InvalidLanguageValue):
            get_text_analyzer(language, ngram=True)

    def test_eng_with_ngram_and_stem(self):

        language = "eng"

        with pytest.raises(InvalidLanguageValue):
            get_text_analyzer(language, ngram=True, stemming=True)

    def test_fra_no_stem(self):

        language = "fra"
        my_text = "Tu m'aimes ?"

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["tu", "m", "aimes"]

    def test_fra_with_stem(self):

        language = "fra"
        my_text = "Tu m'aimes ?"

        analyze_text = get_text_analyzer(language, stemming=True)
        assert analyze_text(my_text) == ["tu", "m", "aim"]

    def test_jpn_default(self):

        language = "jpn"
        my_text = "何かしてみましょう。"

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["何", "か", "し", "て", "み", "ましょ", "う"]

    def test_jpn_with_stem(self):

        language = "jpn"

        with pytest.raises(InvalidLanguageValue):
            get_text_analyzer(language, stemming=True)

    def test_jpn_ngram(self):

        language = "jpn"
        my_text = "何かしてみましょう。"

        analyze_text = get_text_analyzer(language, ngram=True)
        assert analyze_text(my_text) == [
            "何",
            "か",
            "し",
            "て",
            "み",
            "ま",
            "し",
            "ょ",
            "う",
            "。",
            "何か",
            "かし",
            "して",
            "てみ",
            "みま",
            "まし",
            "しょ",
            "ょう",
            "う。",
            "何かし",
            "かして",
            "してみ",
            "てみま",
            "みまし",
            "ましょ",
            "しょう",
            "ょう。",
        ]

    def test_jpn_with_ngram_and_stem(self):

        language = "jpn"

        with pytest.raises(InvalidLanguageValue):
            get_text_analyzer(language, stemming=True)

    def test_cmn_default(self):

        language = "cmn"
        my_text = "我們試試看！"

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["我們", "試試看"]

    def test_kor_default(self):

        language = "kor"
        my_text = "뭔가 해보자!"

        analyze_text = get_text_analyzer(language)
        assert analyze_text(my_text) == ["뭔가", "해", "보", "자"]
