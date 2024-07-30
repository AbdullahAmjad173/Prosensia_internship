class DivisionByZeroError(Exception):
    pass

def safe_division(a, b, precision):
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return round(a / b, precision)

# first input then sending values to function and then print:
try:
    print(safe_division(10, 2, 2))  # Output: 5.0
    print(safe_division(10, 0, 2))  # Raises DivisionByZeroError
except DivisionByZeroError as e:
    print(e)  # Output: Cannot divide by zero
