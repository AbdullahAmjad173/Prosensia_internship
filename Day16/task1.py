try:
    file = open('data.txt', 'r')
    file.close()
except FileNotFoundError:
    print("The file data.txt does not exist.")
