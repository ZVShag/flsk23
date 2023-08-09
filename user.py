import psycopg2

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
print(Uniq('fdtopo','fedya@proton.com'))