# import collections, sys, os  ×
# 標準LIB
import collections
import os
import sys

# Third LIB
import termcolor

# Company LIB
import section_6.lesson_package

# Local LIB
import config

print(collections.__file__)
print(termcolor.__file__)
print(section_6.lesson_package.__file__)
print(config.__file__)

print(sys.path)