def sum_of_squares(N):
    total = 0

    for i in range(1, N + 1):
        total += i ** 2

    return total

# user input
while True:
    user_input = input("Enter a positive integer N: ")

    try:
        N = int(user_input)
        if N <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Calculate and print the sum of squares
result = sum_of_squares(N)
print(f"The sum of the squares of the first {N} natural numbers is: {result}")
