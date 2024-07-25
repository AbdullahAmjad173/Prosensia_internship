#define function to make the value of total and sum =0
def sum_and_average():
    total = 0
    count = 0

#while loop
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")

        if user_input == 'done':
            break

        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

#if else statement
    if count > 0:
        average = total / count
        print(f"Sum: {total}")
        print(f"Average: {average}")
    else:
        print("No numbers were entered.")

# Call the function to run the program
sum_and_average()
