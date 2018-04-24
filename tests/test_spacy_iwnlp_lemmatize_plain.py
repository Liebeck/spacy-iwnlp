import unittest
import spacy
from spacy_iwnlp import spaCyIWNLP


class SpacyIWNLPLemmatizePlain(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.nlp = spacy.load('de')
        iwnlp = spaCyIWNLP(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json', use_plain_lemmatization=True, ignore_case=True)
        self.nlp.add_pipe(iwnlp)

    def test_lemmatize_plain_example1(self):
        doc = self.nlp('Gelbe Farben können manche Menschen glücklich machen.')
        assert doc[0]._.iwnlp_lemmas == ['Gelbes', 'gelb']
        assert doc[1]._.iwnlp_lemmas == ['Farbe']
        assert doc[2]._.iwnlp_lemmas == ['Können', 'können']
        assert doc[3]._.iwnlp_lemmas is None
        assert doc[4]._.iwnlp_lemmas == ['Mensch']
        assert doc[5]._.iwnlp_lemmas == ['glücklich']
        assert doc[6]._.iwnlp_lemmas == ['machen']
        assert doc[7]._.iwnlp_lemmas is None
