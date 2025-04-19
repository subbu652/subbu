y=int(input())
if(y%100==0):
    if(y%400==0):
        print('leap year')
    else:
        print('non leap year')
else:
    if(y%4==0):
        print('leap year')
    else:
        print('non leap year')
