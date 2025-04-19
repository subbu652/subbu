r1,r2=map(int,input().split())

for n in range(r1,r2+1):
    s=0
    for i in range(1,n//2+1):
        if(n%i==0):
            s+=i
    if(s==n):
        print(n)

        
