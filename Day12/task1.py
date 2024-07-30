def string_to_int_with_fallback(s, default):
    try:
        return int(s)
    except ValueError:
        return default

# Calling function and sending strings:
print(string_to_int_with_fallback("123", 0))  # Output: 123
print(string_to_int_with_fallback("abc", 0))  # Output: 0
