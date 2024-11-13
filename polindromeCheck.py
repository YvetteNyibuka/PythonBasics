def palindrome_check(strings):
    result = []
    for string in strings:
        is_palindrome = string == string[::-1]
        result.append((string, is_palindrome))
    return result

strings = ["radar", "hello", "level", "world", "madam"]
print(palindrome_check(strings))
