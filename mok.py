
import nltk 
from nltk.translate import AlignedSent, Alignment, IBMModel1 
 
# Load parallel corpus 
 
amharic_cor = open("corpus/am.txt", "r", encoding='utf-8') 
amharic_list=[] 
amha_sentence=[] 
for sentence in amharic_cor: 
  amha_sentence=sentence.split() 
  amharic_list.append(amha_sentence) 
# print(amharic_list) 
 
# English corpus 
english_cor = open("corpus/en.txt", "r", encoding='utf-8') 
english_list=[] 
eng_sentence=[] 
for sentence in english_cor: 
  eng_sentence=sentence.split() 
  english_list.append(eng_sentence) 
 
english_sentences=english_list 
amharic_sentences=amharic_list 
bitext = [AlignedSent(src, trg) for src, trg in zip(amharic_sentences,english_sentences)] 
 
# Train IBM Model 1 on bitext data 
ibm1 = IBMModel1(bitext, 5) 
# Translate from English to French 
amharic_text = [] 
# french_text = " ".join([max(ibm1.translation_table[english_word].items(), key=lambda x: x[1])[0] for english_word in english_text]) 
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
        french_word = max_translation[0] 
        englishh_text=englishh_text+" "+(french_word) 
        print(french_word) 
    else: 
        print(f"No translations available for {english_word}") 
print('English Senterce: ',englishh_text)