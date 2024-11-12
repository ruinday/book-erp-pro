from flask import jsonify,request
from flask_restful import Resource,reqparse

from .exts import db
from .models import Books

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='name is required.')

class BookResource(Resource):
    def get(self,bid:int):
        book = Books.query.get(bid)
        if book:
            return book.to_dict(),200
        else:
            return {'error':'Book id is not exists'},400
    
    def put(self,bid:int):
        book = Books.query.get(bid)
        if book:
            params = request.json
            book.name = params.get('name')
            book.author = params.get('author')
            book.price = params.get('price')
            book.publish_date = params.get('publish_date')
            book.publisher = params.get('publisher')
            db.session.commit()

            return {'msg':f'Book {book.name} id added!'},200
        else:
            return {'error':'Book id is not exists'},400
    
    def delete(self,bid:int):
        book = Books.query.get(bid)
        if book:
            try:
                db.session.delete(book)
                db.session.commit()
                return {'status':200,'msg':f'book {book.name} has deleted'}
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            return {'error':'Book id is not exists'},400

class BooklistResource(Resource):
    def get(self):
        books = Books.query.all()
        books_list = [it.to_dict() for it in books]
        return books_list
    
    def post(self):
        params = request.json
        book = Books(
            name = params.get('name'),
            author = params.get('author'),
            price = params.get('price'),
            publish_date = params.get('publish_date'),
            publisher = params.get('publisher')
        )
        try:
            db.session.add(book)
            db.session.commit()

            return {'msg':'OK'},200
        except Exception as e:
            db.session.rollback()
            raise e