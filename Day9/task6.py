#function define
def guess_number():
    predefined_number = 42  # You can set this to any number you like
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        user_input = input("Guess the number: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess == predefined_number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < predefined_number:
            print("Too low!")
        else:
            print("Too high!")

    if attempts == max_attempts:
        print("Sorry, you've reached the maximum number of attempts. The number was:", predefined_number)

# Call the function 
guess_number()
