from flask import Flask,render_template,url_for,request,redirect,make_response,flash,session
from insert_book import Insert_book,Get_allbook,Getbook
from user import Insert_user,Uniq,Chek
app = Flask(__name__)
app.config['SECRET_KEY']='cnkjasnckjsacnkjsa6t75326674gfbgf'

@app.errorhandler(404)
def notfound(error):
    return render_template('404.html'),404


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
            if Insert_book(name,author,zhanr,count,price):
                flash('Запись успешно добавлена')
            else:
                flash('При вводе данных произошла ошибка, попробуйте снова')
            return render_template('add.html')
        else:
            return render_template('add.html')

@app.route('/signin',methods=['POST','GET'])
def signin():
    if 'login' in session:
        return redirect(url_for('profile',username=session['login']))
    elif request.method=='POST':
        login=request.form['login']
        password=request.form['password']
        if Chek(login,password):
            session['login']=login
            return redirect(url_for('profile', username=session['login']))



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

@app.route('/allbook/<int:id>')
def getbook(id):
    bk=Getbook(id)
    return render_template('abook.html',bk=bk)

if __name__=='__main__':
    app.run(debug=True)

