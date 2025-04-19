def OperationsBinarystring(binary_str):
    # Check if the input string is null
    if binary_str is None:
        return -1

    # Initialize the result with the first binary digit
    result = int(binary_str[0])

    # Iterate through the binary string, performing bitwise operations based on the characters
    for i in range(1, len(binary_str), 2):
        operator = binary_str[i]
        operand = int(binary_str[i + 1])

        if operator == 'X':
            # XOR operation
            result ^= operand
        elif operator == 'A':
            # AND operation
            result &= operand
        elif operator == 'O':
            # OR operation
            result |= operand

    return result

# Example usage
binary_str = "1X011A0O1"
output = OperationsBinarystring(binary_str)
print(f"Output: {output}")
