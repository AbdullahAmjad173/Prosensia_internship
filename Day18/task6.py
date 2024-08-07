# Using the get method to retrieve values with a default of 0.
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key = 'key4'
value = my_dict.get(key, 0)
print("The value for '{}' is: {}".format(key, value))
