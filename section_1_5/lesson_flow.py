# 30_コメント
print('XXXXX')
# test
"""
test
test

"""
print('XXXX')

# Aplle price
some_value = 100
# 横のコメントはよくない
some_value = 100 #apple price


# 31_1行が長くなる時
s = 'aaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbbbb'
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1
print(x)
y = (1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1)
print(y)
# 80文字以上になると改行する

# 32_if文 33_デバッガーを使って確認してみる
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('100000')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


# 34_論理演算子
a = 1
b = 1

print(a == b)

print(a != b)

print(a < b)

print(a > b)
b = 2
print(a <= b)
a = 2
b = 2
print(a >= b)

if a > 0 and b > 0:
    print('a and b are positive')

if a > 0:
    if b > 0:
        print('a and b are positive')

a = 1
b = -1
if a > 0 or b > 0:
    print('a or b are positive')


if a > 0:
    print('a or b are positive')
elif b > 0:
    print('a or b are positive')


# 35_In と Notの使い所
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2
# 進められていない
if not a == b:
    print('Not equal')

if a != b:
    print('Not equal')



is_ok = True

if not is_ok:
    print('hello')


# 36_値が入っていない判定をするテクニック
# is_ok = True
# is_ok = 1
# is_ok = 0
# is_ok = 10020
# is_ok = ''
# is_ok = 'adfafdsafdsafd'
# is_ok = []
# False, 0, 0.0 '', [], (), {}, set()
is_ok = [1, 2, 3, 4]
if is_ok:
    print('OK!')
else:
    print('No!')


# 37_Noneを判定する場合
is_empty = None
print(is_empty)
print(help(is_empty))

# 進められていない
if is_empty == None:
    print('None!!')

if is_empty is None:
    print('is None!!')

if is_empty is not None:
    print('is None!!')

print(1 == True)
print(1 is True)
print(True is True)
print(None is None)


# 38_while文とcontinue文とbreak文
# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

count = 0

while True:
    if count >= 5:
        break
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

# 39_while else文
print('39_while else文')
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')


print('while break')
count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

# 40_input関数
print('40_input関数')

# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')
#
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# 41_for文とbreak文とcontinue文
print('41_for文とbreak文とcontinue文')

some_list = [1, 2, 3, 4, 5]

print('print by while')
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

print('print by for')
for i in some_list:
    print(i)
print()
for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    print(word)
print('break in for')
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)

print('continue in for')
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
       continue
    print(word)

# 42_for_else文
print('42_for_else文')

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all!')

print('break at banana')
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')
