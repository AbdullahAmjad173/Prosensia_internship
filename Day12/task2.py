def int_to_str_with_formatting(num, format_spec):
    return format(num, format_spec)

# Calling the function and returning the resukt as according to the format:
print(int_to_str_with_formatting(123, "04d"))      # Output: "0123"
print(int_to_str_with_formatting(123, "e"))        # Output: "1.230000e+02"
print(int_to_str_with_formatting(123, "10d"))      # Output: "       123"
