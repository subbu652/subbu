def split_and_sum(arr):
    # Separate even and odd elements
    even_array = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd_array = [arr[i] for i in range(len(arr)) if i % 2 != 0]

    # Sort even and odd arrays in ascending order
    even_array.sort()
    odd_array.sort()

    # Calculate the sum of the second largest elements
    sum_second_largest = 0

    # Check if even array has more than one element
    if len(even_array) > 1:
        sum_second_largest += even_array[-2]

    # Check if odd array has more than one element
    if len(odd_array) > 1:
        sum_second_largest += odd_array[-2]

    return sum_second_largest

# Example usage
array_size = 5
elements = [3, 4, 1, 7, 9]

print("Element at 0 index:", elements[0])
print("Element at 1 index:", elements[1])
print("Element at 2 index:", elements[2])
print("Element at 3 index:", elements[3])
print("Element at 4 index:", elements[4])

result = split_and_sum(elements)
print("Sum of the second largest numbers from both even and odd arrays:", result)
