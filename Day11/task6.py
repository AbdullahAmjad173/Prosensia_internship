def subtract_two_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1 - num2
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Display the result:
print(subtract_two_numbers())
