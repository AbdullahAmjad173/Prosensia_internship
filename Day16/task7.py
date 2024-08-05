# Copy the contents of data.txt to a new file named data_copy.txt
with open('data.txt', 'r') as source_file:
    with open('data_copy.txt', 'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
