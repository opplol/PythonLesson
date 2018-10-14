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
        self._enable_auto_run = enable_auto_run
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

class TeslacarDouble(Car):
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
        print(self.__enable_auto_run)
        print('run super fast')

    def auto_run(self):
        print('auto run')

teslacar_pass = Teslacar('Model S', passwd='456')
teslacar_pass.enable_auto_run = True
print(teslacar_pass.enable_auto_run)



teslacar = Teslacar('Model s')
# teslacar.enable_auto_run = True
# AttributeError: can't set attribute

# teslacar.enable_auto_run = True
# print(teslacar.enable_auto_run)

teslacar_double = TeslacarDouble('Model S', passwd='456')
teslacar_double.run()
print(teslacar_double.enable_auto_run)
