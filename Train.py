import glob
def align_Corpus(src_path,trg_path):

    # Read in the source and target files
    src_files = glob.glob(src_path)
    trg_files = glob.glob(trg_path)

    # Create a dictionary to store the sentence pairs
    sent_pairs = {}

    # Loop over the files and read in the sentence pairs
    for src_file, trg_file in zip(src_files, trg_files):
        with open(src_file, encoding='utf-8') as fsrc, open(trg_file, encoding='utf-8') as ftrg:
            for src_sent, trg_sent in zip(fsrc, ftrg):
                src_sent = src_sent.strip()
                trg_sent = trg_sent.strip()
                sent_pairs.setdefault(src_sent, []).append(trg_sent)

    # Write out the aligned sentence pairs to a new file
    with open('aligned_corpus.txt', 'a', encoding='utf-8') as fout:
        for src_sent, trg_sents in sent_pairs.items():
            for trg_sent in trg_sents:
                # print(f'{src_sent}\t{trg_sent}\n')
                fout.write(f'{src_sent}\n{trg_sent}\n\n',)

    return 0

alignmet=align_Corpus('corpus/am.txt','corpus/en.txt')
alignmet=align_Corpus('corpus/Amharic_English_E-Bible/amharic.txt','corpus/Amharic_English_E-Bible/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_Ethiopic_Bible/amharic.txt','corpus/Amharic_English_Ethiopic_Bible/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_History/amharic.txt','corpus/Amharic_English_History/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_JW_Bible/amharic.txt','corpus/Amharic_English_JW_Bible/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_JW_Daily_Quote/amharic.txt','corpus/Amharic_English_JW_Daily_Quote/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_Legal/amharic.txt','corpus/Amharic_English_Legal/english.txt')
alignmet=align_Corpus('corpus/Amharic_English_News/amharic.txt','corpus/Amharic_English_News/english.txt')
print("done making Corpus")

import nltk
from nltk.translate import AlignedSent
from nltk.translate import IBMModel1

# Load the corpus text file
with open('aligned_corpus.txt', 'r',encoding='utf-8') as f:
    corpus_text = f.read()

# Preprocess the corpus
preprocessed_corpus = []
for line in corpus_text.split('\n\n'):
    if '\n' in line:
        am_sent, en_sent = line.split('\n')
        am_words = nltk.word_tokenize(am_sent.lower())
        en_words = nltk.word_tokenize(en_sent.lower())
        preprocessed_corpus.append(AlignedSent(am_words, en_words))

# Split the corpus into training and testing sets
train_data = preprocessed_corpus
# test_data = preprocessed_corpus[1000:]

# Train an IBM Model 1 on the training data
ibm1 = IBMModel1(train_data, 5)

# Use the trained model to translate a new sentence
am_sent = [""]
# en_sent = ibm1.translate(am_sent.split())
print(en_sent)

# Evaluate the performance of the translation model on the test data
# scores = ibm1.evaluate(test_data)
# print("IBM Model 1 BLEU score:", scores)
sent=''
while sent!='exit':
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
            eng_word = max_translation[0] 
            englishh_text=englishh_text+" "+(eng_word) 
            print(eng_word) 
        else: 
            print(f"No translations available for {english_word}") 
    print('English Senterce: ',englishh_text)