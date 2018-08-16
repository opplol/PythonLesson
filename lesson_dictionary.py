# # 23_辞書型
# >>> d = {'x': 10, 'y': 20}
# >>> d
# {'x': 10, 'y': 20}
# >>> type(d)
# <class 'dict'>
# >>> d['x']
# 10
# >>> d['y']
# 20
# >>> d['x'] = 100
# >>> d
# {'x': 100, 'y': 20}
# >>> d['x'] = 'XXXX'
# >>> d
# {'x': 'XXXX', 'y': 20}
# >>> d['z'] = 200
# >>> d
# {'x': 'XXXX', 'y': 20, 'z': 200}
# >>> d[1] = 10000
# >>> d
# {'x': 'XXXX', 'y': 20, 'z': 200, 1: 10000}
# >>> dict(a = 10, b = 20)
# {'a': 10, 'b': 20}
# >>> dict([('a', 10), ('b', 20) ])
# {'a': 10, 'b': 20}
#
# # 24_辞書型のメソッド
# >>> d = {'x': 10, 'y': 20}
# >>> help(d)
#
# >>> d.keys()
# dict_keys(['x', 'y'])
# >>> d.values()
# dict_values([10, 20])
# >>> d2 = {'x': 1000, 'j': 500}
# >>> d
# {'x': 10, 'y': 20}
# >>> d2
# {'x': 1000, 'j': 500}
# >>> d.update(d2)
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d['x']
# 1000
# >>> d.get('x')
# 1000
# >>> d['z']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'z'
# >>> d.get('z')
# >>> r = d.get('z')
# >>> r
# >>> type(r)
# <class 'NoneType'>
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d.get('x')
# 1000
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d.pop('x')
# 1000
# >>> d
# {'y': 20, 'j': 500}
# >>> del d['y']
# >>> d
# {'j': 500}
# >>> del d
# >>> d
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'd' is not defined
# >>> d = {'a': 100, 'b': 200}
# >>> d
# {'a': 100, 'b': 200}
# >>> d.clear
# <built-in method clear of dict object at 0x103c8fee8>
# >>> d.clear()
# >>> d
# {}
# >>> d = {'a': 100, 'b': 200}
# >>> d
# {'a': 100, 'b': 200}
# >>> 'a' in d
# True
# >>> 'j' in d
# False

# 25_辞書型のコピー
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 100
print(x)
print(y)


# 26_辞書型の使い所
# キーをわかっていれば値を取り出すスピードがリストより早い
print('26_辞書型の使い所')
l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300]
]

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])