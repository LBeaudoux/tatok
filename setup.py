import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tatok",
    version="0.0.3",
    author="L.Beaudoux",
    description="A multilingual text analyzer for the Tatoeba Corpus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LBeaudoux/tatok",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8.0",
    install_requires=[
        "iso639-lang==2.1.0",
        "ipadic==1.0.0",
        "jieba==0.42.1",
        "mecab-ko-dic==1.0.0",
        "mecab-python3==1.0.6",
        "PyStemmer==2.0.1",
        "wordfreq==3.0.3",
    ],
)
