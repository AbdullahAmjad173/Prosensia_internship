def read_lines():
    while True:
        user_input = input("Enter a line of text (or type 'done' to finish): ")

        if user_input == 'done':
            break

        if user_input.startswith(' '):
            continue

        print(user_input)

# Call the function to run the program
read_lines()
