def reverse_string(input_string):
    reversed_string = ""
    
    # Loop for reverse order
    for char in input_string:
        reversed_string = char + reversed_string
    
    return reversed_string

# user input
user_input = input("Enter a string to reverse: ")

# print the string
reversed_str = reverse_string(user_input)
print("Reversed string:", reversed_str)
