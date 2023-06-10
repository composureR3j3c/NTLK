import nltk
nltk.download('punkt')  # download the punkt tokenizer
nltk.download('wordnet')  # download the wordnet lemmatizer
nltk.download('comtrans')

from nltk.corpus import comtrans
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

from nltk.corpus.reader.aligned import AlignedCorpusReader

root="./corpus/Amharic_English_E-Bible/"

reader = AlignedCorpusReader(root, '.*', '.txt', encoding='utf-8')
reader = comtrans.sents("amharic.txt")

for sentence in reader.aligned_sents():
    print(sentence.words)
    print(sentence.mots)
    print(sentence.alignment)

# Sent1 = comtrans.sents("corpus/Amharic_English_E-Bible/amharic.txt")
# Sent1E = comtrans.sents("corpus/Amharic_English_E-Bible/english.txt")

# Sent2 = comtrans.sents("corpus/Amharic_English_Ethiopic_Bible/amharic.txt")
# Sent2E = comtrans.sents("corpus/Amharic_English_Ethiopic_Bible/english.txt")

# from nltk.translate import Alignment, AlignedSent

# als.Al

# def translate(sentence, src_lang='am', tgt_lang='en'):
#     """Translate a sentence using NLTK and return the translation."""
#     # tokenization and lemmatization
#     words = word_tokenize(sentence.lower())
#     lemmatizer = WordNetLemmatizer()
#     lemmas = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in words]
#     # translation
#     synsets = [wn.synsets(l, lang=src_lang)[0] for l in lemmas if wn.synsets(l, lang=src_lang)]
#     translations = [slem.name().split('.')[0] for syn in synsets for slem in syn.lemmas(lang=tgt_lang)]
#     # check if translation is successful
#     if len(translations) > 0:
#         return ' '.join(translations)
#     else:
#         return 'Translation failed.'
    


# def get_wordnet_pos(word):
#     """Map a Penn Treebank part of speech tag to a WordNet part of speech tag."""
#     tag = nltk.pos_tag([word])[0][1][0].upper()
#     tag_dict = {"J": wn.ADJ,
#                 "N": wn.NOUN,
#                 "V": wn.VERB,
#                 "R": wn.ADV}
#     return tag_dict.get(tag, wn.NOUN)  # default to noun

# sentence = "Hello, how are you?"
# translation = translate(sentence, src_lang='am', tgt_lang='en')
# print(translation)