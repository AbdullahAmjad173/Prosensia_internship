
import math

def float_to_int_with_rounding(f, strategy):
    if strategy == "up":
        return math.ceil(f)
    elif strategy == "down":
        return math.floor(f)
    elif strategy == "nearest":
        return round(f)
    else:
        raise ValueError("Invalid rounding strategy")

# calling function and display the result:
print(float_to_int_with_rounding(3.7, "up"))      # Output: 4
print(float_to_int_with_rounding(3.7, "down"))    # Output: 3
print(float_to_int_with_rounding(3.7, "nearest")) # Output: 4
