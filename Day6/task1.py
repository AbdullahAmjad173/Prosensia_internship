# I am creating function for diaplay the output according to my need
def convert_to_number(value):
    if '.' in value:
        return float(value)
    else:
        return int(value)

# Taking input from the user 

a = convert_to_number(input("Enter the hours: "))
b = convert_to_number(input("Enter the hourly wage rate: "))

# Performing the multiplication
c = a * b

# Printing the result
print(c)
