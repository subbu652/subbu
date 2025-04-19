
'''
n = int(input())
caps = ord('A')
sm = ord('a')
count = 1
for i in range(n):
    for j in range(i+1):
        if count%2==0:
            print(chr(sm),end=" ")
        else:
            print(chr(caps), end =" ")
        count +=1
        sm+=1
        caps+=1
    print()


n = int(input())
k = ord('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()
# 5
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 


n = int(input())
li = list(map(int, input().split()))
n_li = []
for i in li:
    temp = i
    for j in li:
        if j>temp:
            temp=j
    if len(n_li)==2:
        print(temp)
        break
    n_li.append(temp)
    li.remove(temp)

def scores(s):
    c1,c2=0,0
    hs,ls=0,0
    for i in s:
        if hs==0 and ls==0:
            hs=i
            ls=i
        elif i>hs:
            hs=i
            c1+=1
        elif i<ls:
            ls=i
            c2+=1
        else:
            continue
    print(c1,c2)
n=int(input())
s=list(map(int,input().split()))
scores(s)


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')


a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    c1=0
    for j in range(1,i+1):
        if i%j==0:
            c1+=1
    n=i+6
    if n<b:
        c2=0
        for k in range(1,n+1):
            if n%k==0:
                c2+=1
    if c1==2==c2:
        print(i,i+6,end='  ')
        c+=1
print(c)



n=int(input())
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i,end=' ')
        
        
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(i)
    print()
'''
