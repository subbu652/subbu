def differenceofSum(m, n):
    # Calculate the sum of integers divisible by m
    sum_divisible_by_m = m * (m + n) // 2

    # Calculate the sum of all integers from 1 to n
    total_sum = n * (n + 1) // 2

    # Calculate the sum of integers not divisible by m
    sum_not_divisible_by_m = total_sum - sum_divisible_by_m

    # Calculate the difference
    result = sum_not_divisible_by_m - sum_divisible_by_m

    return result
m,n=map(int,input().split())
output = differenceofSum(m,n)
print(f"Output : {output}")

