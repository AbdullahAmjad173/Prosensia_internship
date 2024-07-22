# creating function for Conversion of Temp
def celsius_to_Fahrenheit(celsius):
    return((celsius * 9/5) + 32)


celsius = float(input("Enter the temperature in Celsius "))


#Doing Calculations
Fahrenheit = celsius_to_Fahrenheit(celsius)

#Display the result
print ( Fahrenheit)