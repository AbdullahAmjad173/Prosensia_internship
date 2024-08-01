def match_pattern(s, pattern):
    if len(s) != len(pattern):
        return False
    
    for char_s, char_pattern in zip(s, pattern):
        if char_pattern.isalpha() and not char_s.isalpha():
            return False
        if char_pattern.isdigit() and not char_s.isdigit():
            return False
    
    return True

# Passing Values
s = "a1b2"
pattern = "a1b2"
result = match_pattern(s, pattern)
print(f"Pattern matches: {result}")
