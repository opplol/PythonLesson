class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print(self.__class__, 'run')

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
            self._enable_auto_run = is_enable
        else:
            raise ValueError
        
    def run(self):
        print('run super fast')

    def auto_run(self):
        print('auto run')

tesla_car = Teslacar('Model S')
# __enable_auto_run が再定義されてしまう
tesla_car.__enable_auto_run = 'XXXXXXXXX'
print(tesla_car.__enable_auto_run)

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)
