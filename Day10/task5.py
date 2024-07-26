def count_character_occurrences(string, char):
    # Initialize a counter to 0
    count = 0
    
    # Iterate through each character in the string
    for c in string:
        # If the character matches the specified character, increment the counter
        if c == char:
            count += 1
    
    return count


string = "Hello, World!"
char = "o"
count = count_character_occurrences(string, char)
print("The character ",char," occurs ",count,"times in the string.")
