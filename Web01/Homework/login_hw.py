from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Just for fun, don't care about me :3"

@app.route('/user/<username>')
def login(username):
    if username == 'quang':
        return render_template('login_hw.html')
    else:
        return "User not found"


if __name__ == '__main__':
  app.run(debug=True)