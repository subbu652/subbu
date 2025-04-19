# map() and filter() combined
def greater_than_5(n):
    return n>5
def square(n):
    return n**2
li=list(map(int,input().split()))
new_li=list(map(square,filter(greater_than_5,li)))
print(new_li)

'''
def is_even(n):
    return n%2==0
def double(n):
    return n*2
li=list(map(int,input().split()))
double_even=list(map(double,filter(is_even,li)))
print(double_even)


# filter(): to find numbers > 5
li=list(map(int,input().split()))
new_li=list(filter(lambda x:x>5,li))
print(new_li)


values=[1,None,2,4,None,5]
non_none_values=list(filter(None,values))
print(non_none_values)


# filter() to find even numbers
def is_even(x):
    return x%2==0
li=list(map(int,input().split()))
even_num=list(filter(is_even,li))
print(even_num)


# map() with multiple iterables
def add(x,y):
    return x+y
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
print(list(map(add,n2,n1)))


#map(): squares of the elements in a given list
li=list(map(int,input().split()))
print(list(map(lambda x:x**2,li)))


#map(): doubling the elements of a given list
def double(n):
    return n*2
li=list(map(int,input().split()))
new_li=list(map(double,li))
print(new_li)
'''
