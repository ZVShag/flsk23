import psycopg2
from werkzeug.security import generate_password_hash,check_password_hash

class user:
    def __init__(self,login,password):
        self.login=login
        self.password=generate_password_hash(password)
    def Check(self):
        return check_password_hash(self.password)

def Insert_user(name,sname,email,login,password):
    connection=psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='postgres',
        database='book'
    )
    with connection.cursor() as cursor:
        request = "Insert into users(name,sname,email,login,password) Values(%s,%s,%s,%s,%s)"
        record = [name, sname,email,login,password]
        cursor.execute(request, record)
        connection.commit()

def Uniq(login,email):
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='postgres',
        database='book'
    )
    with connection.cursor() as cursor:
        request='Select * from users where login=%s OR email=%s;'
        record=[login,email]
        cursor.execute(request,record)
        return not(type(cursor.fetchone())=='NoneType')

def Chek(login,password):
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='postgres',
        database='book'
    )

    with connection.cursor() as cursor:
        request='Select password from users where login=%s and password=%s;'
        record=[login,password]
        cursor.execute(request,record)
        return not(type(cursor.fetchone())=='NoneType')