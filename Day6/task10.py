# Taking input from the user 
num1 = float(input("Enter the first number (dividend): "))
num2 = float(input("Enter the second number (divisor): "))

# Checking if the second number is zero
if num2 == 0:
    print("Division by zero is not allowed.")
else:
    # Performing the division
    result = num1 / num2
    # Display the result
    print("The result of dividing", num1, "by", num2, "is:", result)
