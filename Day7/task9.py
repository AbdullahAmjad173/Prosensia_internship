num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are positive:", num1, num2)
    
elif num1 > 0 and num2 < 0:
    print(num1, "is positive and", num2, "is negative")
     
elif num1 < 0 and num2 > 0:
    print(num1, "is negative and", num2, "is positive")
     
elif num1 == 0 and num2 == 0:
    print("Both the numbers are zero ",num1,num2)

else:
    print("Both numbers are negative:", num1, num2)
