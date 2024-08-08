# Function to compare two tuples element-wise and return a list of comparison results
def compare_tuples(tup1, tup2):
    return [a == b for a, b in zip(tup1, tup2)]

# printing the result
tup1 = (1, 2, 3)
tup2 = (3, 2, 1)
print("Comparison results:", compare_tuples(tup1, tup2))
