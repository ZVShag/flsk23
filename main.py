from flask import Flask,render_template,url_for,request,redirect,make_response
from insert_book import Insert_book,Get_allbook
from user import Insert_user,Uniq,Chek
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

@app.route('/signin',methods=['POST','GET'])
def signin():
        if request.method=='POST' and Chek(request.form['login'],request.form['password']):
            response=make_response(render_template('index.html'))
            response.set_cookie('loged','True')
            return response
        else:
            return render_template('signin.html')

@app.route('/registr',methods=['POST','GET'])
def registr():
        if request.method=='POST':
            name=request.form['name']
            sname=request.form['sname']
            email = request.form['email']
            login = request.form['login']
            password1=request.form['password']
            password2 = request.form['passwordanother']
            if password1==password2 and Uniq(login,email): # логин и почта уникальны
                Insert_user(name,sname,email,login,password1)
            return redirect('/')
        else:
            return render_template('registr.html')

@app.route('/allbook')
def allbook():
    bks=Get_allbook()
    return render_template('allbook.html',bks=bks)

if __name__=='__main__':
    app.run(debug=True)

