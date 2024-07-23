def gross_salary_calculation(hours, hourly_rate):
    if hours <= 40:
        gross_salary = hours * hourly_rate
    else:
        regular_pay = 40 * hourly_rate
        overtime_pay = (hours - 40) * (hourly_rate * 1.5)
        gross_salary = regular_pay + overtime_pay
    
    return gross_salary

# Taking input from the user
hours = float(input("Enter the hours(In numbers) worked: "))
hourly_rate = float(input("Enter the hourly rate(In numbers): "))

# Calculating the gross salary
gross_salary = gross_salary_calculation(hours, hourly_rate)

# Displaying the result
print("Your Gross Salary is: $", gross_salary)
