#Function to find the Product
def for_opreration(num1,num2):
    product = num1*num2 
    return product

# Taking input from user 
num1 = float (input("Enter the first value to find the Product"))
num2 = float (input("Enter the second value to find the Product"))

#Calling the function
product = for_opreration(num1,num2)

#Displaying the results
print ("The Product of ",num1, " and ", num2, " is " ,product )
