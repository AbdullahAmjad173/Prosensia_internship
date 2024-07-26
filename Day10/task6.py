def substring_between_indices(string, start_index, end_index):
    # it indices if they are out of bounds
    if start_index < 0:
        start_index = 0
    if end_index > len(string):
        end_index = len(string)
    
    # Return the substring 
    return string[start_index:end_index]


string = "Hello, World!"
substring1 = substring_between_indices(string, 7, 12)
substring2 = substring_between_indices(string, -5, 20)

print(substring1)  # Output: World
print(substring2)  # Output: Hello, World!
