def complex_operations(complex_str1, complex_str2):
    # Convert the string to complex number
    comp1 = complex(complex_str1)
    comp2 = complex(complex_str2)
    
    # Perform operations
    addition = comp1 + comp2
    subtraction = comp1 - comp2
    multiplication = comp1 * comp2
    division = comp1 / comp2
    
    # Return results 
    return (addition, subtraction, multiplication, division)

# passing the values to function
result = complex_operations("2+3j", "1+4j")
print(result)
