from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    user_logged_in = True
    name = "Mary"
    letters = list(name)
    name_list = {'name' : name}
    my_list = [1,2,3,4,5,6,7]
    return render_template('basic_html.html',name = name,\
    letters=letters,\
    name_list=name_list,\
    my_list=my_list,\
    user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)
