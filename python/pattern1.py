n =int(input("Enter a number: "))


'''
n = int(input("Enter a number: "))
temp=1
m=n
for i in range(1,n+1):
    p = temp
    for j in range(1,i+1):
        print(p,end=" ")
        p = p-m
    temp = temp+m
    m=m-1
    print()

# Enter a number: 6
# 1
# 7 2
# 12 8 4
# 16 13 10 7
# 19 17 15 13 11
# 21 20 19 18 17 16



n=int(input())
for i in range(1,n+1):
    if i%2==0:
        m=i*n
        for j in range(1,n+1):
            print(m,end=' ')
            m-=1
    else:
        for j in range(1,n+1):
            print((i-1)*n+j,end=' ')
    print()
# input 5
# output
#1 2 3 4 5 
#10 9 8 7 6 
#11 12 13 14 15 
#20 19 18 17 16 
#21 22 23 24 25


n=int(input())
for i in range(1,n+1):
    m=i*i
    for j in range(1,n+1):
        print(m,end=' ')
        m+=1
    print()
# input 5
# output
#1 2 3 4 5 
#4 5 6 7 8 
#9 10 11 12 13 
#16 17 18 19 20 
#25 26 27 28 29



n=int(input())
for i in range(5,0,-1):
    for j in range(1,n+1):
        if i%2==1:
            print(i,end=' ')
        else:
            print(j,end=' ')
    print()
#input 5
# output
#5 5 5 5 5 
#1 2 3 4 5 
#3 3 3 3 3 
#1 2 3 4 5 
#1 1 1 1 1 



n=int(input())
for i in range(1,n+1):
    m=n*i
    for j in range(1,n+1):
        print(m,end=' ')
        m-=1
    print()
#input 5
# output
#5 4 3 2 1 
#10 9 8 7 6 
#15 14 13 12 11 
#20 19 18 17 16 
#25 24 23 22 21



n=int(input())
for i in range(1,n+1):
    m=n
    for j in range(1,n+1):
        if i%2==1:
            print(i,end=' ')
        else:
            print(m,end=' ')
        m-=1
    print()
#input 5
# output
#1 1 1 1 1 
#5 4 3 2 1 
#3 3 3 3 3 
#5 4 3 2 1 
#5 5 5 5 5 



n=int(input())
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(j,end=' ')
    else:
        for j in range(n,0,-1):
            print(j,end=' ')
    print()      
# input =5
#output
#1 2 3 4 5 
#5 4 3 2 1 
#1 2 3 4 5 
#5 4 3 2 1 
#1 2 3 4 5



n=int(input())
asc=ord("a")
for i in range(1,n+1):
    for i in range(asc,asc+i):
        print(chr(j),end=" ")
    print()
'''
