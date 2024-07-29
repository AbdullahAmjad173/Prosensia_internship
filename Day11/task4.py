#using function to check and display the integer only not the characher
def convert_list_of_strings_to_integers(lst):
    result = []
    for s in lst:
        try:
            result.append(int(s))
        except ValueError:
            continue
    return result

# Esending strings:
print(convert_list_of_strings_to_integers(["123", "abc", "456", "789"]))  # Output: [123, 456, 789]
print(convert_list_of_strings_to_integers(["10", "20", "30"]))  # Output: [10, 20, 30]
print(convert_list_of_strings_to_integers(["1.5", "2.7", "3.9"]))  # Output: []
print(convert_list_of_strings_to_integers(["100", "200a", "300"]))  # Output: [100, 300]
