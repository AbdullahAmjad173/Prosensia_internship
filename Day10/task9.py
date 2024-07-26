def replace_occurr(input_string, search_term, replacement_term):
  
    modified_string = input_string.replace(search_term, replacement_term)
    
    return modified_string


original_string = "The quick brown fox jumps over the lazy dog."
search = "fox"
replacement = "cat"

result = replace_occurr(original_string, search, replacement)
print(result) 
