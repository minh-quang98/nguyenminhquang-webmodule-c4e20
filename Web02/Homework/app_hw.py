from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service_hw import Customer

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index_hw.html')

@app.route('/customer')
def lis_cus():
    all_cus = Customer.objects(
        gender= 1,
        contacted= False
    )
    return render_template('customer.html', all_cus=all_cus)

if __name__ == '__main__':
  app.run(debug=True)
 