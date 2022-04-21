from flask import Flask,render_template
# import mysql.connector
# import os

app=Flask(__name__)
# app.secret_key=os.urandom(24)
# conn=mysql.connector.connect(host="localhost",user="root",database="kjhackathon")
# cursor=conn.cursor()


@app.route('/')
def home():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)

