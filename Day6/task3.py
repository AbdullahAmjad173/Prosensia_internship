#DEfine function and use that by calling it

def checking_number(number):
    if number > 0:
        print("Number is positive ")
        print (number)
    elif number < 0:
        print("Number is negative ")
        print (number)
    else: 
        print("Number is Zero") 
        print (number)        


#Taking input

number = int(input("Enter the Number"))

# calling Function
checking_number(number)
