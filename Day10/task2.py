def print_index(str, ind):
    try:
        return str[ind]
    except IndexError:
        return "Out of range"

# passing values to function
result1 = print_index("Hello World", 8)
result2 = print_index("Hello World", 15)

print(result1)  # Output: r
print(result2)  # Output: Out of range
