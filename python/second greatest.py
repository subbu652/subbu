a=int(input())
b=int(input())
c=int(input())
d=int(input())

# print(b>a>c>d or c>a>b>d or d>a>c>b or b>a>d>c or c>a>d>b or d>a>b>c)

print((b>a and c<a>d) or (c>a and b<a>d) or (d>a and b<a>c))

'''((b>a and a>c and a>d) or (c>a and a>b and a>d) or (d>a and a>b and a>c)or
(b>a and a>d and a>c)or (c>a and a>d and a>b) or (d>a and a>c and a>b))'''



