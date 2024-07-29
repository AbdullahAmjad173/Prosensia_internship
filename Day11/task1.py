def convert_string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

# usings strings :
print(convert_string_to_int("123"))  # Output: 123
print(convert_string_to_int("abc"))  # Output: None
print(convert_string_to_int("456"))  # Output: 456
print(convert_string_to_int("12.34"))  # Output: None
