import psycopg2



def Insert_book(name,author,zhanr,count,price):
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
            connection.commit()