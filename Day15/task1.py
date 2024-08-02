def complex_arithmetic(c1, c2, operation):
    if not (isinstance(c1, tuple) and isinstance(c2, tuple)):
        return "Invalid input: Both inputs must be tuples"
    
    try:
        a, b = c1
        c, d = c2
    except ValueError:
        return "Invalid input: Each tuple must have exactly two elements"
    
    if operation == 'add':
        return (a + c, b + d)
    elif operation == 'subtract':
        return (a - c, b - d)
    elif operation == 'multiply':
        return (a*c - b*d, a*d + b*c)
    elif operation == 'divide':
        if c == 0 and d == 0:
            return "Error: Division by zero"
        denominator = c**2 + d**2
        return ((a*c + b*d) / denominator, (b*c - a*d) / denominator)
    else:
        return "Invalid operation: Choose from 'add', 'subtract', 'multiply', 'divide'"

# passing values to function
print(complex_arithmetic((1, 2), (3, 4), 'add'))
print(complex_arithmetic((1, 2), (3, 0), 'divide'))
