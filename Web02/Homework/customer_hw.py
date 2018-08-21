import mlab_hw
from models.service_hw import Customer
from faker import Faker
from random import randint, choice

mlab_hw.connect()

fake = Faker()

for i in range(50):
    print("Saving customer", i + 1, '...')
    new_customer = Customer(
        name= fake.name(),
        gender= randint(0,1),
        phone= fake.phone_number(),
        job= fake.job(),
        company= fake.company(),
        contacted= choice([True, False])
    )
    new_customer.save()