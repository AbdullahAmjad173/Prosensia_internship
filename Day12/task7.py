def exponentiation_table(base, exponent_range):
    return [f"{base}^{i} = {base**i}" for i in range(1, exponent_range + 1)]

# Example usage:
print(exponentiation_table(2, 5))
# Output: ['2^1 = 2', '2^2 = 4', '2^3 = 8', '2^4 = 16', '2^5 = 32']
