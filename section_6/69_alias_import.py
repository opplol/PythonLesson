# from section_6.lesson_package.talk import human
# from section_6.lesson_package.talk import animal
from section_6.lesson_package.talk import *

print(animal.sing())
print(animal.cry())

# __init__ にhumanを追加する必要がある。
print(human.sing())
print(human.cry())
