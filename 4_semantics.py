import nltk

from nltk.corpus import wordnet

synonyms = []
for syn in wordnet.synsets ("Computer"):
  for lemma in syn.lemmas():
      synonyms.append(lemma.name())
print (set(synonyms))

antonyms=[]
for syn in wordnet.synsets("small"):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    antonyms.append(ant.name())
print (antonyms)