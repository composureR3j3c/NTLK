from nltk import sent_tokenize

from googletrans import Translator

translator = Translator()

data = "shut up"

token = sent_tokenize(data)

for tt in token:
    translatedText = translator.translate(tt, dest="en")
    print(translatedText.text)


import pyttsx3

synthesizer = pyttsx3.init()
i=1
while( i<10):
    synthesizer.say(translatedText.text) 
    i=i+1
synthesizer.runAndWait() 
synthesizer.stop()
