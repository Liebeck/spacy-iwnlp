import spacy
from spacy_iwnlp import spaCyIWNLP

nlp = spacy.load('de')
iwnlp = spaCyIWNLP(lemmatizer_path='data/IWNLP.Lemmatizer_20170501.json')
nlp.add_pipe(iwnlp)
doc = nlp('Wir liebten den Fußball in die Schwimmbädern Apfelsäure des Admirals Queues Buggys ständest stündest antatest. Ich wusste nicht, dass ihr die Autos abwuscht.')
# print(doc[1])
# print(doc[2])
# print(doc)
for token in doc:
    print('POS: {}\tIWNLP:{}\tspaCy:{}'.format(token.pos_, token._.iwnlp_lemmas, token.lemma_))
# doc._.iwnlp_lemmas