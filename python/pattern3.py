


'''
# number pattern 50
n=int(input())
p1=0
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        p+=p1
        print(p,end=' ')
        p1+=1
    print()

# number pattern 46
n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        print(j if i%2==1 else m,end=' ')
        m-=1
    print()


# number pattern 45
n=int(input())
m=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    print()


# number pattern 39
n=int(input())
for i in range(1,n+1):
    m=1
    for j in range(1,i*2):
        print(m,end=' ')
        m+=1
    print()


# number pattern 40
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1 if i%2==1 else 2*j,end=' ')
    print()


# number pattern 41
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=' ')
    for j in range(i-1,0,-1):
        print(2*j-1,end=' ')
    print()


# number pattern 42
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end=' ')
    for j in range(i-1,0,-1):
        print(2*j,end=' ')
    print()


# number pattern 43
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()



# number pattern 31
n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(n-i+1):
        print(m,end=' ')
        m+=1
    print()


# number pattern 33
n=int(input())
for i in range(n,0,-1):
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    print()



# number pattern 32
n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    print()



# number pattern 30
n=int(input())
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i+j,end=' ')
    print()


# number pattern 29
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(n-j+1,end=' ')
    print()



# number pattern 28
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n-j+1,end=' ')
    print()



# number pattern 27
n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()




# number pattern 26
n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


# number pattern 25
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()



# number pattern 24
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()




# number pattern 23
n=int(input())
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i,end='')
    print()
'''
