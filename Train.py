import nltk
from nltk.translate import AlignedSent
from nltk.translate import IBMModel1

# Load the corpus text file
with open('aligned_corpus.txt', 'r',encoding='utf-8') as f:
    corpus_text = f.read()

# Preprocess the corpus
preprocessed_corpus = []
for line in corpus_text.split('\n\n'):
    if '\n' in line:
        am_sent, en_sent = line.split('\n')
        am_words = nltk.word_tokenize(am_sent.lower())
        en_words = nltk.word_tokenize(en_sent.lower())
        preprocessed_corpus.append(AlignedSent(am_words, en_words))

# Split the corpus into training and testing sets
train_data = preprocessed_corpus
# test_data = preprocessed_corpus[1000:]

# Train an IBM Model 1 on the training data
ibm1 = IBMModel1(train_data, 5)

# Use the trained model to translate a new sentence
am_sent = [""]
# en_sent = ibm1.translate(am_sent.split())
print(en_sent)

# Evaluate the performance of the translation model on the test data
# scores = ibm1.evaluate(test_data)
# print("IBM Model 1 BLEU score:", scores)
sent=''
while sent!='exit':
    sent = input("Enter Amharic Sentence : ") 
    amharic_text=sent.split() 
    englishh_text="" 
    for english_word in amharic_text: 
        # english_word = "This" 
        print(english_word) 
        translations = ibm1.translation_table.get(english_word) 
        # print("-----------------------------------------") 
        # print('Transalation===',translations) 
        if translations: 
            max_translation = max(translations.items(), key=lambda x: x[1]) 
            eng_word = max_translation[0] 
            englishh_text=englishh_text+" "+(eng_word) 
            print(eng_word) 
        else: 
            print(f"No translations available for {english_word}") 
    print('English Senterce: ',englishh_text)