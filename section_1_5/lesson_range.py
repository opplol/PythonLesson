# 43_range関数
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

for i in range(0, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(10):
    print(i, 'hello')

for _ in range(10):
    print('hello')

# 44_enumerate関数
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)

i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# 45_zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# 46_辞書をfor文で処理する
d = {'x': 100, 'y': 200}

for v in d:
    print(v)

for k, v in d.items():
    print(k, ':', v)

print(d.items())
