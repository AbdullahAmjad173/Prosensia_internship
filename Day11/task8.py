def divide_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2
    except ValueError:
        return "Invalid input. Please enter numeric values."

# EDisplay the result:
print(divide_two_numbers())
