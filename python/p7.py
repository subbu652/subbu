def ReplaceCharacter(str1, ch1, i, ch2):
    # Convert the string to a list to make modifications easier
    str_list = list(str1)

    # Iterate through the characters of the string
    for index, char in enumerate(str_list):
        # Check if the character is equal to ch1
        if char == ch1:
            # Replace ch1 with ch2
            str_list[index] = ch2
        # Check if the character is equal to ch2
        elif char == ch2:
            # Replace ch2 with ch1
            str_list[index] = ch1

    # Convert the list back to a string
    result_str = ''.join(str_list)

    return result_str

# Example usage
str_input = str(input(''))
ch1_input,ch2_input=map(str,input().split())
output = ReplaceCharacter(str_input, ch1_input, 1, ch2_input)
print(f"Output: {output}")
