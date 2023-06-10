import nltk
from nltk.translate import AlignedSent, Alignment, IBMModel1

# Load parallel corpus
english_sentences = [["This", "is", "a", "book"], ["I", "am", "happy"]]
french_sentences = [["Ceci", "est", "un", "livre"], ["Je", "suis", "heureux"]]
bitext = [AlignedSent(src, trg) for src, trg in zip(english_sentences, french_sentences)]

# Train IBM Model 1 on bitext data
ibm1 = IBMModel1(bitext, 5)

# Translate from English to French
english_text = ["The", "cat", "is", "on", "the", "mat"]
french_text = " ".join([max(ibm1.translation_table[english_word].items(), key=lambda x: x[1])[0] for english_word in english_text])

print(f"Translated text: {english_text} -> {french_text}")