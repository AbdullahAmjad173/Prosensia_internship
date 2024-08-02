def evaluate_polynomial(coeffs, x):
    if not coeffs:
        return "Invalid input: Coefficients list cannot be empty"
    
    degree = len(coeffs) - 1
    result = 0
    for i, coef in enumerate(coeffs):
        result += coef * (x ** (degree - i))
    
    return result

# Passing values to the function

print(evaluate_polynomial([1, 0, -4], 2))  # 1x^2 + 0x - 4 at x = 2
print(evaluate_polynomial([2, -3, 5], 1))  # 2x^2 - 3x + 5 at x = 1
