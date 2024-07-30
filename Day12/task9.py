def split_and_join_conditionally(string, split_delim, join_delim, condition):
    # Split the string by the first delimiter
    parts = string.split(split_delim)
    # Filter the parts that meet the condition
    filtered_parts = [part for part in parts if condition(part)]
    # Join the filtered parts using the second delimiter
    return join_delim.join(filtered_parts)


input_string = "apple;banana;cherry;date"
split_delim = ";"
join_delim = ","
condition = lambda x: len(x) > 3

result = split_and_join_conditionally(input_string, split_delim, join_delim, condition)
print(result)  # Output: "apple,banana,cherry"
