def Frequentcharacter(s, x):
    # Count the occurrences of each character in the string
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum frequency and lowest ASCII value
    max_char = max(char_count, key=lambda k: (char_count[k], ord(k)))

    # Replace all occurrences of the most frequent character with 'x'
    result = ''.join(x if char == max_char else char for char in s)

    return result

# Example usage
str_input = str(input(''))
char_x = str(input(''))
output = Frequentcharacter(str_input, char_x)
print(f"Output: {output}")
