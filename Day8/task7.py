#DEfine the function 
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test the function with the strings "123" and "hello"
test_string1 = "123"
test_string2 = "hello"

result1 = is_integer(test_string1)
result2 = is_integer(test_string2)

# Print the results
print("Is " , test_string1," an integer? ",result1)
print("Is ",test_string2," an integer? ",result2)
