
from collections import defaultdict

def train_ibm_model1(corpus):
    # Initialize the translation and alignment probabilities
    t = defaultdict(float)
    a = defaultdict(lambda: defaultdict(float))
    
    # Count the sources and targets
    src_counts = defaultdict(float)
    tgt_counts = defaultdict(float)
    for src_sent, tgt_sent in corpus:
        src_words = src_sent.split()
        tgt_words = tgt_sent.split()
        for src_word in set(src_words):
            src_counts[src_word] += 1
            for tgt_word in set(tgt_words):
                t[(tgt_word, src_word)] = 1 / src_counts[src_word]
                tgt_counts[tgt_word] += 1
      
    # Train the IBM Model 1
    max_iterations = 5  # or any other value
    for _ in range(max_iterations):
        # Initialize the count and total variables
        count = defaultdict(float)
        total = defaultdict(float)
        
        for src_sent, tgt_sent in corpus:
            src_words = src_sent.split()
            tgt_words = tgt_sent.split()
            for tgt_word in tgt_words:
                # Compute the denominator
                denominator = sum([t[(tgt_word, src_word)] for src_word in src_words])
                for src_word in src_words:
                    # Compute the numerator
                    numerator = t[(tgt_word, src_word)]
                    # Compute the expected count
                    expected_count = numerator / denominator
                    # Update the count and total variables
                    count[(tgt_word, src_word)] += expected_count
                    total[src_word] += expected_count
        
        # Update the translation probabilities
        for (tgt_word, src_word), value in count.items():
            t[(tgt_word, src_word)] = value / total[src_word]
        
        # Compute the alignment probabilities
        for src_sent, tgt_sent in corpus:
            src_words = src_sent.split()
            tgt_words = tgt_sent.split()
            for i, tgt_word in enumerate(tgt_words):
                # Compute the denominator
                denominator = sum([t[(tgt_word, src_word)] for src_word in src_words])
                for j, src_word in enumerate(src_words):
                    # Compute the expected count
                    expected_count = t[(tgt_word, src_word)] / denominator
                    # Update the alignment probability
                    a[i][j] += expected_count / tgt_counts[tgt_word]
    
    return t, a

def align(src_sent, tgt_sent, t, a):
    src_words = src_sent.split()
    tgt_words = tgt_sent.split()
    m = len(src_words)
    n = len(tgt_words)
    alignment = []
    for i, tgt_word in enumerate(tgt_words):
        max_prob = 0
        max_index = -1
        for j, src_word in enumerate(src_words):
            prob = t[(tgt_word, src_word)] * a[i][j]
            if prob > max_prob:
                max_prob = prob
                max_index = j
        if max_index != -1:
            alignment.append((max_index, i))
    return alignment

# Load the parallel corpus into memory
with open("parallel_corpus.txt", "r") as f:
    corpus = [tuple(line.strip().split("\t")) for line in f]

# Train the IBM Model 1 on the parallel corpus
t, a = train_ibm_model1(corpus)

# Align a sample sentence pair using the trained IBM Model 1
src_sent = "the cat sat on the mat"
tgt_sent = "le chat s'est assis sur le tapis"
alignment = align(src_sent, tgt_sent, t, a)
print(alignment)