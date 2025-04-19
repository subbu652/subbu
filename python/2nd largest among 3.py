a=int(input())
b=int(input())
c=int(input())
if (a>b>c or c>b>a):
    print(b,'is the second largest number')
else:
    if(b>a>c or c>a>b):
        print(a,'is the second largest number')
    else:
        print(c,'is the  second largest number')
