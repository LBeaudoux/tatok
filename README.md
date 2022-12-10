# tatok

**tatok** is a multilingual text analyzer. It bundles [wordfreq](https://github.com/rspeer/wordfreq) tokenizers with [Snowball](https://snowballstem.org) stemmers, and allows n-gram segmentation.

It has been designed to easily segment sentences from the massively multilingual Tatoeba Corpus.


## Installation

```sh
pip install git+https://github.com/LBeaudoux/tatok.git
```

## Usage

First, import the `get_text_analyzer` function:

```python
from tatok import get_text_analyzer
```

### Tokenization

By default, tatok uses the multilingual tokenizer provided by wordfreq:

```python
>>> analyze_text = get_text_analyzer("en")
>>> analyze_text("She loves me.")
['she', 'loves', 'me']
>>> analyze_text = get_text_analyzer("cmn")
>>> analyze_text("我們試試看！")
["我們", "試試看"]
```

### Stemming

For languages that allow it, you can process the tokens returned by the tokenizer with Snowball stemmers:

```python
>>> from tatok import get_text_analyzer
>>> analyze_text = get_text_analyzer("eng", stemming=True)
>>> analyze_text("She loves me.")
['she', 'love', 'me']
```

### N-gram segmentation

This option is only available for languages with unbounded words like [CJK](https://en.wikipedia.org/wiki/CJK_characters) languages. All 1-grams, 2-grams and 3-grams are returned.

```python
>>> from tatok import get_text_analyzer
>>> analyze_text = get_text_analyzer("cmn", ngram=True)
>>> analyze_text("我們試試看！")
['我',
 '們',
 '試',
 '試',
 '看',
 '！',
 '我們',
 '們試',
 '試試',
 '試看',
 '看！',
 '我們試',
 '們試試',
 '試試看',
 '試看！']
```

### Exceptions

When the language passed as argument is not recognized, no exception is raised and the basic English tokenizer is returned. 

When the ngram or stemming options are not available for a given language, an exception is raised. Below is an example of how to infer a text analyzer that suits your language.

```python
from tatok import get_text_analyzer
from tatok.exceptions import InvalidLanguageValue


def infer_text_analyzer(language):

    try:
        analyze_text = get_text_analyzer(language, ngram=True)
    except InvalidLanguageValue:
        try:
            analyze_text = get_text_analyzer(language, stemming=True)
        except InvalidLanguageValue:
            analyze_text = get_text_analyzer(language)
    
    return analyze_text

```