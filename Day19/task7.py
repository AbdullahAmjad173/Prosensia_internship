# Function that takes a dictionary and returns a list of tuples sorted by the dictionary's values in descending order
def sort_dict_by_values(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

# printing the result
my_dict = {'a': 10, 'b': 1, 'c': 22}
print("Sorted list of tuples:", sort_dict_by_values(my_dict))
