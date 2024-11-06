import os
from flask import Flask,render_template, request,url_for, redirect,session,flash
import jinja2

names=['sruta']
pwd=['1']

app=Flask(__name__,template_folder='Templates')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        first_name=request.get_data('fname')
        password=request.get_data('pwd')
        if first_name in names and password in pwd: 
            return render_template('Admin.html',first_name=first_name,password=password)
        else:
            return render_template('Admin.html',first_name=False,password=False)

@app.route('/register/<usertypename>')
def register(usertypename):
    if usertypename == 'customer':
        return redirect(url_for('customer_signup'))
    # Add more conditions for other user types if needed
    elif usertypename=='professional':
        return redirect(url_for('professional_signup'))
    return "User type not recognized"

@app.route('/customer_signup')
def customer_signup():
    return render_template('Customer.html')


@app.route('/professional_signup')
def professional_signup():
    return render_template('ServiceProfessional.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

if __name__=='__main__':
    app.run(debug=True)

    



