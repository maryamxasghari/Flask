from flask import Flask

app = Flask(__name__)

@app.route('/') #Running on http://127.0.0.1:5000/
def index():
    return "<h1>My first web application!</h1>"

@app.route('/information') #Running on http://127.0.0.1:5000/information
def info():
    return "<h1>informtion!</h1>"


@app.route('/profile/<name>')
def other_page(name):
    return "<h1>This is a page for {} !</h1>".format(name.upper())


if __name__ == '__main__':
    app.run()
