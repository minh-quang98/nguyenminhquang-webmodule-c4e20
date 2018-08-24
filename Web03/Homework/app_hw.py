from flask import *
import mlab
from mongoengine import *
from models.service import Service

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service= Service.objects(
        gender=g, 
    )
    return render_template('search.html',
                            all_service=all_service
    )

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template(
        'admin.html',
        all_service=all_service
    )

@app.route('/delete/<service_id>')
def delete(service_id):
    s = Service.objects.with_id(service_id)
    if s is not None:
        s.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(
            name= name,
            yob= yob,
            phone= phone,
            gender= gender
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/delete-all')
def delete_all():
    s = Service.objects()
    s.delete()
    return 'Deleted'

@app.route('/search/<service_id>')
def profile(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        return render_template('profile.html', service=service)
    else:
       return "Service not found" 

if __name__ == '__main__':
  app.run(debug=True)


# set default input value
# radio bottom