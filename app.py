from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/pw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    size = db.Column(db.String(100))
    beds = db.Column(db.String(100))
    baths = db.Column(db.String(100))
    garage = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.String(100))
    location = db.Column(db.String(100))
    img = db.Column(db.String(100))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __init__(self, name, size):
    self.name = name
    self.size = size



#db.session.query(db.func.avg(User.id)).scalar()
#db.session.query(db.func.sum(User.id)).scalar()
#db.session.query(db.func.min(User.id)).scalar()
#db.session.query(db.func.max(User.id)).scalar()
#db.session.query(db.func.dayname(User.date_joined)).all()
#db.session.query(User.email, db.func.dayname(User.date_joined)).filter(db.func.dayname(User.date_joined) == 'Monday').all()