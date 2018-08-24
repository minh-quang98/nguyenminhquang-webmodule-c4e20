from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
word_list = ['ngoan hiền','hiếu thảo','dễ thương','cá tính','dũng cảm', 'chăm chỉ']
for i in range(50):
    print("Saving service", i + 1, "...")
    new_service = Service(
        name= fake.name(),
        yob= randint(1990,2000),
        gender= randint(0,1),
        measurements= [randint(50,100), randint(60, 90), randint(50,100)],
        height= randint(150,190),
        phone= fake.phone_number(),
        address= fake.address(),
        description= fake.words(nb=3, ext_word_list= word_list),
        status= choice([True, False])
    )

    new_service.save()

