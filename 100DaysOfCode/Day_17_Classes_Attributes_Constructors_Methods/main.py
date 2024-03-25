# Day 17- Classes. Attributes. Constructors. Methods.

"""
If we want to create more attributes related to objects from the class, we will use
a constructor.
Constructor: part of the blueprint that allows us to specify what should happen when
an object is being constructed, also known as initializing an object.

class Car:
def __init__(self):
    # initialize attributes

"""


# Declaring a class
class SampleClass:
    pass  # to use it when we want this class empty momentarily


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Setting out a default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Attributes (variables associated to an object).
#   Adding an attribute

user_1 = User('001', 'Rene')
user_2 = User('002', 'Vero')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# user_1 = User()
# user_1.id = '001'
# user_1.user_name = 'rene'
# print(user_1.user_name)
#
# user_2 = User()
# user_2.id = '002'
# user_2.user_name = 'vero'
# print(user_2.user_name)


