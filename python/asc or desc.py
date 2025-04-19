a=int(input())
b=int(input())
c=int(input())
if(a>b>c):
    print('DESCENDING')
elif(c>b>a):
    print('ASCENDING')
else:
    print('NOT IN BOTH ASCENDING AND DESCENDING')
