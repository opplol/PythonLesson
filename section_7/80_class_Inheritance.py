class Car(object):
   def run(self):
       print(self.__class__, 'run')

class ToyotaCar(Car):
    pass

class Teslacar(Car):
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyotacar = ToyotaCar()
toyotacar.run()

teslacar = Teslacar()
teslacar.auto_run()
teslacar.run()