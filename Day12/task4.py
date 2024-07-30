def list_of_strings_to_ints_with_logging(strings):
    ints = []
    errors = []
    for s in strings:
        try:
            ints.append(int(s))
        except ValueError as e:
            errors.append(f"Error converting '{s}': {e}")
    return ints, errors

#calling the function and checking the strings wheather they are int or character :
ints, errors = list_of_strings_to_ints_with_logging(["123", "abc", "456"])
print("Integers:", ints)  # Output: Integers: [123, 456]
print("Errors:", errors)  # Output: Errors: ["Error converting 'abc': invalid literal for int() with base 10: 'abc'"]
