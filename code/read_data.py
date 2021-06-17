import pyconll
train_data = pyconll.load_from_file(r"C:\Users\EDZ\Desktop\tc_nlp\train0.conll")

for sentence in train_data:
   print(sentence.id)
   # for token in sentence:
   #    if token.upos == 'VERB':
   #       verbs.add(token.lemma)