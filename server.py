from flask import Flask, render_template

from mysqlconnection import connectToMySQL

app = Flask(___name__)

@app.route('/')
def index():

    results = connectToMySQL("users").query_db("SELECT * FROM users")
    print(results)

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)