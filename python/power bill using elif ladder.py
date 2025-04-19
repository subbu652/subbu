n=int(input())
if 100<n<=200:
    print((n-100)*5)
elif n>200:
    print((n-100-(n-200))*5+(n-200)*10)
else:
    print('No Charge')
