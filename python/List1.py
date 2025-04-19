n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
for j in a:
    s=0
    for i in range(1,j):
        if j%i==0:
            s+=i
    if s==j:
        print(j,end=' ')

'''
lst=list(map(int,input().strip().split()))[0:]
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Even:',even,'Odd:',odd)
'''
