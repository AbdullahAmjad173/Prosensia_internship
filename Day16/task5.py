# Count the number of lines in data.txt ....
with open('data.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print(f"Number of lines in data.txt: {line_count}")
