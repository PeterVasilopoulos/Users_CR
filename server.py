from flask import Flask, render_template, redirect, request

from mysqlconnection import connectToMySQL

from user_model import User

app = Flask(__name__)

@app.route('/')
def index():

    user_list = User.get_all()

    return render_template('index.html', user_list = user_list)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    User.create(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)