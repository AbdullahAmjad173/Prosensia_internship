#DEfining the function for product
def opr_numbers (num1, num2):
    Product = num1 * num2 
    return Product

#input from user
num1 = int (input("Enter the first value"))
num2 = int (input("Enter the second value"))

Product = opr_numbers(num1,num2)
#Display the result
print("The product of ",num1," " ,num2, " is ",Product)
