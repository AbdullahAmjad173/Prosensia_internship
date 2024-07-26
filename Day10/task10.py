#re module is used to handle sequences of whitespace characters more effectively
import re

def clean_string(input_string):
    # Remove leading and trailing whitespace
    trimmed_string = input_string.strip()
    
    # Replace any sequence of  whitespace with a single space
    cleaned_string = re.sub(r'\s+', ' ', trimmed_string)
    
    return cleaned_string


original_string = "   This   is  a    string with   irregular  spacing.   "
cleaned = clean_string(original_string)
print(cleaned)  #
