import glob

# Define the paths to the source and target files
src_path = 'corpus/am.txt'
trg_path = 'corpus/en.txt'

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
with open('aligned_corpus.txt', 'w', encoding='utf-8') as fout:
    for src_sent, trg_sents in sent_pairs.items():
        for trg_sent in trg_sents:
            # print(f'{src_sent}\t{trg_sent}\n')
            fout.write(f'{src_sent}\t{trg_sent}\n',)
