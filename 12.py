import nltk 
from nltk.translate import AlignedSent, Alignment, IBMModel1 
 
# Load parallel corpus 
 
english_sentences = [["abebe", "ate", "beso"], ["abebe", "ate", "enjera"],["he","ate","beso"],["he","bought","enjera"]] 
amharic_sentences = [["አበበ", "በሶ", "በላ"], ["አበበ", "እንጀራ", "በላ"],["እሱ","በሶ","በላ"],["እሱ","እንጀራ","ገዛ"]] 
bitext = [AlignedSent(src, trg) for src, trg in zip(amharic_sentences,english_sentences)] 
 
# Train IBM Model 1 on bitext data 
ibm1 = IBMModel1(bitext, 5) 
# Translate from English to French 
amharic_text = ["አበበ", "በሶ", "ገዛ"] 
# french_text = " ".join([max(ibm1.translation_table[english_word].items(), key=lambda x: x[1])[0] for english_word in english_text]) 
 
french_text="" 
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