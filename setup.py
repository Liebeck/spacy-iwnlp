from setuptools import setup, find_packages

setup(
    name='spacy_iwnlp',
    packages=find_packages(),
    version='3.0.0',
    description='Integration of IWNLP-py as spaCy extension',
    author='Dr. Matthias Liebeck',
    author_email='github@liebeck.io',
    url='https://github.com/Liebeck/spacy-iwnlp',
    download_url='https://github.com/Liebeck/spacy-iwnlp/archive/3.0.0.tar.gz',
    keywords=['IWNLP', 'NLP', 'German', 'lemmatization', 'Wiktionary', 'spaCy'],
    install_requires=['spacy>=3.0.0',
                      'iwnlp>=0.1.7']
)
