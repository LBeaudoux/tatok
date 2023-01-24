from unittest.mock import patch

from iso639 import Lang

from tatok.tokens import get_tokenizer


class TestTokenize:
    @patch("tatok.tokens.preprocess_text")
    @patch("tatok.tokens.simple_tokenize")
    def test_regex(self, m_simple_tokenize, m_preprocess_text):
        my_text = "This is a text."

        tokenize = get_tokenizer(Lang("eng"))
        tokenize(my_text)

        m_preprocess_text.assert_called()
        m_simple_tokenize.assert_called()

    @patch("tatok.tokens.preprocess_text")
    @patch("tatok.tokens.mecab_tokenize")
    def test_mecab(self, m_mecab_tokenize, m_preprocess_text):
        my_text = "彼が正しいというのが、私の意見です。"

        tokenize = get_tokenizer(Lang("jpn"))
        tokenize(my_text)

        m_preprocess_text.assert_called()
        m_mecab_tokenize.assert_called()

    @patch("tatok.tokens.preprocess_text")
    @patch("tatok.tokens.jieba_tokenize")
    def test_jieba(self, m_jieba_tokenize, m_preprocess_text):
        my_text = "我忘记问他了。"

        tokenize = get_tokenizer(Lang("cmn"))
        tokenize(my_text)

        m_preprocess_text.assert_called()
        m_jieba_tokenize.assert_called()

    @patch("tatok.tokens.preprocess_text")
    @patch("tatok.tokens.segment")
    def test_icu(self, m_segment, m_preprocess_text):
        my_text = "รองเท้าคู่ไหนเป็นของคุณ"

        tokenize = get_tokenizer(Lang("tha"))
        tokenize(my_text)

        m_preprocess_text.assert_called()
        m_segment.assert_called()
