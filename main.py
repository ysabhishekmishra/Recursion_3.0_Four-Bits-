from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
conn=mysql.connector.connect(host="localhost",user="root",database="recursion3.0")
cursor=conn.cursor()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cources')
def cources():
    return render_template("cources.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/adminlogin')
def Admin_login():
    return render_template("Admin.html")

@app.route('/adminlogin_validation',methods=['POST'])
def adminlogin_validation():
    email=request.form.get('name')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM admindata Where email Like '{}' and password like '{}'""".format(email,password))
    userdata=cursor.fetchall()
    

    if len(userdata)>0:
        session['session_no']=userdata
        return render_template('adminlandpage.html',data=userdata)
    else:
        return redirect('/adminlogin') 


@app.route('/order')
def order():
    if 'session_no' in session:
        return render_template("order.html")
    else:
        return redirect('/login')


@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('name')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM userdata Where email Like '{}' and password like '{}'""".format(email,password))
    userdata=cursor.fetchall()
    

    if len(userdata)>0:
        session['session_no']=userdata
        return redirect('/order')
    else:
        return redirect('/login') 


@app.route('/logout')
def logout():
    session.pop('session_no')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)

