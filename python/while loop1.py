n = int(input())
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

'''
s= input("Enter a string: ")
for i in s:
    if i in "aeiouAEIOU":
        print(i,end=" ")

n = int(input())
prime_numbers = []
num = 2

while len(prime_numbers) < n * (n + 1) // 2:
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        prime_numbers.append(num)
    num += 1

k = 1
index = 0
while index < len(prime_numbers):
    for i in range(k):
        if index < len(prime_numbers):
            print(prime_numbers[index], end=' ')
            index += 1
    print()
    k += 1


# To print prime number which are less than given number

a=int(input())
i=1
while i<=a:
    n=1
    c=0
    while n<=i:
        if i%n==0:
            c+=1
        n+=1
    if c==2:
        print(i,end=' ')
    i+=1


# to print 'n' even numbers

n=int(input())
i=1
while i<=n*2:
    if i%2==0 and i<n*2:
        print(i,end=',')
    if i==n*2:
        print(i)
    i+=1

# sum of factors of a given number

n=int(input())
i=1
sum=0
while i<=n:
    if n%i==0:
        sum+=i
    i+=1
print(sum)


1. sum of n alternate even numbers 

n=int(input())
i=n
sum=0
while i>=1:
    if i%2==0:
        if i%4!=0:
            sum+=i
    i-=1
print(sum)


2. sum of natural numbers without formula

n=int(input())
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)


3. count of even numbers

n=int(input())
i=n
count=0
while i>=1:
    if i%2==0:
        count+=1
    i=i-1
print(count)


4. factors of a number

n=int(input())
i=n
while i>=1:
    if n%i==0:
        print(i,end=" ")
    i-=1


    
5. Even numbers DESC order

n=int(input())
i=n
while i>=1:
    if i%2==0:
        print(i,end=" ")
    i=i-1



6. Even numbers ASC order

n=int(input())
i=1
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i=i-1
    


7. n - natural numbers ASC order

n=int(input())
i=1
while i<=n:
    print(i,end=" ")
    i+=1



8. n - natural numbers DESC order

n=int(input())
i=n
while i>=1:
    print(i,end=" ")
    i-=1
    
'''



