import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

source_sentence = 'I like to play football'
target_sentence = 'J\'aime jouer au football'

source_words = word_tokenize(source_sentence)
target_words = word_tokenize(target_sentence)

for source_word in source_words:
    print(source_word,'\n')

source_vocab = set(source_words)
target_vocab = set(target_words)
   

