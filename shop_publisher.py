import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:Postgres@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
s = Session()

#создание объектов
pb1 = Publisher(name="Alisa")
pb2 = Publisher(name="Bookov")
pb3 = Publisher(name="Barto")
pb4 = Publisher(name="Dikkens")

s.add_all([pb1, pb2, pb3, pb4])
s.commit()

b1 = Book(title="Vesna", id_publisher=1)
b2 = Book(title="Ot_A _do _Ya", id_publisher=2)
b3 = Book(title="Idet_bichok", id_publisher=3)
b4 = Book(title="Christmas_carol", id_publisher=4)
b5 = Book(title="Mne_teper_ne_do_igrushek", id_publisher=3)
b6 = Book(title="Akula", id_publisher=1)

s.add_all([b1, b2, b3, b4, b5, b6])
s.commit()
print(b1, b2)

sh1 = Shop(name="Bukinistika")
sh2 = Shop(name="Kniga")

s.add_all([sh1, sh2])
s.commit()
print(sh1, sh2)

st1 = Stock(count=15, id_book=1, id_shop=1)
st2 = Stock(count=50, id_book=2, id_shop=2)
st3 = Stock(count=15, id_book=6, id_shop=1)
st4 = Stock(count=7, id_book=3, id_shop=2)
st5 = Stock(count=15, id_book=4, id_shop=1)
st6 = Stock(count=5, id_book=5, id_shop=2)
st7 = Stock(count=11, id_book=5, id_shop=1)
s.add_all([st1, st2, st3, st4, st5, st6, st7])
s.commit()
print(st4, st5, st6)

sale1 = Sale(price=99, data_sale=datetime(2022,6,28), count=10, id_stock=1)
sale2 = Sale(price=199, data_sale=datetime(2022,10,2), count=35, id_stock=2)
sale3 = Sale(price=350, data_sale=datetime(2023,4,4), count=5, id_stock=3)
sale4 = Sale(price=350, data_sale=datetime(2023,6,16), count=5, id_stock=4)
sale5 = Sale(price=900, data_sale=datetime(2023,7,14), count=10, id_stock=5)
sale6 = Sale(price=400, data_sale=datetime(2023,5,4), count=5, id_stock=6)

s.add_all([sale1, sale2, sale3, sale4, sale5, sale6])
s.commit()
print(sale1, sale2, sale3)

def getshops(publisher_name_id):
    request = s.query(Book.title, Shop.name, Sale.price, Sale.data_sale).select_from(Shop).\
                join(Stock).\
                join(Book).\
                join(Publisher).\
                join(Sale)
    if publisher_name_id.isdigit():
        i = request.filter(Publisher.id == publisher_name_id).all()
    else:
        i = request.filter(Publisher.name == publisher_name_id).all()
    for book_title, shop_name, price, data_sale in i:
        print(f"{book_title: <40} | {shop_name: <10} | {price: <8} | {data_sale.strftime('%d-%m-%Y')}")

if __name__ == "__main__":
    publ = input("Введите имя или id публициста: ")
    getshops(publisher_name_id = publ)





