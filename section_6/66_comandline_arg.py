import sys

print(sys.argv)

for i in sys.argv:
    print(i)

"""
python 66_comandline_arg.py option1 option2 3
['66_comandline_arg.py', 'option1', 'option2', '3']
66_comandline_arg.py
option1
option2
3
"""