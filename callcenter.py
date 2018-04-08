# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.

# Call Class
#  Create your call class with an init method. Each instance of Call() should have:
# Attributes:

#  unique id

#  caller name

#  caller phone number

#  time of call

#  reason for call
# Methods:

#  display: that prints all Call attributes.
# CallCenter Class
#  Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
# Attributes:

#  calls: should be a list of call objects

#  queue size: should be the length of the call list
# Methods:

#  add: adds a new call to the end of the call list

#  remove: removes the call from the beginning of the list (index 0).

#  info: prints the name and phone number for each call in the queue as well as the length of the queue.
# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.

# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.

class Call(object):
    numofcalls = 0
    def __init__(self, name, phone_number, time, reason):
        self.id = Call.numofcalls
        self.name = name
        self.phone_number =  phone_number
        self.time = time
        self.reason = reason
        Call.numofcalls += 1

    def display(self):
        print "ID: {}, Name: {}, Phone Number: {}, Time: {}, Reason: {}".format(self.id, self.name, self.phone_number, self.time, self.reason)
        return self

class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.qsize = len(self.calls)

    def addCall(self, acall):

        self.calls.append(acall)
        return self

    def removeCall(self, rcall):
        
        self.calls.remove(rcall)
        return self

    def info(self):
        for call in self.calls:
            call.display()
     
call1 = Call("fred", "312-123-1323", "6:15", "complaint")
# call1.display()
call2 = Call("frank", "323-123-1313", "7:30", "compliment")
call3 = Call("terry", "442-123-4133", "5:23", "complaint")
call4 = Call("cindy", "333-413-4884", "6:45", "compliment")
call5 = Call("frank", "323-123-1313", "7:30", "compliment")
call6 = Call("terry", "442-123-4133", "5:23", "complaint")
call7 = Call("cindy", "333-413-4884", "6:45", "compliment")
CallCenter().addCall(call1).addCall(call2).addCall(call3).addCall(call4).addCall(call5).addCall(call6).addCall(call7).info()
print "divider to test remove"
CallCenter().addCall(call1).addCall(call6).addCall(call7).removeCall(call1).info()
