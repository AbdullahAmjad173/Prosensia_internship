# Function to swap the values of two variables using tuple assignment
def swap(a, b):
    a, b = b, a
    return a, b

# printing the result
a = 5
b = 10
a, b = swap(a, b)
print("After swap: a =", a, "b =", b)
