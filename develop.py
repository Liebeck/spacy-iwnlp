import spacy
from spacy_iwnlp import spaCyIWNLP

nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('iwnlp', config={'lemmatizer_path': 'data/IWNLP.Lemmatizer_20181001.json'})
doc = nlp('Wir mögen Fußballspiele mit ausgedehnten Verlängerungen.')
for token in doc:
    print('POS: {}\tIWNLP:{}'.format(token.pos_, token._.iwnlp_lemmas))