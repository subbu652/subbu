n=int(input())
c=0
for i in range(1,n+1):
    num=int(input())
    if(num%i==0):
        c+=1
if(c==2):
    print("prime number")
else:
    print("not a prime number")
