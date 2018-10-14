import builtins

print('print')
builtins.print('builtin_func_print')

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print(sorted(ranking))

print(ranking.get('A'))
print(sorted(ranking, key=ranking.get))

print(sorted(ranking, key=ranking.get, reverse=True))


