from collections import defaultdict

# Initialize the translation and alignment probabilities
t = defaultdict(float)
a = defaultdict(lambda: defaultdict(float))
# Read the aligned sentences from a file

with open("aligned_corpus.txt", "r", encoding='utf-8') as f:
    corpus = [tuple(line.strip().split("\t")) for line in f]
    
src_counts = defaultdict(float)
tgt_counts = defaultdict(float)

from nltk.translate import AlignedSent, Alignment, IBMModel1 

from nltk.corpus import comtrans
import nltk
  
nltk.download('comtrans')
nltk

words = comtrans.words(corpus)
src_sents=[]
tgt_sents=[]
for src_sent, tgt_sent in corpus:

    src_sents.append(src_sent)
    tgt_sents.append(src_sent)
#     # print("Source sentence: ", src_sent)
#     # print("Aligned target sentence: ", tgt_sent)
# bitext = [AlignedSent(src, trg) for src, trg in zip(src_sents,tgt_sents)] 

# Train IBM Model 1 on bitext data 
ibm1 = IBMModel1(corpus, 5) 
# Translate from English to French 
amharic_text = ["አበበ", "በሶ", "ገዛ"] 

for english_word in amharic_text: 
    # english_word = "This" 
    print(english_word) 
    translations = ibm1.translation_table.get(english_word) 
    print("-----------------------------------------") 
    print('Transalation===',translations) 
    if translations: 
        max_translation = max(translations.items(), key=lambda x: x[1]) 
        french_word = max_translation[0] 
        french_text=french_text+" "+(french_word) 
        print(french_word) 
    else: 
        print(f"No translations available for {english_word}") 
print(french_text)



ibm1 = IBMModel1(bitext, 5) 