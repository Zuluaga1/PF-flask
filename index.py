from os import error
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

#mysql connection-----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PORT'] = 8111
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'placas'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('loginp.html')

#---------------dashboard-------------------
@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        return render_template('dashboard.html')
    
@app.route('/da', methods=["GET"])
def da():
    cur = mysql.connection.cursor()
    squery = "SELECT r.rol, count(e.rol) FROM placas.entrada e, placas.rol r  where e.rol=r.idrol  group by e.rol having count(e.rol)>1 ORDER by e.idEntrada;"
    cur.execute(squery)
    #if (error): print(error)
    data = cur.fetchall()
    
    #print(data)
    data = dict((x,y)for x, y in data)
    print(data)
    ##print(data)
    ##print(type(data))
    data = json.dumps(data)
    
    return data

#la placa y esas cosas
@app.route('/entrada')
def entrada():
    return render_template('entrada.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form['user']
        password = request.form['contraseña']
        #print(user)
        cur = mysql.connection.cursor()
        squery = "SELECT user, password FROM log where user = %s and password= %s"
        cur.execute(squery, [user,password])
        data = cur.fetchone()
        cur.close()
        #print(data)
        if data == None:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('entrada'))
            

#MYSQL------------------------------------------

        
        


    




#corriendo  
if __name__ == '__main__':
    app.run(debug=True)