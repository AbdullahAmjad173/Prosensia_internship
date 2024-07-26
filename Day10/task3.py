def get_string_lengths(string_list):
    # Create a new list to store the lengths of the strings
    lengths = []
    
    # Iterate through each string in the input list
    for string in string_list:
        # Append the length of the current string to the lengths list
        lengths.append(len(string))
    
    return lengths

# passing the string
strings = ["apple", "banana", "cherry"]
lengths = get_string_lengths(strings)
print(lengths)  # Output: [5, 6, 6]
