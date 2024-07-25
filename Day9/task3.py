#Function define to find the largest and smallest number
def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]

#for loop
    for number in numbers:
        if number > largest:
            largest = number

    for number in numbers:
        if number < smallest:
            smallest = number

    print("Largest number:", largest)
    print("Smallest number:", smallest)

#While loop 
numbers = []
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input == "done":
        break

    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if numbers:
    largest_smallest(numbers)
else:
    print("No numbers were entered.")
