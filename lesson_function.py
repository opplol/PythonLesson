# 47_関数定義
print('47_関数定義')
#say_something()

def say_something():
    print('hi')

say_something()
print(type(say_something))

f = say_something
f()

def say_something2():
    s = 'hi2'
    return s

result = say_something2()
print(result)


def what_is_this(color):
    print(color)

what_is_this('red')


def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this2('red')
print(result)
result = what_is_this2('green')
print(result)
result = what_is_this2('black')
print(result)

# 48_関数の引数と返り値の宣言
print('48_関数の引数と返り値の宣言')
num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
r2 = add_num('a', 'b')
print(r)
print(r2)

# 49_位置引数とキーワード引数とデフォルト引数
print('49_位置引数とキーワード引数とデフォルト引数')

def menu(entree, drink, desert):
    print('entree :', entree)
    print('drink :', drink)
    print('desert :', desert)

menu('beef', 'beer', 'ice')
menu('beef', 'ice', 'beer')
menu(entree='beef', desert='ice', drink='beer')
menu('beef', desert='ice', drink='beer')
# menu(desert='ice', 'beef', drink='beer')


def menu2(entree='beef', drink='wine', desert='ice'):
    print('menu2######')
    print('entree :', entree)
    print('drink :', drink)
    print('desert :', desert)

menu2()
menu2(entree='chicken')
menu2(entree='chicken', drink='beer')
menu2('chicken', drink='beer')

# 50_デフォルト引数で気をつけること
print('50_デフォルト引数で気をつけること')

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)


z = test_func(100)
print(z)

# デフォルト引数にはリスト、辞書を指定しない方がいい（参照型）
z = test_func(100)
print(z)


def test_func_better(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l

z = test_func_better(100)
print(z)
z = test_func_better(100)
print(z)
