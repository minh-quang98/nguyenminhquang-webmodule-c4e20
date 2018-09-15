from mongoengine import *

class Signin(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = StringField()