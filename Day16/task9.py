# Read data.txt using a context manager (with statement)
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
