from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight, height):
    bmi  = int(weight) / ((int(height) / 100) ** 2)
    return render_template("ex1_hw.html", bmi=bmi)   
if __name__ == '__main__':
  app.run(debug=True)