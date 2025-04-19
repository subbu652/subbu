def LargeSmallSum(arr):
    # Check if the array is empty or has length less than 3
    if len(arr) == 0 or len(arr) < 3:
        return 0

    # Extract elements at odd and even positions
    odd_elements = arr[1::2]  # Elements at odd positions
    even_elements = arr[0::2]  # Elements at even positions

    # Sort the arrays in ascending order for odd and descending order for even
    odd_elements.sort()
    even_elements.sort(reverse=True)

    # Take the second smallest element at odd position
    second_smallest_odd = odd_elements[1]

    # Take the second largest element at even position
    second_largest_even = even_elements[1]

    # Return the sum of the two elements
    return second_smallest_odd + second_largest_even

# Example usage
arr = list(map(int,input().split()))
output = LargeSmallSum(arr)
print(f"Output: {output}")
