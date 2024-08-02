def memoized_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = memoized_fibonacci(n-1, memo) + memoized_fibonacci(n-2, memo)
    return memo[n]

def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# passing values to the function.
print(memoized_fibonacci(10))
print(iterative_fibonacci(10))
