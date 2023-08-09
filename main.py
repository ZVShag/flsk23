from flask import Flask,render_template,url_for,request,redirect
from insert_book import Insert_book

app = Flask(__name__)





@app.route('/')
def index():
        return render_template('index.html')

@app.route('/enter')
def first():
    return render_template('enter.html')

@app.route('/add',methods=['POST','GET'])
def add_book():
        if request.method=='POST':
            name=request.form['name']
            author=request.form['author']
            zhanr=request.form['zhanr']
            count=request.form['count']
            price=request.form['price']

            Insert_book(name,author,zhanr,count,price)
            return redirect('/')
        else:
            return render_template('add.html')




if __name__=='__main__':
    app.run(debug=True)

