def flatten_list(nested_list):
    flat_list = []
    max_depth = 0
    
    def flatten_helper(lst, depth):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for item in lst:
            if isinstance(item, list):
                flatten_helper(item, depth + 1)
            else:
                flat_list.append(item)
    
    flatten_helper(nested_list, 1)
    return flat_list, max_depth

# Passing values
nested_list = [1, [2, [3, 4], 5], 6]
flat_list, depth = flatten_list(nested_list)
print(f"Flattened list: {flat_list}")
print(f"Original depth: {depth}")
