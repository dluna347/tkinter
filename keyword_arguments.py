# *args - unlimited positional arguments

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

to_print = add(3, 5, 7, 9, 11, 13, 15)

#----------------------------------------------------------


# **kwargs - unlimited key word arguments

def calculate(n, **kwargs):
    n += kwargs["add"]
    n*= kwargs["multiply"]
    return n

#------------------------------------------------------------
# creating a class with **kwargs

class Car():
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

# or

class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        # the benefit of using this method is that it wont crash
        # if make and model are not provided when the class is called. 
        # instead it'll just return none.  This is how a class is created 
        # with alot of "optional" key word arguments.

my_car = Car(make="Tesla")

print(my_car.make)