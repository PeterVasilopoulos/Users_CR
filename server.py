from flask import Flask, render_template

from mysqlconnection import connectToMySQL

from user_model import User

app = Flask(__name__)

@app.route('/')
def index():

    results = connectToMySQL("users").query_db("SELECT * FROM users")
    print(results)

    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug = True)