import unittest
import spacy
from spacy_iwnlp import spaCyIWNLP


class SpacyIWNLPLemmatize(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.nlp = spacy.load('de')
        iwnlp = spaCyIWNLP(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json')
        self.nlp.add_pipe(iwnlp)

    def test_lemmatize_example1(self):
        doc = self.nlp('Wir mögen Fußballspiele mit ausgedehnten Verlängerungen.')
        assert doc[0]._.iwnlp_lemmas is None
        assert doc[1]._.iwnlp_lemmas == ['mögen']
        assert doc[2]._.iwnlp_lemmas == ['Fußballspiel']
        assert doc[3]._.iwnlp_lemmas is None
        assert doc[4]._.iwnlp_lemmas == ['ausgedehnt']
        assert doc[5]._.iwnlp_lemmas == ['Verlängerung']
        assert doc[6]._.iwnlp_lemmas is None
