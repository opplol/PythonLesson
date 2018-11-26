f = open('test.txt', 'w')
f.write('test')
f.close()

f = open('test.txt', 'a')
f.write('test')
f.close()

f = open('test.txt', 'w')
f.write('test\n')
print('I am print', file=f)
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()
