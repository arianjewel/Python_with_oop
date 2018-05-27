class Vehicle:
    '''Base class for all vehicles'''

    def __init__(self,name,manufacturer,color):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color

    def drive(self):
        print('Driving',self.manufacturer,self.name)

    def turn(self,direction):
        print('Turning',self.name,'to',direction)

    def brake(self):
        print(self.name,'is stopping!')


class Car(Vehicle):
    """Car class"""
    def __init__(self,name,manufacturer,color,year):        #constructor for child/derived class
        print('creating a car')
        super().__init__(name,manufacturer,color)           #base class method call on derived class
        self.year=year
        self.wheels=4
        print('A new car has been created. Name:',self.name)
        print('It has',self.wheels,'wheels')
        print('The car was built in',self.year)

    def change_gear(self, gear_name):
        'Method for changing gear'
        print(self.name,'is changing gear to',gear_name)

    def turn(self,direction):                           #mathod overridding
        print(self.name,'is turning',direction)

class MotorCycle(Vehicle):
    """docstring for MotorCycle."""
    def __init__(self, arg,g,h,k):
        super().__init__(k,g,h)
        self.year = arg
        print('ok')


if __name__=='__main__':
    v1=Vehicle('Fusion 110 EX',"Walton","Black")
    v2=Vehicle('Softail Delux',"Harley_Davidson","Blue")
    v3=Vehicle('Mustang 5.0 GT Coupe',"Ford","Red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn('left')
    v2.turn('right')

    v1.brake()
    v2.brake()
    v3.brake()

    c=Car('Mustang 5.0 GT Coupe','Ford','Red',2017)
    c.drive()
    c.brake()
    c.change_gear('P')

    c=Car('Mustang 5.0 GT Coupe','Ford','Red',2017)
    v=Vehicle('Softail Delux',"Harley_Davidson","Blue")
    c.turn('right')
    v.turn('right')

    c=Car('Mustang 5.0 GT Coupe','Ford','Red',2017)
    print(c.name,c.year,c.wheels)

    mc=MotorCycle(k='R15',g='Bazaz',h='Red',arg=2017)
    print(mc.year,mc.manufacturer,mc.name)
