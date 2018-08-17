from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return "Just for fun, don't care about me :3"

@app.route('/about-me')
def about_me():
    return render_template('index_hw.html')

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code = 302)

if __name__ == '__main__':
  app.run(debug=True)