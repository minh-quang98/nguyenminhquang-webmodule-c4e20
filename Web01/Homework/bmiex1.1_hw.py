from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight, height):
    bmi = int(weight) / ((int(height) / 100) ** 2)
    if bmi < 16:
        noti = "You are severely underweight"
    elif bmi < 18.5:
        noti = "You are underweight"
    elif bmi < 25:
        noti = "You are normal"
    elif bmi < 30:
        noti = "You are overweight"
    else:
        noti = "You are obese"
    return noti

if __name__ == '__main__':
  app.run(debug=True)