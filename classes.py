class Car:
    # pass
    # DocString - Helps in documentations, gives you an idea of what is going on a class
    # Example for Dictionaries Documentation
    # print(help(dict()))

    '''
    This is a Car class
    A class doing nothing we add pass
    
    Setting properties(attributes of a class) - we use the init method
    init acts as a constructor
    Self signifies the object that you are creating
    '''

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def accelerate(self, speed):
        accel = speed + 20
        print(f'The {self.color} {self.name} accelerates at {accel} Mph')

# print(type(Car))
# Creating an instance of a class
# car1 = Car("Benz", "Gray")
# car2 = Car("Audi", "Black")
# # print(car1.name)
# car1.accelerate(120)
# car2.accelerate(140)
# print(type(car1))

print(help(Car))
