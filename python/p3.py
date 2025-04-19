def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    if sorted(str1) == sorted(str2):
        return 'Yes'
    else:
        return 'No'

# Example usage
input_str1,input_str2=list(map(str,input().split()))
output = are_anagrams(input_str1, input_str2)
print(f"Output: {output}")
