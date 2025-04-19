s = input()
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')

'''
s=str(input())
stack=[]
for x in s:
    if x in '({[':
        stack.append(x)
    elif x in ')}]':
        if x=='}' and stack[-1]=='{' or x==']' and stack[-1]=='[' or x==')' and stack[-1]=='(':
            stack.pop()
    else:
        break
if not stack:
    print('Balanced')
else:
    print('Un-balanced')


#capitalize()
string='my name is subbu'
print(string.capitalize())

#casefold()
string='My Name Is Subbu'
print(string.casefold())

#center
string='RAMANA'
print(string.center(10))
print(string.center(19,'$'))

#count
string='RAMANA SUbbu'
print(string.count('u'),string.count('a'))

#find
st=' this is first text'
print(st.find('is'))
print(st.find('ir'))

#endswith
st=' this is first text'
print(st.endswith('text'))

#index
st=' this is first text'
print(st.index('i',3,10))

#expandtabs
st='D\te\tm\to\t'
print(st.expandtabs(0))

#isalnum
st='Guna369'
print(st.isalnum(),'is alnum')

##isalpha
st='RAM'
print(st.isalpha(),'is decimal')

#isdecimal
s='12'
print(s.isdecimal())

#isdigit
d='4567'
print(d.isdigit(),'is digit')

#isidentifier
d='demo02'
print(d.isidentifier(),'is identifier')

#islower
s='Subba Raju'
print(s.islower(),'is lower')

#isnumeric
d='345'
print(d.isnumeric(),'is numeric')

#issapce
s='demo'
print(s.isspace(),'is space')

#istitle
s='The Loin King'
print(s.istitle(),'is title')

#isupper
s='SUBBu'
print(s.isupper(),'is upper')

#lower
s='SUBBU'
print(s.lower())

#join
s={'Siva','Rama','Raju'}
sep='_#_'
print(sep.join(s))

#lstrip
s='    Subba Raju'
print(s.lstrip())

#replace
s='RAMANA'
print(s.replace('A','@'))

#rfind, rindex
s='this is subbu'
print(s.rfind('subbu'),s.rindex('subbu'))

# rsplit, rstrip
s='Siva,RAMA,Raju'
print(s.rsplit(',',10),s.rstrip('#'))

#split
s='one two three four'
print(s.split())

#splitlines
s='one\ntwo\nthree\nfour'
print(s.splitlines())

'''













