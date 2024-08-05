# Handle the case when data.txt does not exist and print a user-friendly error message
try:
    with open('data.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("The file data.txt does not exist.")
#i had creates the data.txt file .... 