from app import db
from sqlalchemy import Text,Float,JSON

class ProcessData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(Text)
    price = db.Column(Float)
    description = db.Column(Text)
    category = db.Column(Text)
    rating = db.Column(JSON)
