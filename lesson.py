# 8_変数宣言
num = 1
name = 'Mike'
is_ok = True

print(num)
print(name)
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

name_1 = '1'
num_1 = int(name_1)
print(num_1, type(num_1))
print('')
# 9_printで出力
print('HI')
print('HI', 'MIKE')
print('')
print('HI', 'MIKE', sep=',', end='\n')
print('HI', 'MIKE', sep=',', end='\n')
print('')
print('HI', 'MIKE', sep=',', end='')
print('HI', 'MIKE', sep=',', end='')
print('')
print('HI', 'MIKE', sep=',', end='.\n')
print('HI', 'MIKE', sep=',', end='.\n')

# 10_数値
'''
2 + 2
Out[2]: 4
5 -2
Out[3]: 3
5 * 6
Out[4]: 30
50 - 5 * 6
Out[5]: 20
(50 - 5) * 6
Out[6]: 270
8 / 5
Out[7]: 1.6
type(1)
Out[8]: int
type(1.6)
Out[9]: float
0.6
Out[10]: 0.6
.6
Out[11]: 0.6
17 / 3
Out[12]: 5.666666666666667
17 // 3
Out[13]: 5
17 % 3
Out[14]: 2
5 * 5
Out[15]: 25
5 ** 2
Out[16]: 25
5 * 5 * 5 * 5 * 5
Out[17]: 3125
5 ** 5
Out[18]: 3125
x = 5
x
Out[20]: 5
y = 10
x * y
Out[22]: 50
a
Traceback (most recent call last):
  File "/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2963, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-23-3f786850e387>", line 1, in <module>
    a
NameError: name 'a' is not defined
pie = 3.141515151515
pie
Out[25]: 3.141515151515
round(pie, 2)
Out[26]: 3.14
'''
import  math

result = math.sqrt(25)
print(result)

log_val = math.log2(10)
print(log_val)

print(help(math))