class Car:
    """"a simple test to rep a car"""
    def __init__(me,make ,model, year):
        """"Initiallize attributes to describe a car"""
        me.make = make
        me.model = model
        me.year = year
        me.odometer_reading = 0
    def get_discription_name(me):
        """return a neat name"""
        long_name = f"{me.make} {me.model} {me.year}"
        return long_name.title()
    def read_odometer(me):
        """print a cars milage"""
        print(f"This car has {me.odometer_reading} mile on it")

    def update_odometer(me,mileage):
        """set odometer to a given value
        reject change"""
        me.odometer_reading = mileage

    def update_odometer(me,mileage):
        """set odometer to a given value
        reject change"""
        
        if mileage >= me.odometer_reading:
            me.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")

    def increment_odometer(me,miles):
        """add amount to odometer"""
        me.odometer_reading += miles
class Battery:
    """"A simple attempt to model battery"""    
    def __init__(me, battery_size=1000):
        """Initialize battery attributes"""
        me.battery_size = battery_size

    def describe_battery(me):
        """print a battery description"""    
        print(f"This car has a {me.battery_size}-KWh Bttery.")

class ElectricCar(Car):
    """represent aspects of a car specific to electric cars"""

    def __init__(me, make, model, year):
        """"Initialize attributes if the parent class"""
        super().__init__(make, model, year)
        me.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_discription_name())
my_tesla.battery.describe_battery()