from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b7fcf6b718e2f5900b03bda"

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

