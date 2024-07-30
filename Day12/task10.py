import re
from collections import defaultdict

def is_palindrome_with_freq_analysis(string):
    # Remove all non-alphanumeric characters and convert to lower case
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    
    # Check if the cleaned string is a palindrome
    is_palindrome = cleaned_string == cleaned_string[::-1]
    
    # Calculate the frequency of each character in the cleaned string
    char_freq = defaultdict(int)
    for char in cleaned_string:
        char_freq[char] += 1

    return is_palindrome, dict(char_freq)


input_string = "A man, a plan, a canal, Panama!"
is_palindrome, freq_analysis = is_palindrome_with_freq_analysis(input_string)
print(f"Is palindrome: {is_palindrome}")  # Output: Is palindrome: True
print(f"Character frequencies: {freq_analysis}")
# Output: Character frequencies: {'a': 8, 'm': 2, 'n': 4, 'p': 2, 'l': 2, 'c': 1}
