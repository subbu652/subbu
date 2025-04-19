n=int(input())
s=0
while(n>0):
    r=n%10
    s=r*r+s
    n=n//10
print(s)
