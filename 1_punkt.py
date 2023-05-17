import nltk
import matplotlib.pyplot as plot

nltk.download('punkt')
# nltk.download('punkt')

text="""welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

from nltk.tokenize import word_tokenize
print("word_tokenize")
print(word_tokenize(text))


from nltk.tokenize import sent_tokenize
print("sent_tokenize")
print(sent_tokenize(text))


from nltk.probability import FreqDist
print("FreqDist")
fd=FreqDist(word_tokenize(text))
print(FreqDist(word_tokenize(text)))

print(fd.most_common(4))

fd.plot(30,cumulative=False)
plot.show()

