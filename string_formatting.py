def string_lengths(strings):
    return {string: len(string) for string in strings}


strings = input(str())
result = string_lengths(strings)
print(result)
