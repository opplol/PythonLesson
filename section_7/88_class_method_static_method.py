class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.x)
print(a.kind)
print(a.what_is_your_kind())
b = Person
# print(b.x)
print(b.kind)
print(b.what_is_your_kind())

print(Person.what_is_your_kind())
print(Person.kind)

Person.about(200)