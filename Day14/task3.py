import ast

def dict_to_str_and_back(input_dict):
    try:
        # Convert dictionary to string
        str_representation = str(input_dict)
        
        # Convert string back to dictionary
        output_dict = ast.literal_eval(str_representation)
        
        return output_dict
    
    except Exception as e:
        # Log the error and return the original input and error message
        return {"input": input_dict, "error": str(e)}

# Send the input depict. 
input_dict = {"key1": "value1", "key2": "value2"}
result = dict_to_str_and_back(input_dict)
print(result)
