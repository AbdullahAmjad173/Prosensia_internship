def is_leap_year(year):
    if (year % 4 == 0): #If it trues then it goes to nest if stament otherwise display the else part
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:   #ELse of divisible by 400
                return False
        else:      #ELse of divisible by 100 
            return True
    else:           #ELse of divisible by 4 
        return False

year = int(input("Enter the year to chaeck wheater it is leap year or not "))

#value pass tp function and then display
if is_leap_year(year):
    print(year)
    print("Is a leap year.")
else:
    print(year)
    print("Is not a leap year.")


    
    