# Optional Assignment: Store
# Now, let's build a store to contain our products by making a store class and putting our products into an array.

# Store class:
# Attributes:

#  products: an array of products objects

#  location: store address

#  owner: store owner's name
# Methods:

#  add_product: add a product to the store's product list

#  remove_product: should remove a product according to the product name

#  inventory: print relevant information about each product in the store
# You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.

class Store(object):

    def __init__(self, location, owner, product = []):
        self.product = product
        self.location = location
        self.owner = owner

    def addProduct(self, prod):
        self.prod = prod
        self.product.append(self.prod)
        return self

    def removeProduct(self, prod):
        self.prod = prod
        self.product.remove(self.prod)
        return self

    def inventory(self):
        print self.product
        return self

store1 = Store("Bellevue", "Jeff")
store1.addProduct("pizza").addProduct("beer").addProduct("smokes").addProduct("fun").inventory()
store1.removeProduct("fun").inventory()
