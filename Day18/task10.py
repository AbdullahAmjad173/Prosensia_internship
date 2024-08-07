def most_common_word(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_counts[word] += 1

    most_common = max(word_counts, key=word_counts.get)
    print("The most common word is '{}' with {} occurrences.".format(most_common, word_counts[most_common]))

# Example usage
filename = 'example.txt'  # Make sure to replace this with the path to your text file.
most_common_word(filename)
