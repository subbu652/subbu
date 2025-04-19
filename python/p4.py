def Productsmallpair(sum, arr):
    # Check if the array has less than 2 elements or is empty
    if len(arr) < 2:
        return -1

    # Sort the array in ascending order
    arr.sort()

    # Initialize variables to store the indices of the two smallest elements
    index_j = 0
    index_k = 1

    # Iterate through the array to find the two smallest elements
    for i in range(2, len(arr)):
        if arr[i] < arr[index_j]:
            index_k = index_j
            index_j = i
        elif arr[i] < arr[index_k] and arr[i] != arr[index_j]:
            index_k = i

    # Calculate the product of the two smallest elements
    product = arr[index_j] * arr[index_k]

    # Check if the sum of the two smallest elements is less than the given sum
    if arr[index_j] + arr[index_k] < sum:
        return product
    else:
        return 0

# Example usage
sum1 =int(input())
arr1 =list(map(int,input().split()))
output1 = Productsmallpair(sum1, arr1)
print(f"Output 1: {output1}")
