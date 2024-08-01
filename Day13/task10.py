class InvalidInputError(Exception):
    pass

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def normalize_and_analyze(data):
    # Ensure the input list contains only numeric values and is not empty
    if not data or not all(isinstance(x, (int, float)) for x in data):
        raise InvalidInputError("Input list must contain only numeric values and cannot be empty")
    
    min_val = min(data)
    max_val = max(data)
    
    # Normalize the data to the range 0 to 1
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    
    # Calculate statistical measures
    mean = calculate_mean(normalized_data)
    median = calculate_median(normalized_data)
    variance = calculate_variance(normalized_data, mean)
    
    return normalized_data, {'mean': mean, 'median': median, 'variance': variance}

# Passing Values
data = [10, 20, 30, 40, 50]
try:
    normalized_data, stats = normalize_and_analyze(data)
    print(f"Normalized data: {normalized_data}")
    print(f"Statistics: {stats}")
except InvalidInputError as e:
    print(e)
