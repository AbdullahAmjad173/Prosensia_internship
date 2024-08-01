
def binary_conversion(binary_str, fixed_length):
    # Convert binary string to integer
    integer = int(binary_str, 2)
    
    binary_str_back = bin(integer)[2:]  # [2:] to remove the '0b' prefix

    binary_str_back = binary_str_back.zfill(fixed_length)
    
    return binary_str_back

#passing values to function
binary_str = "101"
fixed_length = 8
result = binary_conversion(binary_str, fixed_length)
print(result)
