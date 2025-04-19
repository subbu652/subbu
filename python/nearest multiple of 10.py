'''n=int(input())
r=n%10
if r>=5:
    print(n+10-r)
else:
    print(n-r)'''

n=int(input())
r=n%10
if r<=4:
    print(n//10*10)
else:
    print(n//10*10+10)
