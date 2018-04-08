class User(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Db(object):
    def __init__(self):
        self.contents = []
        self.next_id = 1

    def create(self, name):
        newUser = User(name, self.next_id)
        self.next_id += 1
        self.contents.append(newUser)

    def all(self):
        return self.contents

    def get(self, id):
        for user in self.contents:
            if user.id == id:
                return user

    def filter(self, name):
        temp = []
        for user in self.contents:
            if user.name == name:
                temp.append(User)
        return temp

    def exclude(self, name):
        temp = []
        for user in self.contents:
            if user.name != name:
                temp.append(User)
        return temp

UserDb = Db()
UserDb.create("Ray")
UserDb.create("Bill")
UserDb.create("Ray")
UserDb.create("Bill")
users = UserDb.all()
# UserDb.filter("Ray")
print UserDb.contents
print users