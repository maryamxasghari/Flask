from flask import Flask

app = Flask(__name__)

@app.route('/') #Running on http://127.0.0.1:5000/
def index():
    return "<h1>My first web application!</h1>"

@app.route('/profile/<name>')
def other_page(name):
    if name[-1].lower() != "y":
        nw_name =name[:-1]+"y"
        return "<h1>New name {} !</h1>".format(nw_name)
    else:
        nw_name =name[:-1]+"iful"
        return "<h1>New name {} !</h1>".format(nw_name)

if __name__ == '__main__':
    app.run()
