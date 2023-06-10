import nltk
  
nltk.download('comtrans')

from nltk.corpus import comtrans

words = comtrans.words("amh.txt")

for word in words[:20]:
    print(word)
print("...")


from nltk.translate import Alignment, AlignedSent

# als = AlignedSent( ["Reprise", "de", "la", "session" ], \
#     ["Resumption", "of", "the", "session" ] , \
#     Alignment( [ (0 , 0), (1 , 1), (2 , 2), (3 , 3) ] ) )

from nltk.translate import IBMModel1

com_ibm1 = IBMModel1(comtrans.aligned_sents()[:10], 100)

print(round(com_ibm1.translation_table["Abebe"]["አበበ"], 3) )

# print(round(com_ibm1.translation_table["Sitzungsperiode"]["session"] , 3) )

# print(round(com_ibm1.translation_table["ሰው"]["human"] , 3) )