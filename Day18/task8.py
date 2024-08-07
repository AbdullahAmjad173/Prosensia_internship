def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)
