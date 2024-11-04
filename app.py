import os
from flask import Flask,render_template, request,url_for, redirect,session,flash


app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/register/<usertypename>',methods=['GET','POST'])
def register():
    pass 

    



