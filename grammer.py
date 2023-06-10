import nltk
from nltk.tokenize import sent_tokenize
from nltk.parse.corenlp import CoreNLPParser
from nltk.tokenize.treebank import TreebankWordTokenizer
from gingerit.gingerit import GingerIt

# Define a sentence with grammatical errors
sentence = "He enjoyes to ski and play tennis."

# Use the CoreNLP parser to get a parse tree
parser = CoreNLPParser()
parsed_sent = next(parser.raw_parse(sentence))
parsed_string = ''.join(str(parsed_sent).split()) # convert Unicode to string and remove whitespace

# Use the TreebankWordTokenizer to tokenize the sentence
tokens = TreebankWordTokenizer().tokenize(sentence)

# Use GingerIt to correct grammar errors
corrected_sent = GingerIt().parse(parsed_string).get('result')

# Join the corrected tokens together to form the final corrected sentence
corrected_tokens = TreebankWordTokenizer().tokenize(corrected_sent)
corrected_sent = ' '.join(corrected_tokens)

# Print the original sentence and the corrected sentence
print("Original sentence: ", sentence)
print("Corrected sentence: ", corrected_sent)
