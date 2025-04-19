# 8)sum of squares of individual digits of a number
def fun(n):
    r=n%10
    if n==0:
        return 0
    else:
        return r**2+fun(n//10)
a=int(input())
print(fun(a))


'''
# 7)sum of even digits of a number
def fun(n):
    if n==0:
        return 0
    r=n%10
    if r%2==0:
        return r+fun(n//10)
    else:
        return fun(n//10)
a=int(input())
print(fun(a))


# 6)sum of even digits of a number
def fun(n):
    r=n%10
    if n==1:
        return 1
    elif r%2==1:
        return 1+fun(n//10)
    else:
        return fun(n//10)
a=int(input())
print(fun(a))


# 5) sum of n even numbers
def fun(n):
    if n==2:
        return 2
    elif n%2==0:
        return n+fun(n-1)
    else:
        return fun(n-1)
a=int(input())
print(fun(a*2))



# 4)sum of odd numbers upto n
def fun(n):
    if n==1:
        return 1
    elif n%2==1:
        return n+fun(n-1)
    else:
        return fun(n-1)
a=int(input())
print(fun(a))


# 3)count of even numbers upto n
def fun(n):
    if n==2:
        return 1
    elif n%2==0:
        return 1+fun(n-1)
    else:
        return fun(n-1)
a=int(input())
print(fun(a))


# 2) sum of factors of a number
def fun(n,i=1):
    if i>n:
        return 0
    elif n%i==0:
        return i+fun(n,i+1)
    else:
        return fun(n,i+1)
n=int(input())
print(fun(n))


# 1) count of factors of a number
def fun(n,i=1):
    if i>n:
        return 0
    elif n%i==0:
        return 1+fun(n,i+1)
    else:
        return fun(n,i+1)
n=int(input())
print(fun(n))



def factors(n,i=1):
    if n%i==0:
        print(i,end=' ')
    if i<n:
        factors(n,i=i+1)
n=int(input())
factors(n)


def sum_even(n):
    if n%2==1:
        n=n-1
        if n==2:
            return 2
        return n+sum_even(n-2)
    else:
        if n==2:
            return 2
        return n+sum_even(n-2)
n=int(input())
print(sum_even(n))
'''
