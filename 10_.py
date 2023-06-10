import nltk
from nltk.translate import ibm1, ibm2

# Train the IBM Model 1 on parallel sentence pairs
bitext = []
with open('alignment-en-fr.txt') as f:
  for line in f:
    en_sent, fr_sent = line.strip().split()
    bitext.append((en_sent.split(), fr_sent.split()))
model1 = ibm1.IBMModel1(bitext, 5)

# Use the IBM Model 1 to translate a new English sentence to French
en_sent = 'This is a test sentence'
fr_sent = model1.translate(en_sent.split())
print(' '.join(fr_sent))

# Train the IBM Model 2 on parallel sentence pairs
bitext = []
with open('alignment-en-fr.txt') as f:
  for line in f:
    en_sent, fr_sent = line.strip().split('\t')
    bitext.append((en_sent.split(), fr_sent.split()))
model2 = ibm2.IBMModel2(bitext, 5)

# Use the IBM Model 2 to translate a new English sentence to French
en_sent = 'This is a test sentence'
fr_sent = model2.translate(en_sent.split())
print(' '.join(fr_sent))
