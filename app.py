import os
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_session import Session 
from markupsafe import escape
import json
import uuid
from os.path import join, dirname, realpath
from flask_uploads import IMAGES, UploadSet, configure_uploads
from pathlib import Path

app = Flask(__name__)

app.config['SECRET_KEY'] = '_1#y6G"F7Q2z\n\succ/'
app.config['APPLICATION_ROOT'] = "/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/pw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'sqlalchemy'

db = SQLAlchemy(app)

files = UploadSet('files', IMAGES)

app.config['UPLOADED_FILES_ALLOW'] = set(['png', 'jpg', 'jpeg'])
app.config['UPLOADED_FILES_DEST'] = 'static/upload'
configure_uploads(app, files)

app.config['SESSION_SQLALCHEMY'] = db
app.config['APPLICATION_ROOT'] = "/"

sess = Session(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    img = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self,name,email,phone,img,password):
        self.name=name
        self.email=email
        self.phone=phone
        self.img=img
        self.password=password
    
    def __repr__(self):
        return repr(id)

class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    size = db.Column(db.String(100))
    beds = db.Column(db.String(100))
    baths = db.Column(db.String(100))
    garagenumber = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.String(100))
    location = db.Column(db.String(100))
    img = db.Column(db.String(100))
    ownername = db.Column(db.String(100), nullable=False)
    owneremail = db.Column(db.String(100))
    ownerphone = db.Column(db.String(100), nullable=False)
    ownerimg = db.Column(db.String(100))

    def __init__(self,name,size,beds,baths,garagenumber,description,price,location,img,ownername, owneremail, ownerphone, ownerimg):
        self.name=name
        self.size=size
        self.beds=beds
        self.baths=baths
        self.garagenumber=garagenumber
        self.description=description
        self.price=price
        self.location=location
        self.img=img
        self.ownername=ownername     
        self.owneremail=owneremail  
        self.ownerphone=ownerphone     
        self.ownerimg=ownerimg 
    
    def __repr__(self):
        return repr(id)
    

@app.route("/mapteste")
def mapteste():
    return render_template('mapteste.html')

@app.route("/admin_main")
def admin_main():
    if 'username' in session:
        total_users = User.query.count()
        total_props = Property.query.count()
        return render_template('admin.html', total_users=total_users, total_props=total_props)
    return render_template('login.html')

@app.route("/list_user")
def list_user():
    if 'username' in session:
        data = User.query.all()
        return render_template('list_user.html', data=data)
    return redirect(url_for('admin_main'))

@app.route("/add_user")
def add_user():
    if 'username' in session:
        return render_template('add_user.html')
    return redirect(url_for('admin_main'))

@app.route('/insert_user', methods=['POST'])
def insert_user():
    if 'username' in session:
        descending = User.query.order_by(User.id.desc())
        last_item = descending.first()
        last_id = last_item.id + 1
        u = User.query.all()
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        img = request.files['img']
        password = request.form['password']
        filename = 'static/img/user.png'
        if request.method == 'POST' and img:
            filename = 'static/upload/' + files.save(request.files['img']) 
        new_user = User(name=name, email=email, phone=phone, img=filename, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_user'))
    return redirect(url_for('admin_main'))

@app.route("/add_prop")
def add_prop():
    if 'username' in session:
        return render_template('add_prop.html')
    return redirect(url_for('admin_main'))  

@app.route("/add_prop2")
def add_prop2():
    if 'username' in session:
        return render_template('add_prop2.html')
    return redirect(url_for('admin_main'))  

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'username' in session:
        data=request.args.get('id_user')
        #print('teste'+data_file)
        User.query.filter_by(id=data).delete()
        #my_file = Path(os.path.join(app.config['UPLOADED_FILES_DEST'], data_file))
        #if my_file.exists():
            #os.remove(os.path.join(app.config['UPLOADED_FILES_DEST'], data_file))
        db.session.commit()
        return redirect(url_for('list_user'))
    return redirect(url_for('admin_main'))  

@app.route("/update_user", methods=['POST'])
def update_user():
    if 'username' in session:
        data=request.args.get('id_user')
        update = User.query.filter_by(id=data)

        return render_template('edit_user.html', update=update)
    return redirect(url_for('admin_main'))   

@app.route('/edit_user', methods=['POST'])
def edit_user():
    if 'username' in session:
        
        data = request.form['id']
        #print('teste'+str(data))
        update = User.query.filter_by(id=data).first()
        bd_img = update.img
        img = request.files['img']

        if request.method == 'POST' and 'name' in request.form:
            update.name = request.form['name'] 

        if request.method == 'POST' and 'email' in request.form:    
            update.email = request.form['email']

        if request.method == 'POST' and 'phone' in request.form:
            update.phone = request.form['phone']

        update.img = bd_img
        if request.method == 'POST' and img:
            update.img = 'static/upload/' + files.save(request.files['img']) 

        if request.method == 'POST' and 'password' in request.form:
            update.password = request.form['password'] 

        db.session.commit()
        return redirect(url_for('list_user'))
    return redirect(url_for('admin_main'))    

@app.route('/insert_prop', methods=['POST'])
def insert_prop():
    descending = Property.query.order_by(Property.id.desc())
    last_item = descending.first()
    last_id = last_item.id + 1
    p = Property.query.all()
    
    name = request.form['name']   
    size = request.form['size']
    beds = request.form['beds']
    baths = request.form['baths']   
    garagenumber = request.form['garagenumber']
    description = request.form['description']
    price = request.form['price']
    location = request.form['location']
    img = request.files['img']
    ownername = request.form['ownername']
    owneremail = request.form['owneremail']
    ownerphone = request.form['ownerphone']
    ownerimg = request.files['ownerimg']

    filename = 'static/img/h2.jpg'
    filename2 = 'static/img/user.png'

    if request.method == 'POST' and img:
        filename = 'static/upload/' + files.save(request.files['img'])    
    if request.method == 'POST' and ownerimg:
        filename2 = 'static/upload/' + files.save(request.files['ownerimg'])   
    new_prop = Property(name=name, size=size, beds=beds, img=filename, garagenumber=garagenumber, baths=baths, description=description, price=price, ownername=ownername, owneremail=owneremail, ownerphone=ownerphone, ownerimg=filename2, location=location)
    db.session.add(new_prop)
    db.session.commit()
    return redirect(url_for('list_prop'))  

@app.route('/delete_prop', methods=['POST'])
def delete_prop():
    if 'username' in session:
        data=request.args.get('id_prop')
        #print('teste'+data_file)
        Property.query.filter_by(id=data).delete()
        #my_file = Path(os.path.join(app.config['UPLOADED_FILES_DEST'], data_file))
        #if my_file.exists():
            #os.remove(os.path.join(app.config['UPLOADED_FILES_DEST'], data_file))
        db.session.commit()
        return redirect(url_for('list_prop'))
    return redirect(url_for('admin_main'))   

@app.route("/update_prop", methods=['POST'])
def update_prop():
    if 'username' in session:
        data=request.args.get('id_prop')
        update = Property.query.filter_by(id=data)

        return render_template('edit_prop.html', update=update)
    return redirect(url_for('admin_main')) 

@app.route('/edit_prop', methods=['POST'])
def edit_prop():
    if 'username' in session:
        
        data = request.form['id']
        #print('teste'+str(data))
        update = Property.query.filter_by(id=data).first()
        bd_img = update.img
        bd_img2 = update.ownerimg
        img = request.files['img']
        ownerimg = request.files['ownerimg']

        if request.method == 'POST' and 'name' in request.form:
            update.name = request.form['name'] 

        if request.method == 'POST' and 'size' in request.form:    
            update.size = request.form['size']

        if request.method == 'POST' and 'beds' in request.form:
            update.beds = request.form['beds']

        if request.method == 'POST' and 'baths' in request.form:
            update.baths = request.form['baths'] 

        if request.method == 'POST' and 'garagenumber' in request.form:    
            update.garagenumber = request.form['garagenumber']

        if request.method == 'POST' and 'description' in request.form:
            update.description = request.form['description']

        if request.method == 'POST' and 'price' in request.form:
            update.price = request.form['price']

        if request.method == 'POST' and 'location' in request.form:
            update.location = request.form['location']

        update.img = bd_img
        if request.method == 'POST' and img:
            update.img = 'static/upload/' + files.save(request.files['img'])    

        if request.method == 'POST' and 'ownername' in request.form:
            update.ownername = request.form['ownername']

        if request.method == 'POST' and 'owneremail' in request.form:
            update.owneremail = request.form['owneremail']

        if request.method == 'POST' and 'ownerphone' in request.form:
            update.ownerphone = request.form['ownerphone']

        update.ownerimg = bd_img2
        if request.method == 'POST' and ownerimg:
            update.ownerimg = 'static/upload/' + files.save(request.files['ownerimg'])    

        db.session.commit()
        return redirect(url_for('list_prop'))
    return redirect(url_for('admin_main'))     

@app.route("/list_prop")
def list_prop():
    if 'username' in session:
        data = Property.query.all()
        data2 = User.query.all()
        return render_template('list_prop.html', data=data, data2=data2)
    return redirect(url_for('admin_main'))

@app.route('/admin')
def admin():
    if 'username' in session:
        return render_template('admin.html')
    return redirect(url_for('admin_main'))

@app.route('/login', methods=['POST'])
def login():
        email = request.form['email']
        password = request.form['pass']
        querydata = User.query.filter_by(email = email, password = password).first()
        session['username'] = querydata.name
        session['profile'] = querydata.img
        return redirect(url_for('admin_main')) 
        

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect(url_for('main')) 

@app.route("/prop", methods=['POST'])
def prop():
    
    data = request.args.get('id_prop')
    #print(str(id)) 
    p = Property.query.filter_by(id=data).first()
    return render_template('home.html',
        idprop = p.id,
        nameprop = p.name,
        sizeprop = p.size,
        bedsprop = p.beds,
        bathsprop = p.baths,
        garageprop = p.garagenumber,
        descriptionprop = p.description,
        priceprop = p.price,
        locationprop = p.location,
        imgprop = p.img,
        ownername = p.ownername,
        ownerimg = p.ownerimg,
        owneremail = p.owneremail,
        ownerphone = p.ownerphone
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
        garageprop = p.garagenumber,
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
        garageprop = p.garagenumber,
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

if __name__ == '__main__':
    app.run(debug=True)


#db.session.query(db.func.avg(User.id)).scalar()
#db.session.query(db.func.sum(User.id)).scalar()
#db.session.query(db.func.min(User.id)).scalar()
#db.session.query(db.func.max(User.id)).scalar()
#db.session.query(db.func.dayname(User.date_joined)).all()
#db.session.query(User.email, db.func.dayname(User.date_joined)).filter(db.func.dayname(User.date_joined) == 'Monday').all()