def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Taking number from user
number = int(input("Enter the number to find the factorial: "))

# Verify that the number is not negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print("Factorial of", number, "is", result)
