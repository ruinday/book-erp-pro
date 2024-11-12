from datetime import datetime

from sqlalchemy import Integer,String,Float,Date,DateTime
from sqlalchemy.orm import MappedColumn

from .exts import db

class Books(db.Model):
    __tablename__ = 'books'
    id = MappedColumn(Integer,primary_key=True,autoincrement=True)
    name = MappedColumn(String(255),nullable=False)
    author = MappedColumn(String(55),nullable=False)
    price = MappedColumn(Float)
    publish_date = MappedColumn(Date)
    publisher = MappedColumn(String(255))
    create_date = MappedColumn(DateTime,default=datetime.now)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'author':self.author,
            'price':self.price,
            'publish_date':self.publish_date.isoformat(),
            'publisher':self.publisher
        }