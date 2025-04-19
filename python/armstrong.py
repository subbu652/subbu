num=int(input())
temp=num
s=0
while(temp>0):
    rem=temp%10
    s=s+rem**3
    temp=temp//10
if(num==s):
    print(num,"Armstrong")
else:
    print(num,"Not armstrong")
