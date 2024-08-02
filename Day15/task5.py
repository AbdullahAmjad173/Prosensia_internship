def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num*num, limit + 1, num):
                sieve[multiple] = False
    return primes

def prime_generator(limit):
    primes = sieve_of_eratosthenes(limit)
    for prime in primes:
        yield prime

# Epassing values to the function
for prime in prime_generator(30):
    print(prime)
