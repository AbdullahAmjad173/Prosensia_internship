def fibonacci_sequence(N):
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    sequence = []
    
    for _ in range(N):
        sequence.append(a)  # Add the current number to the sequence
        a, b = b, a + b    # Update to the next numbers in the sequence
    
    return sequence

# Get user input
user_input = input("Enter the number of Fibonacci numbers to generate: ")

try:
    N = int(user_input)
    if N <= 0:
        print("Please enter a positive integer.")
    else:
        # Generate and print the Fibonacci sequence
        fib_sequence = fibonacci_sequence(N)
        print("Fibonacci sequence:", fib_sequence)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
