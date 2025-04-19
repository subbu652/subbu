# string = "banana"
# d = {}
# def fun(s):
#     for i in s:
#         d[i] = s.count(i)
#     print(d)
# fun(string)


def rectangle(l,b):
    for j in range(1,b+1):
        for i in range(1,l+1):
            if j==1 or j == b or i==1 or i==l:
                print("* ", end="")
            else:
                print("  ",end='')
        print()
rectangle(5,3)






