a=int(input())
b=int(input())
c=int(input())
d=int(input())

# for voting ,age of a person is eligible or not
print(a>=18)
print(b>17)
print()

# 1st number is greater than all remaining numbers
print(a>b)
print(a>b>c)  # a>b and a>c
print(a>b>c>d)  # a>b and a>c and a>d
print()  # empty line

# 1st number is 2nd greatest number among all numbers
print(a<b)
print(b>a>c or c>a>b) # b>a and a>c or c>a and a>b

# print(b>a>c>d or c>a>b>d or d>a>c>b or b>a>d>c or c>a>d>b or d>a>b>c)

print((b>a and c<a>d) or (c>a and b<a>d) or (d>a and b<a>c))

'''((b>a and a>c and a>d) or (c>a and a>b and a>d) or (d>a and a>b and a>c)or
(b>a and a>d and a>c)or (c>a and a>d and a>b) or (d>a and a>c and a>b))'''

