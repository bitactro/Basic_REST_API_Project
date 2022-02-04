# save this as app.py
from re import S
import sqlite3
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/")
def index():
    return "API"

@app.route("/books/get")
def getBooks():
    con = sqlite3.connect("bookdb.db")
    con.row_factory =sqlite3.Row

    cur= con.cursor()

    cur.execute("SELECT *from books")

    rows=cur.fetchall()
    data = []
    for row in rows:
        data.append([x for x in row])
    return jsonify(data)



@app.route("/books/get/<id>")
def getBookById():
    con = sqlite3.connect("bookdb.db")
    con.row_factory =sqlite3.Row

    cur= con.cursor()

    cur.execute("SELECT *from books where id="+id)

    rows=cur.fetchone()
    data = []
    
    data.append([x for x in rows])
    return jsonify(data)
   


@app.route('/books/add', methods=['POST','GET'])
def addBooks():
    if request.method == 'POST':
     with sqlite3.connect("bookdb.db") as con:
        cur =con.cursor()
     try:
        title=request.json['title']
        desc=request.json['desc']
        price=request.json['price']

        cur.execute("INSERT INTO books(title, desc, price) VALUES(?,?,?)",(title,desc,price))
        con.commit()
        msg="Record Successfully added"
     except:
         con.rollback()
         msg="error in adding record."
     finally:
         con.close()
         return msg
         


    return "Book"


    
if __name__ == "__main__":
    app.run(debug=True)