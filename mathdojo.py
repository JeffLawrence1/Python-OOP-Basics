# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:

# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

# PART III
# Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.

class MathDojo(object):

    def __init__(self):
        self.results = 0

    def add(self, *args):
        for x in args:
            if type(x) == list or type(x) == tuple:
                for y in x:
                    self.results += y
            else:
                self.results += x
        return self

    def subtract(self, *args):
        for x in args:
            if type(x) == list or type(x) == tuple:
                for y in x:
                    self.results -= y
            else:
                self.results -= x
        return self

    def result(self):
        print self.results
        return self

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
md.add([1], 3,4).add([3,5,7,8], (4, 4, 2, 6), [2,4.3,1.25]).subtract(2, [2,3], (6, 2, 4.2), [1.1,2.3]).result()