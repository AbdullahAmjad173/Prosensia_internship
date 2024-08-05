# Read all lines from data.txt and print them to the console
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
#since file have nothing so its output is null