# spacy-iwnlp
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/Liebeck/spacy-iwnlp/master/LICENSE.md)
[![Build Status](https://api.travis-ci.org/Liebeck/spacy-iwnlp.svg?branch=master)](https://travis-ci.org/Liebeck/spacy-iwnlp)

This package uses the [spaCy 3.0 extensions](https://spacy.io/usage/processing-pipelines#extensions) to add [IWNLP-py](https://github.com/Liebeck/iwnlp-py) as German lemmatizer directly into your spaCy pipeline.

Please report bugs with spacy-iwnlp as issue in [IWNLP-py](https://github.com/Liebeck/iwnlp-py).


## Usage
``` python
import spacy
from spacy_iwnlp import spaCyIWNLP
nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('iwnlp', config={'lemmatizer_path': 'data/IWNLP.Lemmatizer_20181001.json'})
doc = nlp('Wir mögen Fußballspiele mit ausgedehnten Verlängerungen.')
for token in doc:
    print('POS: {}\tIWNLP:{}'.format(token.pos_, token._.iwnlp_lemmas))
```

## Installation
1. Use pip to install spacy-iwnlp
``` bash
pip install spacy-iwnlp
```
2. Download the latest processed IWNLP dump from http://lager.cs.uni-duesseldorf.de/NLP/IWNLP/IWNLP.Lemmatizer_20181001.zip and unzip it.

## Citation
Please include the following BibTeX if you use IWNLP in your work:
``` bash
@InProceedings{liebeck-conrad:2015:ACL-IJCNLP,
  author    = {Liebeck, Matthias  and  Conrad, Stefan},
  title     = {{IWNLP: Inverse Wiktionary for Natural Language Processing}},
  booktitle = {Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)},
  year      = {2015},
  publisher = {Association for Computational Linguistics},
  pages     = {414--418},
  url       = {http://www.aclweb.org/anthology/P15-2068}
}
```