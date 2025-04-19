def Autocount(n):
    # Check if the length of the input is greater than 10 characters
    if len(n) > 10:
        return 0

    count = 0

    # Iterate through each character in the string
    for i in range(len(n)):
        digit_count = int(n[i])

        # Count the occurrences of the digit at its position
        if n.count(str(i)) == digit_count:
            count += 1

    return count

# Example usage
input_str = str(input())
output = Autocount(input_str)
print(f"Output: {output}")
