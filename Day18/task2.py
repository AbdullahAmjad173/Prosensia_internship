def print_value(dictionary, key):
    if key in dictionary:
        print("Value:", dictionary[key])
    else:
        print("The key '{}' is not found in the dictionary.".format(key))

# Example usage
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print_value(my_dict, 'key2')
print_value(my_dict, 'key4')
