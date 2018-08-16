# 20_タプル型

# >>> t = (1, 2, 3, 4, 1, 2)
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> type(t)
# <class 'tuple'>
# >>> t[0] = 100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> t[0]
# 1
# >>> t[-1]
# 2
# >>> t[2:5]
# (3, 4, 1)
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> t.index(1)
# 0
# >>> t.index(1, 1)
# 4
# >>> t.count(1)
# 2
# >>> help(list)
#
# >>> help(taple)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'taple' is not defined
# >>> help(tuple)
#
# >>> t = ([1, 2, 3], [4, 5, 6])
# >>> t
# ([1, 2, 3], [4, 5, 6])
# >>> t[0]
# [1, 2, 3]
# >>> t[0] = [1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> t[0][0]
# 1
# >>> t[0][0] = 100
# >>> t
# ([100, 2, 3], [4, 5, 6])
# >>> t = 1, 2, 3
# >>> type(t)
# <class 'tuple'>
# >>> t
# (1, 2, 3)
# >>> t = 1,
# >>> type(t)
# <class 'tuple'>
# >>> t
# (1,)
# >>> t = 1
# >>> type(t)
# <class 'int'>
# >>> t = ()
# >>> type(t)
# <class 'tuple'>
# >>> t
# ()
# >>> t = (1)
# >>> t
# 1
# >>> type()t
#   File "<stdin>", line 1
#     type()t
#           ^
# SyntaxError: invalid syntax
# >>> type(t)
# <class 'int'>
# >>> t = ('test')
# >>> t
# 'test'
# >>> t = ('test',)
# >>> t
# ('test',)
# >>> t = 1,
# >>> t * 100
# (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# >>> t + 100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "int") to tuple
# >>> new_tutpe = (1, 2, 3) + (4, 5, 6)
# >>> new_tutpe
# (1, 2, 3, 4, 5, 6)
# >>> new_tuple = (1) + (4, 5, 6)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
# >>> new_tutpe = (1,) + (4, 5, 6)
# >>> new_tutpe
# (1, 4, 5, 6)
# >>>


# 21_タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

# 長すぎに気をつける
a, b, c, d, e, f = 'Mike', 'L', 'B', 'C', 'D', 'E'
a = 'Mike'
b = 'l'

i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)

a = 100
b = 200
print(a, b)

a, b = b, a
print(a, b)

# 22_タプルの使い所
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)



print('Bad bug')
chose_from_two = ['A', 'B', 'C']

answer = []
chose_from_two.append('A')
chose_from_two.append('C')

print(chose_from_two)
print(answer)

print('Good prevent bug')
chose_from_two = ('A', 'B', 'C')

answer = []
chose_from_two.append('A')
chose_from_two.append('C')

print(chose_from_two)
print(answer)
