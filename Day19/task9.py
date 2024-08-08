from collections import Counter

# Function to read a text file, count the frequency of each word, and return the top N most common words as a list of tuples
def top_n_words(filename, N):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(N)

# print result
filename = 'romeo.txt'  # Make sure to replace this with the path to your text file
N = 3
print("Top N words:", top_n_words(filename, N))
