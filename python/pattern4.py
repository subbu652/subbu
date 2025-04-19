# This Code is only for Odd inputs
n=int(input("Enter the input:"))
m=n//2+1
for i in range(1,n+1):
    if i<=m:
        for j in range(1,i+1):
            print('*',end=' ')
    else:
        for j in range(1,m):
            print('*',end=' ')
        m-=1
    print()


'''
n=int(input('Enter the input : '))
p,q=1,2
for i in range(1,n+1):
    print('  '*(n-i),end=' ')
    for j in range(1,i+1):
        if i%2==1:
            print(p,end=' ')
            p+=2
        else:
            print(q,end=' ')
            q+=2
    print()

#pattern number 10
n=int(input())
p=2*(n-1)-1
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        if m%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        m-=1
    print('  '*p,end='')
    p-=2
    for j in range(1,i+1):
        if j%2==1 and i!=n:
            print('*',end=' ')
        elif i==n and j<=(i//2):
            print('  *',end=' ')
        else:
            print(' ',end=' ')
    print()
p=1
for i in range(n-1,0,-1):
    m=i
    for j in range(1,i+1):
        if m%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        m-=1
    print('  '*p,end='')
    p+=2
    for j in range(1,i+1):
        if j%2==1 and i!=n:
            print('*',end=' ')
        elif i==n and j<=(i//2):
            print('  *',end=' ')
        else:
            print(' ',end=' ')
    print()



# pattern number 25
n=int(input())
for i in range(1,n):
    m=i
    for j in range(1,i+1):
        if m%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        m-=1
    print()
for i in range(n,0,-1):
    m=i
    for j in range(1,i+1):
        if m%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        m-=1
    print()




# pattern number 24
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'1',end=' ')
    for j in range(2,i+1):
        if j!=i:
            print(i-1,end=' ')
        else:
            print('1',end=' ')
    print()



# pattern number 23
n=int(input())
for i in range(n,0,-1):
    for j in range(1,n*2):
        if i+j==n+1 or (j%2==1 and i==n) or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(2,n+1):
    for j in range(1,n*2):
        if i+j==n+1 or (j%2==1 and i==n) or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



# pattern number 22
n=int(input())
for i in range(1,n):
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n,0,-1):
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



# pattern number 21
n=int(input())
for i in range(n,0,-1):
    for j in range(1,n*2):
        if i+j==n+1 or (j%2==1 and i==n) or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



# pattern number 20
n=int(input())
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j==n+1 or (j%2==1 and i==n) or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



# pattern number 19
n=int(input())
for i in range(1,n):
    print(' '*(i-1),end=' ')
    for j in range(i,n+1):
        print(j,end=' ')
    print()
for i in range(n,0,-1):
    print(' '*(i-1),end=' ')
    for j in range(i,n+1):
        print(j,end=' ')
    print()


# pattern number 18
n=int(input())
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(i,n+1):
        print(j,end=' ')
    print()


# pattern number 17
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)


# pattern number 16
n=int(input())
m=n
for i in range(1,n+1):
    print('* '*m)
    m-=1
for i in range(2,n+1):
    print('* '*i)


# pattern number 15
n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i,end=' ')
    print()


# pattern number 14
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i,end=' ')
    print()


# pattern number 13
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print('*',end=' ')
    print()



# pattern number 12
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()



# pattern number 11
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()


# pattern number 9
n=int(input())
for i in range(1,n):
    print(' '*(n-i)+'* '*i,end=' ')
    print()
for i in range(n,0,-1):
    print(' '*(n-i)+'* '*i,end=' ')
    print()

    
# pattern number 9
n=int(input())
for i in range(1,n):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(n,0,-1):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()


# pattern number 8
n=int(input())
for i in range(1,n+1):
    print(' '*(i-1)+'*'*(n-1))



# pattern number 7
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    p=2
    for j in range(1,i):
        print(p,end=' ')
        p+=1
    print()
        

# pattern number 6
n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        print(m%2,end=' ')
        m-=1
    print()


# pattern number 5
n=int(input())
m=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    print()



# pattern number 4
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# pattern number 3
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()



# pattern number 2
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(i,end=' ')
    print()


# pattern number 1
n=int(input())
for i in range(1,n+2):
    for j in range(1,n+1):
        if i==1 or i==n+1 or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
