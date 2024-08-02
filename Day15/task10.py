import re

def validate_data(entries):
    report = {'length': [], 'content': [], 'format': []}
    
    for entry in entries:
        length_valid = len(entry) >= 5 and len(entry) <= 20
        content_valid = entry.isalpha() or entry.isnumeric() or entry.isalnum()
        format_valid = bool(re.match(r'^\w+@\w+\.\w+$', entry)) or bool(re.match(r'^\d{4}-\d{2}-\d{2}$', entry))
        
        report['length'].append(length_valid)
        report['content'].append(content_valid)
        report['format'].append(format_valid)
    
    return report

# passing values to the function.
entries = ["hello", "12345", "hello123", "test@example.com", "2024-08-01"]
print(validate_data(entries))
