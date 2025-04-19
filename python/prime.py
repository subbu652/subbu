n=int(input())
p=1
s=[]
while len(s)!=(n*(n+1)//2):
    c=0
    for i in range(1,p+1):
        if p%i==0:
            c+=1
    if c==2:
        s.append(p)
    p+=1
print(s)
for i in range(1,n+1):
    p,m=i-1,n-1
    for j in range(1,i+1):
        print(s[p],end=' ')
        p+=m
        m-=1
    print()

'''
def prime_or_not(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,'is prime')
    else:
        print(n,'is not a prime')
'''       
