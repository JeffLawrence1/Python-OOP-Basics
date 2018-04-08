# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

#  Price

#  Item Name

#  Weight

#  Brand

#  Cost

#  Status: default "for sale"
# Methods:

#  Sell: changes status to "sold"

#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

#  Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.

#  Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):

    def __init__(self, price, item, weight, brand, cost, status= "for sale"):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sold(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.tax = tax
        self.price = self.price + (self.price * self.tax)
        return self

    def ret(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        if self.reason == "nib":
            self.status = "for sale"
        if self.reason == "used":
            self.status = "used"
            self.price = self.price - (self.price * .2)
        return self

    def displayInfo(self):
        print "Price: {}, Item: {}, Weight: {}, Brand: {}, Cost: {}, Status: {}".format(self.price, self.item, self.weight, self.brand, self.cost, self.status)
        return self

item1 = Product(2.99, "Elysian IPA", "22 oz", "Elysian", 1.99)
item1.addTax(.1).displayInfo()

item2 = Product(1.99, "Doritos, Nacho Cheese", "16 oz", "Doritos", .99)
item2.ret("used").displayInfo()

item3 = Product(9.99, "Pepperoni pizz", "2 lbs", "Dominoes", 5.99)
item3.sold().displayInfo()

item1.addTax(.15).sold().displayInfo()
