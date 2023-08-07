from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from book import Book

import psycopg2
app = Flask(__name__)





@app.route('/')
def index():
        return render_template('index.html')

@app.route('/enter')
def first():
    return render_template('enter.html')

@app.route('/add',methods=['POST','GET'])
def Add_Book():
    pass


if __name__=='__main__':
    app.run(debug=True)