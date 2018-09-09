# 51_function_arg for tuple

def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)

say_something('hi!', 'Mike', 'Nance')

def say_something2(*args):
    print(args)
    for arg in args:
        print(arg)

say_something2('hi!', 'Mike', 'Nance')


def say_something3(word, *args):
    print('word : ', word)
    for arg in args:
        print(arg)

say_something3('hi!', 'Mike', 'Nance')


t = ('Mike', 'Nancy')
say_something3('Hi!', *t)


#52_function arg for dictionary
def menu(entree='beef', dring='wine'):
    print(entree, dring)

menu(entree='beef', dring='coffee')

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, ' : ', v)


menu(entree='beef', dring='coffee')

d = {
    'entree' : 'beef',
    'drink' : 'ice coffee',
    'dessert' : 'ice'
}
menu(**d)


def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'apple', 'orange', entree='beef', dring='coffee')

# 53_doc string
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
          bool: The return value. True for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
help(example_func)

# 54_inner function
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)

def outer2(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer2(3, 4)


# 55 Closure
def outer(a, b):

    def inner():
        return a + b

    return inner

print(outer(1, 2))

f = outer(1, 2)
r = f()
print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

