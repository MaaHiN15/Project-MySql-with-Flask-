import sqlite3
from flask import *

app = Flask(__name__)

def db():
    con = sqlite3.connect('database.db')
    return con


def table():
    con = db()
    cur = con.cursor()
    cur.execute("create table student (id int primary key not null, name varchar[100] not null, dept varchar[200]);")
    con.commit()    
    con.close()
    
def users():
    con = db()
    con.row_factory = sqlite3.row
    cur = con.cursor()
    cur.execute("select * from users;")
    rows = cur.fetchall()
    return rows


    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stu')
def stu():
    return render_template("stu.html")

@app.route('/final', methods=['GET', 'POST'])
def final():
    if request.method == "POST":
        try:
            msg = ""
            id = request.form['id']
            name = request.form['name']
            dept = request.form['dept']
            con = db()
            cur = con.cursor()
            cur.execute("insert into student (id,name,dept) values (?,?,?)", (id, name, dept))
            con.commit()
            msg = "insertion done"
        except:
            con.rollback()
            msg = "Insertion failure"
        finally:
            con.close()
    return render_template("final.html", msg = msg)
            


if __name__ == ("__main__"):
    app.run(debug=True)
