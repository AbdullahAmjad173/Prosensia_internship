def fibonacci(n, depth=0, max_depth=10):
    if depth > max_depth:
        return "Depth limit reached"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1, depth+1, max_depth) + fibonacci(n-2, depth+1, max_depth)

#passing values to the function.
print(fibonacci(10))
print(fibonacci(50, max_depth=20))  # Larger depth limit
