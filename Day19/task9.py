from collections import Counter
import re

def top_n_words(filename, N):
    with open(filename, 'r') as file:
        text = file.read()

    # Use regular expressions to find words (alphanumeric + apostrophes)
    words = re.findall(r"\b[\w']+\b", text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Return the top N most common words
    return word_counts.most_common(N)

# Example usage
filename = 'romeo.txt'  # Replace with the path to your text file
N = 3
print("Top N words:", top_n_words(filename, N))
