from spacy.tokens import Token
from iwnlp.iwnlp_wrapper import IWNLPWrapper
from spacy.language import Language


__version__ = "3.0.0"

@Language.factory("iwnlp")
def create_component(nlp: Language, name, lemmatizer_path):
    return spaCyIWNLP(lemmatizer_path=lemmatizer_path)

class spaCyIWNLP(object):
    def __init__(self, lemmatizer_path, use_plain_lemmatization=False, ignore_case=False):
        self.lemmatizer = IWNLPWrapper(lemmatizer_path=lemmatizer_path)
        self.use_plain_lemmatization = use_plain_lemmatization
        self.ignore_case = ignore_case
        Token.set_extension('iwnlp_lemmas', force=True, default=None)

    def __call__(self, doc):
        for token in doc:
            token._.iwnlp_lemmas = self.get_lemmas(token)
        return doc

    def get_lemmas(self, token):
        if self.use_plain_lemmatization:
            return self.lemmatizer.lemmatize_plain(token.text, ignore_case=self.ignore_case)
        else:
            return self.lemmatizer.lemmatize(token.text, pos_universal_google=token.pos_)
