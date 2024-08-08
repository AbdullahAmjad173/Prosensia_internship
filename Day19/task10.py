# Function using list comprehension to take a dictionary and return a sorted list of tuples with values and keys reversed
def reversed_dict_to_sorted_tuples(dictionary):
    return sorted([(value, key) for key, value in dictionary.items()])

# print the result.
my_dict = {'a': 10, 'b': 1, 'c': 22}
print("Sorted list of reversed tuples:", reversed_dict_to_sorted_tuples(my_dict))
