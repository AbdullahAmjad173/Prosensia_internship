# Attempt to access a non-existent key and handle KeyError.
my_dict = {'key1': 'value1', 'key2': 'value2'}
key = 'key3'

try:
    value = my_dict[key]
except KeyError:
    print("The key '{}' does not exist in the dictionary.".format(key))
