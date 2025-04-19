def DectoNBase(n, num):
    # Check if n is within the valid range
    if not (1 < n <= 36):
        return "Invalid base"

    # Define the symbols for the first 36 digits
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Initialize an empty string to store the n-based result
    result = ""

    # Perform the conversion process
    while num > 0:
        remainder = num % n
        result = symbols[remainder] + result
        num //= n

    return result

# Example usage
N,Num=map(int,input().split())
output = DectoNBase(N, Num)
print(f"Output : {output}")

