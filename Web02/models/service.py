from mongoengine import *

# Design database
class Service(Document):  # chữ cái đầu của tên class luôn viết hoa
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()