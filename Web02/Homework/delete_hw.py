from mongoengine import *
from models.service import Service

dele = Service.objects.first()
dele.delete()