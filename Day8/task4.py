#DEfining the function for sum
def add_numbers (num1, num2):
    sum_total = num1 + num2 
    return sum_total

#input from user
num1 = int (input("Enter the first value"))
num2 = int (input("Enter the second value"))

sum_total = add_numbers(num1,num2)
#Display the result
print("The sum of ",num1," " ,num2, " is ",sum_total)
