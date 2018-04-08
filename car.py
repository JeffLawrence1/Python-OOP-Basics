# Assignment: Car
# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# A sample output would be like this:

# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12
# Copy
# Price: 2000
# Speed: 5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12
# Copy
# Price: 2000
# Speed: 15mph
# Fuel: Kind of Full
# Mileage: 95mpg
# Tax: 0.12
# Copy
# Price: 2000
# Speed: 25mph
# Fuel: Full
# Mileage: 25mpg
# Tax: 0.12
# Copy
# Price: 2000
# Speed: 45mph
# Fuel: Empty
# Mileage: 25mpg
# Tax: 0.12
# Copy
# Price: 20000000
# Speed: 35mph
# Fuel: Empty
# Mileage: 15mpg
# Tax: 0.15

class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

        self.display_all()

    def display_all(self):
        print "price is {}, top speed is {}, fuel tank is {}, mileage is {}, and the tax rate is {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(15000, 78, "half", 43222)
car2 = Car(24000, 82, "empty", 23000)
car3 = Car(32000, 68, "one third", 32111)
car4 = Car(5000, 58, "half", 83222)
car5 = Car(4000, 62, "empty", 123000)
car6 = Car(52000, 108, "full", 111)
    