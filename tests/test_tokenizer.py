from unittest.mock import patch

from iso639 import Lang

from tatok.tokens import get_tokenizer


class TestTokenize:
    @patch("tatok.tokens.wf_tokenize")
    def test_eng(self, m_wf_tokenize):
        my_text = "This is a text."

        tokenize = get_tokenizer(Lang("eng"))
        tokenize(my_text)

        m_wf_tokenize.assert_called_with(my_text, "en")
