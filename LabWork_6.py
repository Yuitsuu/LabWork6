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

#       4

def is_substring(s1, s2):
    return s2 in s1

s1 = input()
s2 = input()

if is_substring(s1, s2):
    print("Да")
else:
    print("Нет")

#       5

def replace_a(s):
    return s.replace("a", "@")

s = input()
print(replace_a(s))

#       6

s = input()
last_name, first_name, middle_name = s.split()

# Формируем результат: Фамилия с заглавной + первые буквы имени и отчества с заглавной

res = last_name.capitalize() + " " + first_name[0].upper() + "." + middle_name[0].upper() + "."
print(res)

#       7

s = input()
count_a = len(s) - len(s.replace("а", ""))
print(count_a)
