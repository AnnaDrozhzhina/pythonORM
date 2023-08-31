import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship



Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'Publisher {self.id}:{self.name}'

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Book {self.id}:{self.title}'

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'Shop {self.id}:{self.name}'

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'Stock {self.id}:({self.id_book}, {self.id_shop}, {self.count})'

class Sale(Base):
     __tablename__ = "sale"

     id = sq.Column(sq.Integer, primary_key=True)
     price = sq.Column(sq.Integer, nullable=False)
     data_sale = sq.Column(sq.Date, nullable=False)
     id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
     count = sq.Column(sq.Integer, nullable=False)
     stock = relationship(Stock, backref="sales")

     def __str__(self):
         return f'Sale {self.id}:({self.price}, {self.data_sale}, {self.count}, {self.id_stock})'

def create_tables(engine):
    Base.metadata.create_all(engine)

DSN = 'postgresql://postgres:Postgres@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
