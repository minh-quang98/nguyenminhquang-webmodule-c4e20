import mongoengine

# mongodb://<muadongad>:<123abc>@ds125862.mlab.com:25862/muadongkhonglanh

host = "ds125862.mlab.com"
port = 25862
db_name = "muadongkhonglanh"
user_name = "muadongad"
password = "123abc"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )
