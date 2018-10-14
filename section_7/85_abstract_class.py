import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('OK')

baby = Baby()
# baby.drive()
adult = Adult()
# TypeError: Can't instantiate abstract class Adult with abstract methods drive
adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print(self.__class__, 'run')

    def ride(self, person):
        person.drive()

class ToyotaCar(Car):
    def run(self):
        print('run fast')


class Teslacar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, passwd='123'):
        # self.model = model
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('run super fast')

    def auto_run(self):
        print('auto run')
