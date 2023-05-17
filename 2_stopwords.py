import nltk

nltk.download('stopwords')
text="""welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demowords= ["playing", "happiness","going","doing","yes","no","1","having","had", "haved"]
from nltk.corpus import stopwords
stop_words= stopwords.words ("english")
# print (stop_words)
# print("\n\n")
# print (set(stop_words))

from nltk.tokenize import word_tokenize, sent_tokenize
tokenize_words= word_tokenize(text)
#print(tokenize_words )
tokenize_words_without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)
print("stop words that got removed", set(tokenize_words)-set(tokenize_words_without_stop_words))