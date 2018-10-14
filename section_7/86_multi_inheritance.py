class Person(object):
    def talk(self):
        print('talk')

    def take(self):
        print('person_take')

class Car(object):
    def run(self):
        print('run')

    def take(self):
        print('Car take')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
person_car_robot.take()
