from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()