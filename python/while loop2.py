n=str(input())
l=list(n)
rev=l[::-1]
print(rev)

'''
# to find the given number is Automorphic number or not

n=int(input())
a=n
sq=n**2
b=sq
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
rev1=0
while rev1!=rev and sq!=0:
    rem1=sq%10
    rev1=rev1*10+rem1
    sq//=10
if rev1==rev:
    print(a,b,'YES')
else:
    print(a,b,'NO')



# to find whether the given number is palindrome or notnb121,12,1,0
t=n                   #121
rev=0                 #1,12,121
while n>0:
    r=n%10            #1,2,1
    rev=rev*10+r      #1,12,121
    n//=10            #12,1,0
if t==
rev:
    print('Yes, it is palindrome')
else:
    print('No, it is not a palindrome')
    


#to find given number is happy number or not
n=int(input())
p=n
while n!=1 and n!=4:
    s=0
    t=n
    while t>0:
        r=t%10
        s=s+r*r
        t=t//10
    n=s
if s==1:
    print('Happy number')
else:
    print('Not a Happy number')



# to find given number is Niven/Harshad:sum of fatcors of a number is factor of N.

n=int(input())
temp=n
i=1
s=0
while temp>0:
    rem=temp%10
    s=s+rem
    temp//=10
if n%s==0:
    print(n,'is Harshad number')
else:
    print(n,'is not Harshad number')


        
# how to use flag 
n=int(input())
i=1
flag=False
while i<=2*n:
    if i%2==0:
        if flag:
            print(end=',')
        print(i,end='')
        flag=True
    i+=1
    

# to find product of even digits sum and odd digits sum of a number

n=int(input())
odd=0
even=0
while n>0:
    r=n%10
    if r%2==0:
        even+=r
    else:
        odd+=r
    n//=10
print(even*odd)



# to find sum of digits and product of digits of a number is equal or not
n=int(input())
s=0
p=1
while n>0:
    r=n%10
    s+=r
    p*=r
    n//=10
if s==p:
    print('True')


# to find odd digits sum of a number

n=int(input())
odd_sum=0
while n>0:
    r=n%10
    if r%2!=0:
        odd_sum+=r
    n//=10
print(odd_sum)



# to find even digits count of a number

n=int(input())
count=0
while n>0:
    r=n%10
    if r%2==0:
        count+=1
    n//=10
print(count)


# to find individual digits sum of a number

n=int(input())
sum1=0
while n>0:
    n//=10
    sum1+=1
print(sum1)



# to find individual digits count of a number

n=int(input())
count=0
while n>0:
    n//=10
    count+=1
print(count)



# To print prime number which are less than given number

a=int(input())
for i in range(1,a+1):
    n=1
    c=0
    while n<=i:
        if i%n==0:
            c+=1
        n+=1
    if c==2:
        print(i,end=' ')



# to find given number is perfect number or not

n=int(input())
i=1
sum1=0
while i<=n:
    if n%i==0:
        if i<n:
            sum1+=i
    i+=1
if sum1==n:
    print(n,'is perfect number')
else:
    print(n,'is not perfect number')



# perfect number

n=int(input())
i=1
sum1=0
while i<n:
    if n%i==0:
        sum1+=i
    i+=1
if sum1==n:
    print(n,'is perfect number')
else:
    print(n,'is not perfect number')
'''


