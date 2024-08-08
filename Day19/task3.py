# Create a tuple with three elements
fruits = ('apple', 'banana', 'cherry')

# Try to change the value of the second element and handle the error
try:
    fruits[1] = 'orange'
except TypeError as e:
    print("Error:", e)
