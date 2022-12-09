NGRAM_LANGS = {
    "bod",
    "cdo",
    "cjy",
    "cmn",
    "cnp",
    "cpx",
    "csp",
    "czh",
    "czo",
    "dzo",
    "gan",
    "hak",
    "hsn",
    "jpn",
    "kar",
    "khb",
    "khm",
    "kor",
    "lao",
    "lbj",
    "lzh",
    "mnp",
    "mya",
    "nan",
    "pli",
    "sip",
    "tai",
    "tha",
    "vie",
    "wuu",
    "yue",
    "zho",
}


# Snowball stemming Algorithms (with the libstemmer library) seem to
# be the only morphological analyzers used by Manticore Search on
# tatoeba.org. See 'tatoeba2/src/Shell/SphinxConfShell.php'

TATOEBA_STEMMER_LANGS = {
    "ara": "ara",  # Arabic
    "eus": "eus",  # Basque
    "cat": "cat",  # Catalan
    "dan": "dan",  # Danish
    "nld": "nld",  # Dutch
    "eng": "eng",  # English
    "fin": "fin",  # Finnish
    "fra": "fra",  # French
    "deu": "deu",  # German
    "ell": "ell",  # Greek
    "hin": "hin",  # Hindi
    "hun": "hun",  # Hungarian
    "ind": "ind",  # Indonesian
    "gle": "gle",  # Irish
    "ita": "ita",  # Italian
    "lit": "lit",  # Lithuanian
    "npi": "nep",  # Nepali
    "nob": "nor",  # Norwegian (Bokmål)
    "por": "por",  # Portuguese
    "ron": "ron",  # Romanian
    "rus": "rus",  # Russian
    "spa": "spa",  # Spanish
    "swe": "swe",  # Swedish
    "tam": "tam",  # Tamil
    "tur": "tur",  # Turkish
}
