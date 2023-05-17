import nltk

nltk.download('wordnet')
nltk.download('vader_lexicon')

text="""welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demowords= ["playing", "happiness","going","doing","yes","no","1","having","had", "haved"]


from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

lemmatizer=WordNetLemmatizer()
stemmer=PorterStemmer()
sia=SIA()

for word in demowords:
    print (word,stemmer.stem(word), lemmatizer.lemmatize(word, "v"),sia.polarity_scores(word))

print(sia.polarity_scores("Python is fun"))
print(sia.polarity_scores("chaos is great"))
print(sia.polarity_scores(text))