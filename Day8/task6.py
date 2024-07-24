def compute_pay(hours_worked, hourly_rate):
    # Calculate regular pay for up to 40 hours
    if hours_worked <= 40:
        pay=  hours_worked * hourly_rate
        return pay
    
    else:
        # Calculate overtime pay for hours over 40
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        pay = regular_pay + overtime_pay
    
    return pay


# Taking input from the user
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Calculate the pay
pay = compute_pay(hours, rate)

# Print the result
print("The weekly pay is: ",pay)
