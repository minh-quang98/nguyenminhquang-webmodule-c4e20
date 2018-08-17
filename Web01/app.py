from flask import Flask, render_template
app = Flask(__name__)
# luôn kiểm tra server

@app.route('/')
def index():
    posts = [
        {
            "title": "Tiêu đề bài thơ",
            "content": "Nội dung bài thơ",
            "author": "Nah",
            "sex": 1
        },
        {
            "title": "Thơ con cóc",
            "content": "Hahahaa",
            "author": "Neh",
            "sex": 0
        }
    ]
    

    return render_template('index.html', posts=posts)

@app.route('/hello')
def say_hello():
    return "<h1>Nah! Don't care about me</h1>"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {}, your're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x,y):
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)  # auto sửa lỗi

# nếu lệnh lỗi mà lưu thì server auto tắt