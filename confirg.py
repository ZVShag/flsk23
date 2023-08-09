import psycopg2

# pip install psycopg2

def create():
    try:
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="postgres",
            database='book'

        )
        connection.autocommit = True
        print('ok')
        return connection
    except:
        pass
