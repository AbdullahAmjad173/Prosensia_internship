import re

def extract_dates(input_string):
    date_pattern = r'\b\d{4}[-/]\d{2}[-/]\d{2}\b'
    dates = re.findall(date_pattern, input_string)
    return dates

# passing values to the function.
print(extract_dates("The event is on 2023-08-15 and the deadline was 2023-07-31."))
