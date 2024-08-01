def clean_string(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned

def char_frequency(s):
    # Create a dictionary to store character frequencies
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def anagram_check(str1, str2):
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    # Check if the cleaned strings are anagrams
    are_anagrams = char_frequency(cleaned_str1) == char_frequency(cleaned_str2)
    
    # Return the result and the frequency analysis
    return are_anagrams, {
        'frequency_str1': char_frequency(cleaned_str1),
        'frequency_str2': char_frequency(cleaned_str2)
    }

# Passing values.
str1 = "Listen!"
str2 = "Silent!!"
result, frequencies = anagram_check(str1, str2)
print(f"Are anagrams: {result}")
print("Frequencies:", frequencies)
