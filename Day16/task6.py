# Find and print all lines that contain the word "error" in log.txt  ..............
try:
    with open('log.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if 'error' in line:
            print(line, end='')
except FileNotFoundError:
    print("The file data.txt does not exist.")