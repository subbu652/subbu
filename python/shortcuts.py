# n = int(input('Enter a number: '))
# squares = [ i**2 for i in range(1,n+1)]
# print(squares)

# sq_dict = { f"square value of {i}" : i*i for i in range(1,n+1) }
# print(sq_dict)

# a,b,c =map(int,input('enter some values :').split())
# print(a,b,c)
#
# a,b = 10,20
# print(a+b)

# words = ["I", "am", "Omkaram", "Subbaraju"]
# print(" ".join(words))

# a,b =map(int,input('Enter some values :').split())
# print(a if a>b else b)

# li = list(map(int,input().split()))
# for index,item in enumerate(li):
#     print(f"index {index+1} :",item)

# from itertools import zip_longest
# list1 = [1,2,3]
# list2 = ['a','b']
# zipped = zip_longest(list1,list2,fillvalue='N/A')
# print(list(zipped))

items = list(map(int,input("Enter values :").split()))
check = any(item%2==0 for item in items)
print(check)
#
# print("Sum of numbers:",sum(items))
# print("Max value in items:",max(items))
# print("Min value in items:",min(items))

# i=j=[3]
# i+=j
# print(i,j)