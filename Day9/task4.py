#function to find unique number
def remove_duplicates(numbers):
    unique_numbers = set()
    result = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.add(number)
            result.append(number)

    return result

# list of numbers
numbers = [10, 5, 8, 10, 3, 5, 7, 8, 3]
print("Original list:", numbers)

unique_numbers = remove_duplicates(numbers)
print("List without duplicates:", unique_numbers)
