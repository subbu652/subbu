n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(' *'*n,end='')
    else:
        print('* '*n,end='')
    print()
# input 5
# output
#* * * * * 
# * * * * *
#* * * * * 
# * * * * *
#* * * * *

'''
n=int(input())
for i in range(1,n+1):
    if i==1:
        print(1,end=' ')
    else:
        p=i+1
        for j in range(1,i):
            print(p,end=' ')
            p+=1
    q=2*i-2
    for j in range(1,i):
        print(q,end=' ')
        q-=1
    print()
# input 5
# output
#1 
#3 2 
#4 5 4 3 
#5 6 7 6 5 4 
#6 7 8 9 8 7 6 5



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('  '*(2*(n-i)),end='')
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    print()
# input 5
# output
#1                 1 
#1 2             2 1 
#1 2 3         3 2 1 
#1 2 3 4     4 3 2 1 
#1 2 3 4 5 5 4 3 2 1


   
n=int(input())
t=0
for i in range(1,n+1):
    t=t+i
    m=t
    p=t-i+1
    for j in range(1,i+1):
        print(p if i%2==1 else m,end=' ')
        p+=1
        m-=1
    print()
#input 5
# output
#1 
#3 2 
#4 5 6 
#10 9 8 7 
#11 12 13 14 15



n=int(input())
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i<=(n+1)//2:
            print(p,end=' ')
        else:
            print(n-i+1,end=' ')
    p+=1
    print()
#input 5
# output
#1 
#2 2 
#3 3 3 
#2 2 2 2 
#1 1 1 1 1



n=int(input())
for i in range(1,n+1):
    p=n
    m=i
    for j in range(1,i+1):
        if j==1:
            print(i,end=' ')
        else:
            m+=p
            print(m,end=' ')
        p-=1
    print() 
#input 5
#output
#1 
#2 6 
#3 7 10 
#4 8 11 13 
#5 9 12 14 15



n=int(input())
p1=0
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        p+=p1
        print(m,end=' ')
        p1+=1
    print()
# input 5
#output
#1 
#2 4 
#7 11 16 
#22 29 37 46 
#56 67 79 92 106



n=int(input())
m=1
for i in range(1,n+1):
    p=m
    for j in range(1,2**(i-1)+1):
        print(p,end=' ')
        p+=1
        if p>9:
            p=p-9
    m=p
    print()
#input 5
#output
#1 
#2 3 
#4 5 6 7 
#8 9 1 2 3 4 5 6 
#7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4
        


n=int(input())
for i in range(1,n+1):
    t=i
    for j in range(1,i+1):
        if i%2==1:
            print(j,end=' ')
        else:
            print(t,end=' ')
        t-=1
    print()
# input 5
# output
#1 
#2 1 
#1 2 3 
#4 3 2 1 
#1 2 3 4 5



n=int(input())
m=1
for i in range(1,n+1):
    p=m
    for j in range(1,i+1):
        print(p,end=' ')
        p+=1
    m=p
    print()
# input 5
# output
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15



n=int(input())
for i in range(1,n+1):
    m=1
    for j in range(1,2*i):
        if j<i:
            print(m,end=' ')
            m+=1
        else:
            print(m,end=' ')
            m-=1
    print()
# input 5
#output
#1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1 



n=int(input())
for i in range(1,n+1):
    m=2
    for j in range(1,2*i):
        if j<i:
            print(m,end=' ')
            m+=2
        else:
            print(m,end=' ')
            m-=2
    print()
# input 5
# output
#2 
#2 4 2 
#2 4 6 4 2 
#2 4 6 8 6 4 2 
#2 4 6 8 10 8 6 4 2



n=int(input())
for i in range(1,n+1):
    m=1
    for j in range(1,2*i):
        if j<i:
            print(m,end=' ')
            m+=2
        else:
            print(m,end=' ')
            m-=2
    print()
# input 5
# output
#1 
#1 3 1 
#1 3 5 3 1 
#1 3 5 7 5 3 1 
#1 3 5 7 9 7 5 3 1



n=int(input())
for i in range(1,n+1):
    if i%2==0:
        p=2
        for j in range(1,i+1):
            print(p,end=' ')
            p+=2
    else:
        p=1
        for j in range(1,i+1):
            print(p,end=' ')
            p+=2
    print()
# input 5
# output
#1 
#2 4 
#1 3 5 
#2 4 6 8 
#1 3 5 7 9 




n=int(input())
for i in range(1,n+1):
    for j in range(1,2*i):
        print(j,end=' ')
    print()
#input 5
# output
#1 
#1 2 3 
#1 2 3 4 5 
#1 2 3 4 5 6 7 
#1 2 3 4 5 6 7 8 9



n=int(input())
p=n
for i in range(1,n+1):
    m=p
    for j in range(1,p+1):
        print(m,end=' ')
        m+=1
    p-=1
    print()
# input 5
# output
#5 6 7 8 9 
#4 5 6 7 
#3 4 5 
#2 3 
#1 


n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    print()
# input 5
# output
#1 
#2 3 
#3 4 5 
#4 5 6 7 
#5 6 7 8 9



n=int(input())
p=n
for i in range(1,n+1):
    m=i
    for j in range(1,p+1):
        print(m,end=' ')
        m+=1
    p-=1
    print()
#input 5
#output
#1 2 3 4 5 
#2 3 4 5 
#3 4 5 
#4 5 
#5 



n=int(input())
p=n
for i in range(1,n+1):
    m=p
    for j in range(1,i+1):
        print(m,end=' ')
        m+=1
    p-=1
    print()
#input 5
# output
#5 
#4 5 
#3 4 5 
#2 3 4 5 
#1 2 3 4 5 


n=int(input())
p=1
for i in range(n,0,-1):
    m=n
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    p+=1
    print()
#input 5
#output
#5 4 3 2 1 
#5 4 3 2 
#5 4 3 
#5 4 
#5


n=int(input())
p=n
for i in range(n,0,-1):
    m=n
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    p-=1
    print()
#input 5
#output
#5 4 3 2 1 
#5 4 3 2 
#5 4 3 
#5 4 
#5



n=int(input())
for i in range(1,n+1):
    m=n
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    print()
# input 5
# output 5
#5 
#5 4 
#5 4 3 
#5 4 3 2 
#5 4 3 2 1



n=int(input())
for i in range(1,n+1):
    m=i
for j in range,i+1):
        print(m,end=' ')
        m-=1
    print()
# input 5
#output
#1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1



n=int(input())
m=n
for i in range(1,n+1):
    p=m
    for j in range(1,n-i+2):
        print(p,end=' ')
        p-=1
    m-=1
    print()
    ArithmeticError#input 5
# output
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1



n=int(input())
m=n
for i in range(1,n+1):
    for j in range(1,i+1):
        print(m,end=' ')
    m-=1
    print()
#input
#output
#5 
#4 4 
#3 3 3 
#2 2 2 2 
#1 1 1 1 1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#input 5
# output
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5



n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=' ')
    print()
#input 5
# output
#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i%2,end=' ')
    print()
# input 5
#output
#1 
#0 0 
#1 1 1 
#0 0 0 0 
#1 1 1 1 1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2,end=' ')
    print()
#input 5
#output
#1 
#1 0 
#1 0 1 
#1 0 1 0 
#1 0 1 0 1 



n=int(input())
p=0
for i in range(1,n+1):
    p+=i
    if  i%2==0:
        m=p
        for j in range(1,n+1):
            print(m,end=' ')
            m+=1
    else:
        for j in range(1,n+1):
            print((i-1)*5+j,end=' ')
    print()
#input 5
#output
#1 2 3 4 5 
#3 4 5 6 7 
#11 12 13 14 15 
#10 11 12 13 14 
#21 22 23 24 25
            
      
n=int(input())
p=0
for i in range(1,n+1):
    p=p+i
    for j in range(1,n+1):
      print(p+j-1,end=' ')
    print()
#input 5
# output
#1 2 3 4 5 
#3 4 5 6 7 
#6 7 8 9 10 
#10 11 12 13 14 
#15 16 17 18 19




n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
#input 5
# output
#1         
#1 2       
#1 2 3     
#1 2 3 4   
#1 2 3 4 5 



n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j>i:
            print(' ',end=' ')
        else:
            print(j,end=' ')
    print()
#input 5
#output
#        1 
#      2 1 
#    3 2 1 
#  4 3 2 1 
#5 4 3 2 1



n=int(input())
for i in range(1,n+1):
    m=i
    for j in range(1,n+1):
        if m<=n:
            print(m,end=' ')
        else:
            print(m-n,end=' ')
        m+=1
    print()
#input 5
# output
#1 2 3 4 5 
#2 3 4 5 1 
#3 4 5 1 2 
#4 5 1 2 3 
#5 1 2 3 4




#this program same as above
n=int(input())
for i in range(1,n+1):
    s=0
    for k in range(1,i+1):
        s+=k
    p=s
    for j in range(1,n+1):
      print(p,end=' ')
      p+=1
    print()




n=int(input())
p=n*n
for i in range(1,n+1):
    for j in range(1,n+1):
        print(p,end=' ')
        p-=1
    print()

# input 5
# output
#25 24 23 22 21 
#20 19 18 17 16 
#15 14 13 12 11 
#10 9 8 7 6 
#5 4 3 2 1 

  

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n) and (j==1 or j==n):
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
# input 5
#output
#1 0 0 0 1 
#0 0 0 0 0 
#0 0 0 0 0 
#0 0 0 0 0 
#1 0 0 0 1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n+1)//2==j or (i==1 or i==n) and (j==1 or j==n):
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
# input 5
# output
#1 0 0 0 1 
#0 0 0 0 0 
#0 0 1 0 0 
#0 0 0 0 0 
#1 0 0 0 1 



n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=' ')
    print()
# input 5
# output
#5 4 3 2 1 
#5 4 3 2 1 
#5 4 3 2 1 
#5 4 3 2 1 
#5 4 3 2 1



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n+1)//2==j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
# input 5
# output:
#1 1 1 1 1 
#1 0 0 0 1 
#1 0 1 0 1 
#1 0 0 0 1 
#1 1 1 1 1



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n+1)//2==j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
# input 5
# output
#0 0 0 0 0 
#0 0 0 0 0 
#0 0 1 0 0 
#0 0 0 0 0 
#0 0 0 0 0



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==5 or j==1 or j==5:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
# input 5
#output
#1 1 1 1 1 
#1 0 0 0 1 
#1 0 0 0 1 
#1 0 0 0 1 
#1 1 1 1 1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==5:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
#input 5
# output
#1 1 1 1 1 
#0 0 0 0 0 
#0 0 0 0 0 
#0 0 0 0 0 
#1 1 1 1 1 



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==5:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
#input 5
# output
#1 0 0 0 1 
#1 0 0 0 1 
#1 0 0 0 1 
#1 0 0 0 1 
#1 0 0 0 1 



n=int(input())
m=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if m==j or i==j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    m-=1
    print()
#input 5
# output
#1 0 0 0 1 
#0 1 0 1 0 
#0 0 1 0 0 
#0 1 0 1 0 
#1 0 0 0 1



n=int(input())
m=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if m==j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    m-=1
    print()
#input 5
# output
#0 0 0 0 1 
#0 0 0 1 0 
#0 0 1 0 0 
#0 1 0 0 0 
#1 0 0 0 0



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
#input 5
#output
#1 0 0 0 0 
#0 1 0 0 0 
#0 0 1 0 0 
#0 0 0 1 0 
#0 0 0 0 1

'''



