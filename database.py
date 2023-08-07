from main import connection

def Insert_books(name,author,about,count,price):
    try:

            with connection.cursor() as cursor:
                cursor.execute(
                    """Insert into books(name,author,about,count,price) 
                    Values (name,author,about,count,price);""")

    except Exception as exp:
            print('Error')
    finally:
        connection.close()