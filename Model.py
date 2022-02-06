from api import db 
class BookModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    desc=db.Column(db.String, nullable=False)
    price=db.Column(db.Integer, nullable=False)

    def __init__(self, t, d, p):
        self.title = t
        self.desc = d
        self.price = p