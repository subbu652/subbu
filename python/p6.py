def Numberofcarry(num1, num2):
    carry_count = 0
    carry = 0

    # Iterate through the digits from right to left
    while num1 > 0 or num2 > 0:
        # Extract the rightmost digits of num1 and num2
        digit1 = num1 % 10
        digit2 = num2 % 10

        # Calculate the sum along with the carry from the previous operation
        total = digit1 + digit2 + carry

        # Update the carry for the next iteration
        carry = total // 10

        # Check if there is a carry for the current operation
        if carry > 0:
            carry_count += 1

        # Move to the next digits
        num1 //= 10
        num2 //= 10

    return carry_count

# Example usage
num1_1, num2_1 = map(int,input().split())
output1 = Numberofcarry(num1_1, num2_1)
print(f"Output 1: {output1}")
