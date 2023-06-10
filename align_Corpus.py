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
print("done")