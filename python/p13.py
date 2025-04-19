def MaxInArray(arr, length):
    # Check if the array is empty
    if length == 0:
        print("Array is empty")
        return

    # Initialize variables to store the maximum element and its index
    max_element = arr[0]
    max_index = 0

    # Iterate through the array to find the maximum element and its index
    for i in range(1, length):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i

    # Print the maximum element and its index
    print(max_element)
    print(max_index)

# Example usage
arr = list(map(int,input().split()))
length = len(arr)
MaxInArray(arr, length)
