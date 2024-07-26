def concatenate_and_convert(str1, str2):
    # Concatenate the two strings
    concatenated_str = str1 + str2
    
    # Check if the concatenated string contains only digits
    if concatenated_str.isdigit():
        # Convert the string to an integer and return it
        return int(concatenated_str)
    else:
        # Return the concatenated string as is
        return concatenated_str


result1 = concatenate_and_convert("123", "456")
result2 = concatenate_and_convert("abc", "123")
print(result1)  # Output: 123456 (as an integer)
print(result2)  # Output: abc123 (as a string)
