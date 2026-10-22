#       1

#def f(s):
#    if len(s)<5:
#        print("короткая")
#    elif len(s)<=10:
#        print("средняя")
#    else:
#        print('длинная')

#f(input())

#       2

#def f(x):
#    if len(x) == 0:
#        print('строка пуста')
#    else:
#        print( x[0], x[-1] )

#f(input())

#       3

def palendrome(s):
    s= s.replace(" ","").lower
    return s==s[::-1]
s=input()
if palendrome(s):
    print("yes")
else:
    print("no")