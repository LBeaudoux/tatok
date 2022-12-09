# tatok

A multilingual text analyzer for the Tatoeba Corpus.

```python
>>> from tatok import get_text_analyzer
>>> analyze_text = get_text_analyzer("eng", stemming=True)
>>> analyze_text("She loves me.")
['she', 'love', 'me']
```