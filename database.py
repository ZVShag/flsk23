from confirg import create

def Insert_books(name,author,about,count,price):
    try:

        with create().cursor() as cursor:
                    cursor.execute(
                    """Insert into books(name,author,about,count,price) 
                    Values (name,author,about,count,price);""")
                    create().commit()
        cursor.close()
        print(name)
    except Exception as exp:
            print('Error')
    finally:
        create().close()