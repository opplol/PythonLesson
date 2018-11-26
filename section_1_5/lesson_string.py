# 11_文字列
s = 'test'
print(s)
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('Say "I don\'t know"')
print("Say \"I don\'t know\"")
print('Hello. \nHow are you')
print(r'C:\name\name')
print("""
Line1
Line2
Line3
""")
print('########################')
print("""\
Line1
Line2
Line3\
""")
print('########################')

print('Hi, ' * 3)
print('Hi, ' * 3 + 'Mike')
print('Py''thon')

a = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
b = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(a)
print(b)

prefix = 'Py'
print(prefix + 'thon')

# 12_文字列のインデックスとスライス
print()
print('12_文字列のインデックスとスライス')
word = 'Python'
print(word[0])
print(word[1])
print(word[-1])
print('#########')
print(word[0:2])
print(word[2:5])
print('#########')
print(word[0:2])
print(word[5])
print('#########')
print(word[2:])
# print(word[100])
print('#########')
word = 'j' + word[1:]
print(word)
print(word[:])
print('#########')
n = len(word)
print(n)

# 13_文字のメソッド
print('13_文字のメソッド')

s = 'My name is Lee. Hi Lee'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)
print('#########')

print(s.find('Lee'))
print(s.rfind('Lee'))
print(s.count('Lee'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Lee', 'Nancy'))


# 14_文字の代入
print('14_文字の代入')
'''
>>> 'a is {}'.format('a')
'a is a'
>>> 'a is {}'.format('test')
'a is test'
>>> 'a is {} {} {}'.format(1, 2, 3)
'a is 1 2 3'
>>> 'a is {0} {1} {2}'.format(1, 2, 3)
'a is 1 2 3'
>>> 'a is {2} {1} {0}'.format(1, 2, 3)
'a is 3 2 1'
>>> 'My name is {0} {1}'.format('SangHo', 'Lee')
'My name is SangHo Lee'
>>> 'My name is {0} {1}. Watashiwa {1} {0}'.format('SangHo', 'Lee')
'My name is SangHo Lee. Watashiwa Lee SangHo'
>>> 'My name is {first} {last}. Watashiwa {last} {first}'.format(first = 'SangHo', last = 'Lee')
'My name is SangHo Lee. Watashiwa Lee SangHo'
>>> 1
1
>>> '1'
'1'
>>> x = str(1)
>>> type(x)
<class 'str'>
>>> str(3.14)
'3.14'
>>> str(True)
'True'
>>> 
'''
