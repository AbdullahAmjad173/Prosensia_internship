def transform_string(string):

    result = {
        "lowercase": string.lower(),
        "uppercase": string.upper(),
        "titlecase": string.title()
    }
    
    return result


input_string = "hello world"
transformed = transform_string(input_string)
print(transformed)

