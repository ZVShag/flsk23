import psycopg2
host="127.0.0.1"
name="postgres"
password="postgres"
db_name='book'
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
    except:
        pass
