import os
from flask import Flask,render_template, request,url_for, redirect,session,flash
import jinja2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import datetime 

cwd = os.getcwd()

app=Flask(__name__,template_folder='Templates')
database_path = os.path.join(cwd,'HomeAssitPro','Database.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path



db=SQLAlchemy()

class ServiceRequest(db.Model):
    __tablename___='customer'
    ServiceRequestId=db.Column(db.Integer,primary_key=True);
    DateOfRequest=db.Column(db.DateTime,nullable=False,default=datetime.datetime)
    DateOfCompletion=db.Column(db.DateTime)
    ServiceStatus=db.Column(db.String,nullable=False)
    ServiceRating=db.Column(db.String)
    Remarks=db.Column(db.String)
    #foreign keys 
    CustomerId=db.Column(db.Integer, db.ForeignKey('customer.CustomerId'), nullable=False)
    ProfessionalId= db.Column(db.Integer, db.ForeignKey('professional.ProfessionalId'), nullable=False)
    ServiceId= db.Column(db.Integer, db.ForeignKey('service.ServiceId'), nullable=False)
    #Service_Customer_Association
    Customer_Service= db.relationship('Customer',backref='cust_req',uselist=False)
    #Service_Professional_Association
    Professional_Service= db.relationship('Professional',backref='prof_req',uselist=False)


class User(db.Model):
    __tablename__='user'
    UserId = db.Column(db.Integer,primary_key=True);
    Email = db.Column(db.String,nullable=False,unique=True); 
    Password = db.Column(db.String,default=False); 
    Role = db.Column(db.String,default='user'); 
    #Customer_User_Association
    Customer= db.relationship('Customer',backref='cust',uselist=False)
    #Professional_User_Association
    professional = db.relationship('Professional',backref='prof',uselist=False)
class Customer(db.Model):
    __tablename___='customer'
    CustomerId=db.Column(db.Integer,primary_key=True);
    FirstName=db.Column(db.String,nullable=False)
    LastName=db.Column(db.String)
    Phoneno=db.Column(db.Integer,nullable=False,unique=True)
    HouseNo=db.Column(db.String)
    Addressline1=db.Column(db.String,nullable=False)
    Addressline2=db.Column(db.String,nullable=False)
    City=db.Column(db.String)
    Country=db.Column(db.String,default='India')
    Pincode=db.Column(db.Integer,nullable=False)
    #ForeignKey
    UserId=db.Column(db.Integer, db.ForeignKey('user.UserId'), nullable=False)

class Professional(db.Model):
    __tablename___='professional'
    ProfessionalId=db.Column(db.Integer,primary_key=True);
    FirstName=db.Column(db.String,nullable=False)
    LastName=db.Column(db.String)
    Phoneno=db.Column(db.Integer,nullable=False,unique=True)
    AlternatePhoneno=db.Column(db.Integer)
    HouseNo=db.Column(db.String)
    Addressline1=db.Column(db.String,nullable=False)
    Addressline2=db.Column(db.String,nullable=False)
    City=db.Column(db.String)
    Country=db.Column(db.String,default='India')
    Pincode=db.Column(db.Integer,nullable=False)
    ExperienceInYrs=db.Column(db.Integer,nullable=False)
    documents=db.Column(LargeBinary)
    #ForeignKey
    UserId=db.Column(db.Integer, db.ForeignKey('user.UserId'), nullable=False)
    ServiceID=db.Column(db.Integer, db.ForeignKey('service.ServiceId'), nullable=False)

class Service(db.Model):
    __tablename__='service'
    ServiceId=db.Column(db.Integer,primary_key=True);
    ServiceName=db.Column(db.String,nullable=False);
    ServiceCode=db.Column(db.String,nullable=False)
    ServiceDescription=db.Column(db.String)
    BasePrice=db.Column(Numeric(10,2),nullable=False)
    DateCreated=db.Column(db.DateTime,nullable=False,default=datetime.datetime)
    #Service_Professional_Relationship 
    service_opted= db.relationship('Professional',backref='prof_ser',uselist=False)



# def CreateAdmin():
#     user = db.session.get(User, 'admin@HomeAssitPro')
#     if not user:
#         user = User(Email='admin@homeassitpro',Password='1',Role='admin')
#         db.session.add(user); 
#         db.session.commit()
#         print('admin created')
#     return ''



db.init_app(app)
app.app_context().push()

 



@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        Email=request.form.get('email')
        password=request.form.get('pwd')
        print(Email,password)
        User1=User.query.filter(User.Email==Email and User.Password==password).first()
        if User1 and User1.Role=='admin':
            return render_template('Admin.html')
        elif User1 and User1.Role=='customer':
            return render_template('Dashboard.html')
        else:
            return redirect(url_for('home'))
            

@app.route('/register/<usertypename>')
def register(usertypename):
    if usertypename == 'customer':
        return redirect(url_for('customer_signup'))
    # Add more conditions for other user types if needed
    elif usertypename=='professional':
        return redirect(url_for('professional_signup'))
    return "User type not recognized"

@app.route('/customer_signup',methods=['POST','GET'])
def customer_signup():
    if request.method=='GET':
        return render_template('Customer.html')
    elif request.method=='POST':
        ph=request.form.get('ph')
        email=request.form.get('email')
        pwd=request.form.get('pwd')
        user=User.query.filter(User.Email==email and User.Password==pwd).first()
        print(user)
        if user:
            return render_template('index.html')
        else:
            fname=request.form.get('fname')
            lname=request.form.get('lname')
            hno=request.form.get('plot')
            ad1=request.form.get('ad1')
            ad2=request.form.get('ad2')
            cty=request.form.get('city')
            ctry=request.form.get('country')
            pc=request.form.get('pc')

            user = User(Email=email,Password=pwd,Role='customer')
            db.session.add(user); 
            db.session.commit()
            
            cust = Customer(FirstName=fname,\
            LastName=lname,HouseNo=hno,Addressline1=ad1,Addressline2=ad2,\
            City=cty,Country=ctry,Phoneno=ph,Pincode=pc,UserId=user.UserId)
            db.session.add(cust); 
            db.session.commit()
            return render_template('Submit.html')
        
        


@app.route('/professional_signup')
def professional_signup():
    return render_template('ServiceProfessional.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__=='__main__':
    db.create_all()
    #CreateAdmin()
    app.run(debug=True)

    



