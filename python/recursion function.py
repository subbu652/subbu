# re-fun 10
def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
n=int(input())
print(fun(n))

'''
# re-fun 9
def fun(n):
    if n%2:
        print(n,end=' ')
    if n:
        fun(n-1)
    if n%2==1:
        print(n,end=' ')
n=int(input())
fun(n)


# re-fun 8
def fun(n):
    if n%2==0:
        print(n,end=' ')
    if n:
        fun(n-1)
    if n%2==1:
        print(n,end=' ')
n=int(input())
fun(n)


# re-fun 7
def fun(n):
    if n:
        fun(n-1)
    if n%2==0:
        print(n,end=' ')
n=int(input())
fun(n)


# re-fun 6
def fun(n):
    if n%2==0:
        print(n,end=' ')
    if n:
        fun(n-1)
n=int(input())
fun(n)


# re-fun 5
def fun(n):
    print(n,end=' ')
    if n:
        fun(n-1)
    print(n,end=' ')
n=int(input())
fun(n)


# re-fun 4
def fun(n):
    print(n,end=' ')
    if n:
        fun(n-1)
n=int(input())
fun(n)


# re-fun 3
def fun(n):
    if n:
        fun(n-1)
    print(n,end=' ')
n=int(input())
fun(n)


# re-fun 2
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n,end=' ')
    
n=int(input())
fun(n)


# re-fun 1
def fun(n):
    if n==0:
        return
    print(n,end=' ')
    fun(n-1)
n=int(input())
fun(n)



def even(n):
    if n%2==1:
        n=n-1
        if n>2:
            even(n-2)
        print(n,end=' ')
    else:
        if n>2:
            even(n-2)
        print(n,end=' ')
n=int(input())
even(n)
        
def even(n):
    if n>1:
        even(n-1)
    if n%2==0:
        print(n,end=' ')
n=int(input())
even(n)
'''
