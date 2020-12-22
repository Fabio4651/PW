from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'PW'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def property():
    cur = mysql.connection.cursor()
    #cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')
    #cur.execute('''INSERT INTO example VALUES (1, 'Diego')''')
    #cur.execute('''INSERT INTO example VALUES (2, 'Zman')''')
    #mysql.connection.commit()

    cur.execute('''SELECT * FROM property, user''')
    results = cur.fetchall()
    print(results)
    #return results[1]['name']
    return render_template('hometeste.html',
        idprop = results[0]['id'],
        nomeprop = results[0]['name'],
        sizeprop = results[0]['size'],
        bedsprop = results[0]['beds'],
        bathsprop = results[0]['baths'],
        garageprop = results[0]['garage'],
        descriptionprop = results[0]['description'],
        priceprop = results[0]['price'],
        locationprop = results[0]['location'],
        imgprop = results[0]['img'],
        ownerprop = results[0]['user.name'],
        ownerimg = results[0]['user.img'],
        owneremail = results[0]['email'],
        ownerphone = results[0]['phone']
    )


#@app.route("/prop", methods=['GET'])
#def room_get():
 #   name = request.args.get('search')
  #  r = prop.query.filter_by(name=name).all()[0]
   # return render_template('index2.html',
    #    id = r.id,
     #   room_type = r.room_type,
      #  map_position_x = r.map_position_x,
       # map_position_y = r.map_position_y,
        #capacity = r.capacity
    #)


#cursor = mysql.get_db().cursor()

