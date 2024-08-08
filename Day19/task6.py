# Create a dictionary with three key-value pairs
my_dict = {'x': 1, 'y': 2, 'z': 3}

# Function to return a list of tuples representing the dictionary items
def dict_to_tuples(dictionary):
    return list(dictionary.items())

# printing the result
print("Dictionary as list of tuples:", dict_to_tuples(my_dict))
