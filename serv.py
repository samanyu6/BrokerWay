from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9182736455'
app.config['MYSQL_DB'] = 'housing'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

"""@app.route('/')
def home():
    return render_template('index.html')"""

@app.route('/')
def apartment():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM person''')
    data = cur.fetchall()
    return render_template('per.html', data = data)

@app.route('/insert_person', methods = ['GET','POST'])
def insert_person():
    try:
        if request.method == 'POST':
            pid = request.form['pid']
            n = request.form['name']
            p = request.form['phone']
            cur = mysql.connection.cursor()
            print pid,n,p
            cur.execute("INSERT INTO person(per_id,name,phone) VALUES(%s,%s,%s);",(pid,n,p))
            mysql.connection.commit()
    except:
        print(Exception)
    return render_template('insert.html')

@app.route('/admin_login', methods = ['GET','POST'])
def admin_login():
    if request.method == 'POST':
        admin_id = request.form['admin_id']
        admin_pass = request.form['pass']
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM admin WHERE (admin_id, password) = (%s,%s)''',(admin_id,admin_pass))
        n = cur.fetchall()
        if len(n)!=0:
            print 'Enter'
        else:
            print 'Wrong'
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug = True)
