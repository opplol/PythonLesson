class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print(self.__class__, 'run')

class ToyotaCar(Car):
    def run(self):
        print('run fast')

class Teslacar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('run super fast')

    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyotacar = ToyotaCar('Lexus')
print(toyotacar.model)
toyotacar.run()

teslacar = Teslacar('Model s')
print(teslacar.model)
teslacar.auto_run()
teslacar.run()