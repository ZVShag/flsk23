class Book:
    def __init__(self,name,author,zhanr,count,price):
        name = name
        author = author
        zhanr = zhanr
        count=count
        price=price
    def __repr__(self):
        return '<Book %r>'% self.name