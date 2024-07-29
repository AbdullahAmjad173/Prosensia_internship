def subtract_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1 - num2
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage:
print(subtract_two_numbers())
