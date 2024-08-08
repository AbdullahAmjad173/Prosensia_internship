# Create a list and a tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Append 4 to the list
my_list.append(4)
print("List after append:", my_list)

# Try to append 4 to the tuple and handle the error
try:
    my_tuple.append(4)
except AttributeError as e:
    print("Error:", e)
