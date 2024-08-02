def transform_string(s):
    s = s.title()
    words = s.split()
    transformed_words = []
    for word in words:
        if word.isdigit():
            transformed_words.append(num2words(int(word)))
        elif len(word) > 5:
            transformed_words.append(word[::-1])
        else:
            transformed_words.append(word)
    return ' '.join(transformed_words)

def num2words(num):
    num_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return ' '.join(num_map[digit] for digit in str(num))

# passing values to the function
print(transform_string("This is an example string with digits 123 and longword."))
