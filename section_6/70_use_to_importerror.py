# from section_6.lesson_package.talk import human
# from section_6.lesson_package.talk import animal
# from section_6.lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())
#
# print(human.sing())
# print(human.cry())

try:
    from section_6.lesson_package import utils
except ImportError:
    from section_6.lesson_package.tools import utils

utils.say_twice('world')
