#Function to find the Square
def for_opreration(num1):
    Square = num1*num1 
    return Square

# Taking input from user 
num1 = int(input("Enter the value to find the Square"))

#Calling the function
Square = for_opreration(num1)

#Displaying the results
print ("The Square of ",num1, "  is " ,Square )
