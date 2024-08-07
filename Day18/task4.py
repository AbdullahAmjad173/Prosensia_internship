# Read a line of text from the user
text = input("Enter a line of text: ")

# Split the text into words and count occurrences using a dictionary
word_counts = {}
words = text.split()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Print the dictionary of word counts
print("Word counts:", word_counts)
