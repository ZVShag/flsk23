import psycopg2

def Insert_book(name,author,zhanr,count,price):
        try:
            connection = psycopg2.connect(
                host='127.0.0.1',
                user="postgres",
                password="postgres",
                database='book'
            )
            with connection.cursor() as cursor:
                request="Insert into books(name,author,zhanr,count,price) Values(%s,%s,%s,%s,%s)"
                record=[name,author,zhanr,count,price]
                cursor.execute(request,record)
            return True
        except:
            return False



def Get_allbook():
    connection = psycopg2.connect(
        host='127.0.0.1',
        user="postgres",
        password="postgres",
        database='book'
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'Select * from books;'
        )
        return cursor.fetchall()
        connection.commit()

def Getbook(id):
    connection = psycopg2.connect(
        host='127.0.0.1',
        user="postgres",
        password="postgres",
        database='book'
    )

    with connection.cursor() as cursor:
        cursor.execute(
            f'Select * from books where id={id};'
        )
        return cursor.fetchone()
        connection.commit()
