def compare_strings(str1, str2):
    if str1 < str2:
        return f'"{str1}" comes before "{str2}"'
    elif str1 > str2:
        return f'"{str1}" comes after "{str2}"'
    else:
        return f'"{str1}" is equal to "{str2}"'


result1 = compare_strings("apple", "banana")
result2 = compare_strings("orange", "grape")
result3 = compare_strings("cherry", "cherry")

print(result1)  # Output: "apple" comes before "banana"
print(result2)  # Output: "orange" comes after "grape"
print(result3)  # Output: "cherry" is equal to "cherry"
