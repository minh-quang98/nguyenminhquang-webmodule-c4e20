import mongoengine

# mongodb://<admin>:<admin123>@ds125862.mlab.com:25862/muadongkhonglanh

host = "ds125862.mlab.com"
port = 25862
db_name = "muadongkhonglanh"
user_name = "admin"
password = "admin123"

def connect():
    mongoengine.connect(
        db_name,
        host=host,
        port=port,
        username=user_name,
        password=password
    )