# 56_デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func : ', func.__name__)
        print('args : ', *args)
        print('kwargs : ', **kwargs)
        result = func(*args, **kwargs)
        print('result : ', result)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info
@print_more
def add_num_info_more(a, b):
    return a + b

r = add_num_info_more(20, 30)
print(r)
@print_info
def sub_num(a, b):
    return a - b

s = sub_num(20, 10)
print(s)


print('start')
r = add_num(10, 20)
print('end')
print(r)

f = print_info(add_num)
r = f(10, 20)
print(r)

# 57_ラムダ
print('57 ラムダ')
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

sample_func_lambda = lambda word: word.capitalize()


change_words(l, sample_func)
change_words(l, sample_func_lambda)
change_words(l, lambda word: word.capitalize())

# 58_ジェネレータ
print('58_ジェネレータ')

l = ['Good morning', 'Good affernoon', 'Good night']

for i in l:
    print(i)


print('####################')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

print('####################')
g = greeting()
print(next(g))
print('1111111111')
print(next(g))
print('2222222222')
print(next(g))

def counter(num = 10):
    for _ in range(num):
        yield 'run'

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))



print(next(g))
print(next(g))
