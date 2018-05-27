'''class Car:
    name=''
    color=''

    def __init__(self,name,color):         #constructor
        self.name=name
        self.color=color

    def start(self=0):
        print('Starting the engine')

Car.name='Axio'
Car.color='black'
print('Name of car is',Car.name)
print('color:',Car.color)
Car.start()
print(dir(Car))

my_car=Car()
my_car.name='Allion'
my_car2=my_car.name
print(my_car2)
my_car.start()'''





'''class Car:
    name=''
    color=''

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def start(self):
        print('Starting the engine')

my_car=Car('Corolla','white')
print(my_car.name)
print(my_car.color)
my_car.start()'''




'''class Car:
    def __init__(self,n,c):
        self.name=n
        self.color=c

    def start(self):
        print('Starting the engine')

my_car=Car('Corolla','white')
my_car.year=2017                  #add attribute with object out of class
print(my_car.name,my_car.color,my_car.year)
my_car.start()'''




'''class Car:
    def __init__(self,n,c):
        self.name=n
        self.color=c

    def start(self2):
        print('Name:',self2.name)
        print('color:',self2.color)
        print('Starting the engine')

my_car=Car('Corolla','white')
my_car.start()
my_car2=Car('Premio','black')
my_car2.start()
my_car3=Car('Allion','blue')
my_car3.start()'''




class Car:
    def __init__(self, name,manufacturer,color,year,cc):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
        self.year=year
        self.cc=cc

    def start(self):
        print('start engine')

    def brake(self):
        print('please brake')

    def drive(self):
        print('please drive')

    def turn(self):
        print('please turn')

    def change_gear(self):
        print('please change gear')

my_car=Car('Toyota','Toyota company','Black',2018,800)
print(my_car.name,my_car.manufacturer,my_car.color,my_car.year,my_car.cc)
my_car.start()
my_car.brake()
my_car.drive()
my_car.turn()
my_car.change_gear()
