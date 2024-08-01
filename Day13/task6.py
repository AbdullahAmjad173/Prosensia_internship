def interpolate_string(template, values):
    for key, value in values.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template

# passing values
template = "My name is {name} and I am {age} years old."
values = {"name": "Alice", "age": 30}
formatted_string = interpolate_string(template, values)
print(formatted_string)