"""
Test Test ###############
"""
# 59_リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []

for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = [i for i in t]
k = [i for i in t if i % 2  == 0]
print(r)
print(k)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)

# 60_辞書内包表記

w = ['mon', 'tue', 'wed']
f = ['coffe', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 61_集合内包表現
s = set()
for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10)}
r = {i for i in range(10) if i % 2 == 0}
print(s)
print(r)

# 62_ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))

g = (i for i in range(10) if i % 2 == 0)
print(type(g))

for x in g:
    print(x)

# 63_名前空間とスコープ


animal = 'cat'

def f():
    # print(animal)
    global animal
    animal = 'dog'
    print('after', animal)
    print('local:', locals())

print('global: ', animal)
f()

print('global_var:', globals())

def f():
    """Test func doc"""
    print(f.__doc__)
    print(f.__name__)
f()

# 64_例外処理
l = [1, 2, 3]
i = 5
# l[i]
try:
    l[i]
except:
    print("Don't worry")
print("last")

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
print("last2")

del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
print("last3")

l = [1, 2, 3]
try:
    () + l
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
print("last4")


try:
    () + l
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
finally:
    print('clean up')

try:
   l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
finally:
    print('clean up')

# try:
#     () + l
# finally:
#     print('clean up')

try:
    # l[i]
    l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')


# 65_独自例外の作成
# raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
