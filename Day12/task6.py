class InvalidListError(Exception):
    pass

def cumulative_subtraction(numbers):
    if len(numbers) < 2:
        raise InvalidListError("The list must contain at least two elements")
    
    result = numbers[0]
    for num in numbers[1:]:
        if not isinstance(num, (int, float)):
            raise InvalidListError("All elements in the list must be numbers")
        result -= num
    return result


try:
    print(cumulative_subtraction([10, 2, 3]))  # Output: 5
    print(cumulative_subtraction([10]))  # Raises InvalidListError
except InvalidListError as e:
    print(e)  # Output: The list must contain at least two elements

