def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    # Calculate the cumulative multiplication
    cumulative_product = 1
    for factor in factors:
        cumulative_product *= factor
    
    return factors, cumulative_product

# passing values.
number = 56
factors, product = prime_factors(number)
print(f"Prime factors: {factors}")
print(f"Cumulative product: {product}")
