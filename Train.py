import nltk
from nltk.translate import AlignedSent
from nltk.translate import IBMModel1

# Load the corpus text file
with open('aligned_corpus.txt', 'r', encoding='utf-8') as f:
    corpus_text = f.read()

# Preprocess the corpus
preprocessed_corpus = []

with open("aligned_corpus.txt", "r", encoding='utf-8') as f:
    corpus = [tuple(line.strip().split("\t")) for line in f]
    
for am_sent, en_sent in corpus:
    am_words = (am_sent).split()
    en_words = (en_sent).split()
    preprocessed_corpus.append(AlignedSent(am_words, en_words))

# Split the corpus into training and testing sets
train_data = preprocessed_corpus
test_data = preprocessed_corpus[1000:]

# Train an IBM Model 1 on the training data
ibm1 = IBMModel1(train_data, 5)

# Use the trained model to translate a new sentence
am_sent = "ገዛ"
en_sent = ibm1.translate(am_sent.split())
print(en_sent)

# Evaluate the performance of the translation model on the test data
scores = ibm1.evaluate(test_data)
print("IBM Model 1 BLEU score:", scores)
