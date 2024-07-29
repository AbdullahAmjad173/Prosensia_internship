def multiply_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1 * num2
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Display the result:
print(multiply_two_numbers())
