def calculate(m, n):
    # Ensure m > n and both are non-negative
    if m < 0 or n < 0:
        return "Invalid input"

    # Initialize the sum
    total_sum = 0

    # Iterate through the range from n to m (inclusive)
    for num in range(m, n + 1):
        # Check if the number is divisible by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            # Add the number to the sum
            total_sum += num

    return total_sum

# Example usage
m1,n1=map(int,input().split())
output = calculate(m1,n1)
print(f"Output : {output}")
