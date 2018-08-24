from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b781f1d718e2f3624f8b751"

# kieuanh = Service.objects(id= id_to_find) ##=> []
# kieuanh = Service.objects.get(id= id_to_find) ## => service objects
service = Service.objects.with_id(id_to_find) ## => service objects

if service is not None:
    # service.delete()
    # print("Deleted")
    print(service.to_mongo())
    service.update(set__yob=2005, set__name="Linh kute")
    service.reload()
    print(service.to_mongo())

else:
    print("Not found")