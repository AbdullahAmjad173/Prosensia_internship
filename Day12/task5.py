class NotANumberError(Exception):
    pass

def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise NotANumberError("Both inputs must be numbers")
    return a + b


try:
    print(add_numbers(3, 4))  # Output: 7
    print(add_numbers(3, "4"))  # Raises NotANumberError
except NotANumberError as e:
    print(e)  # Output: Both inputs must be numbers
