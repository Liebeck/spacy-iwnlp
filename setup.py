from setuptools import setup, find_packages

setup(
    name='spacy_iwnlp',
    packages=find_packages(),
    version='0.0.2',
    description='Integration of IWNLP-py as spaCy extension',
    author='Matthias Liebeck',
    author_email='liebeck@cs.uni-duesseldorf.de',
    url='https://github.com/Liebeck/spacy-iwnlp',
    download_url='https://github.com/Liebeck/spacy-iwnlp/archive/0.0.2.tar.gz',
    keywords=['IWNLP', 'NLP', 'German', 'lemmatization', 'Wiktionary', 'spaCy'],
    install_requires=['spacy>=2.0.0,<3.0.0',
                      'iwnlp>=0.1.7']
)
