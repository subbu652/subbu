n=int(input())

#wap to print 'true' if given num is EVEN otherwise 'false'
rem=n%2
print(rem<1)
print(rem==0)

#wap to print 'true' if given num is mutliple of 5 otherwise 'false'
a=n%5
print(a==0)


#wap to print 'true' if given num is mutliple of 2 otherwise 'false'
print(n%2==0)

'''

1. n is divided by 2
2. n is multiple of 2                (dividend) - numerator
3. 2 is a factor or divisor of n     (divisor) - denominator

'''
#wap to print 'true' if given num is EVEN and FACTOR of 50 otherwise 'false'
print(50%n==0 and n%2==0)

#wap to print 'true' if given num is odd mutliple of 5 and greater than 100 otherwise 'false'
print(n%10==5 and n>100)
print(n%2!=0 and n%5==0 and n>100)

