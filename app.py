from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/pw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['APPLICATION_ROOT'] = "/"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    img = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    size = db.Column(db.String(100))
    beds = db.Column(db.String(100))
    baths = db.Column(db.String(100))
    garage = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.String(100))
    location = db.Column(db.String(100))
    img = db.Column(db.String(100))
    owner = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    
@app.route('/query', methods=['POST'])
def query():
    data = request.args.get('id_prop') #if key doesn't exist, returns None
    print('Diego '+str(data)) 
    return '''<h1>The language value is: {}</h1>'''.format(data)

@app.route("/prop", methods=['POST'])
def prop():
    data = request.args.get('id_prop')
    #print(str(id)) 
    p = Property.query.filter_by(id=data).first()
    u = User.query.first()
    return render_template('home.html',
        idprop = p.id,
        nameprop = p.name,
        sizeprop = p.size,
        bedsprop = p.beds,
        bathsprop = p.baths,
        garageprop = p.garage,
        descriptionprop = p.description,
        priceprop = p.price,
        locationprop = p.location,
        imgprop = p.img,
        ownerprop = u.id,
        ownerimg = u.img,
        owneremail = u.email,
        ownerphone = u.phone
    )
@app.route("/search", methods=['GET'])
def search():
    p = Property.query.filter_by(id=1).first()
    u = User.query.filter_by(id=1).first()
    return render_template('search.html',
        idprop = p.id,
        nameprop = p.name,
        sizeprop = p.size,
        bedsprop = p.beds,
        bathsprop = p.baths,
        garageprop = p.garage,
        descriptionprop = p.description,
        priceprop = p.price,
        locationprop = p.location,
        imgprop = p.img,
        ownerprop = u.id,
        ownerimg = u.img,
        owneremail = u.email,
        ownerphone = u.phone
    )

@app.route("/", methods=['GET'])
def main():
    p = Property.query.filter_by(id=1).first()
    u = User.query.filter_by(id=1).first()
    return render_template('index.html',
        idprop = p.id,
        nameprop = p.name,
        sizeprop = p.size,
        bedsprop = p.beds,
        bathsprop = p.baths,
        garageprop = p.garage,
        descriptionprop = p.description,
        priceprop = p.price,
        locationprop = p.location,
        imgprop = p.img,
        ownerprop = u.id,
        ownerimg = u.img,
        owneremail = u.email,
        ownerphone = u.phone
    )

def __init__(self, name, size):
    self.name = name
    self.size = size



#db.session.query(db.func.avg(User.id)).scalar()
#db.session.query(db.func.sum(User.id)).scalar()
#db.session.query(db.func.min(User.id)).scalar()
#db.session.query(db.func.max(User.id)).scalar()
#db.session.query(db.func.dayname(User.date_joined)).all()
#db.session.query(User.email, db.func.dayname(User.date_joined)).filter(db.func.dayname(User.date_joined) == 'Monday').all()