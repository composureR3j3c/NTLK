from nltk import sent_tokenize

from googletrans import Translator

translator = Translator()

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."

token = sent_tokenize(data)

for tt in token:
    translatedText = translator.translate(tt, dest="am")
    print(translatedText.text)