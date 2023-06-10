from collections import defaultdict

# Initialize the translation and alignment probabilities
t = defaultdict(float)
a = defaultdict(lambda: defaultdict(float))

# Read the aligned sentences from a file
with open("aligned_corpus.txt", "r") as f:
    corpus = [tuple(line.strip().split("\t")) for line in f]

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
max_iterations = 5
for i in range(max_iterations):
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

# Print the translation and alignment probabilities
print("Translation probabilities:")
for (tgt_word, src_word), value in t.items():
    print("{} -> {}: {}".format(src_word, tgt_word, value))
    
print("Alignment probabilities:")
for i in sorted(a.keys()):
    for j in sorted(a[i].keys()):
        print("p({} | {}): {}".format(i, j, a[i][j]))
