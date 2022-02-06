# save this as app.py
import Model
from re import S
from flask import Flask
import ConDB
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///appdb.db'
db=SQLAlchemy(app)

    

@app.route("/")
def index():
    return "API"

@app.route("/books/get")
def getBooks():

    try:
        #con = sqlite3.connect("appdb.db")
        #con.row_factory =sqlite3.Row

        #cur= con.cursor()
        #cur.execute("SELECT *from book_model")
        #rows=cur.fetchall()
        rows=Model.BookModel.query.all()
        data = []
        for row in rows:
           d={
               "id":row.id,
               "title":row.title,
               "desc":row.desc,
               "price":row.price
           }
           data.append(d)
    except:
        data="error"
    #con.close()
    return jsonify(data)



@app.route("/books/get/<string:id>", methods=['POST','GET'])
def getBookById(id):
    if request.method == 'GET':
        response_msg="no records exists with id="+str(id)
        try:
            #con = sqlite3.connect("appdb.db")
            #con.row_factory =sqlite3.Row
            #cur= con.cursor()
            #cur.execute("SELECT *from book_model where id="+str(id))
            #rows=cur.fetchall()
            rows=Model.BookModel.query.filter_by(id=id)
            for row in rows:
                response_msg={
                    "id":row.id,
                    "title":row.title,
                    "desc":row.desc,
                    "price":row.price
                }
            
        except:
            response_msg="ERROR"
        finally:
            #con.close()
            return response_msg

        
   


@app.route('/books/add', methods=['POST','GET'])
def addBooks():
    if request.method == 'POST':
    
     #with sqlite3.connect("bookdb.db") as con:
        #cur =con.cursor()
     try:
        title=request.json['title']
        desc=request.json['desc']
        price=request.json['price']

        book=Model.BookModel(title, desc, price)
        db.session.add(book)
        db.session.commit()

        #cur.execute("INSERT INTO books(title, desc, price) VALUES(?,?,?)",(title,desc,price))
        #con.commit()
        msg="Record Successfully added"
     except:
         #con.rollback()
         msg="error in adding record."
     finally:
         #con.close()
         return msg
         


    return "Book"


    
if __name__ == "__main__":
    app.run(debug=True)