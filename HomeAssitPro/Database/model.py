from flask_sqlalchemy import SQLAlchemy,numeric,LargeBinaryObject
import datetime 



db=SQLAlchemy()


class ServiceRequest(db.Model):
    __tablename___='customer'
    ServiceRequestId=db.Column(db.integer,primary_key=True);
    DateOfRequest=db.Column(db.datetime,nullable=False,default=datetime.datetime)
    DateOfCompletion=db.Column(db.datetime)
    ServiceStatus=db.column(db.string,nullable=False)
    ServiceRating=db.column(db.string)
    Remarks=db.Column(db.string)
    #foreign keys 
    CustomerId=db.Column(db.Integer, db.ForeignKey('customer.CustomerId'), nullable=False)
    ProfessionalId= db.Column(db.Integer, db.ForeignKey('professional.ProfessionalId'), nullable=False)
    ServiceId= db.Column(db.Integer, db.ForeignKey('service.ServiceId'), nullable=False)
    #Service_Customer_Association
    Customer_Service= db.relationship('customer',backref='cust_req',uselist=False)
    #Service_Professional_Association
    Professional_Service= db.relationship('professional',backref='prof_req',uselist=False)


class User(db.Model):
    __tablename__='users'
    Userid = db.Column(db.integer,primary_key=True);
    Email = db.Column(db.String,nullable=False); 
    Password = db.Column(db.string,default=False); 
    Role = db.Column(db.String,default='user'); 
    #Customer_User_Association
    Customer= db.relationship('customer',backref='cust',uselist=False)
    #Professional_User_Association
    professional = db.relationship('professional',backref='prof',uselist=False)
class Customer(db.Model):
    __tablename___='customer'
    CustomerId=db.Column(db.integer,primary_key=True);
    FirstName=db.Column(db.string,nullable=False)
    LastName=db.Column(db.string)
    Phoneno=db.Column(db.integer,nullable=False)
    HouseNo=db.Column(db.string)
    Addressline1=db.column(db.string,nullable=False)
    Addressline2=db.column(db.string,nullable=False)
    City=db.Column(db.string)
    Country=db.Column(db.string,default='India')
    Pincode=db.Column(db.integer,nullable=False)
    #ForeignKey
    UserId=db.Column(db.Integer, db.ForeignKey('user.UserId'), nullable=False)

class Professional(db.Model):
    __tablename___='professional'
    ProfessionalId=db.Column(db.integer,primary_key=True);
    FirstName=db.Column(db.string,nullable=False)
    LastName=db.Column(db.string)
    Phoneno=db.Column(db.integer,nullable=False)
    AlternatePhoneno=db.Column(db.integer)
    HouseNo=db.Column(db.string)
    Addressline1=db.column(db.string,nullable=False)
    Addressline2=db.column(db.string,nullable=False)
    City=db.Column(db.string)
    Country=db.Column(db.string,default='India')
    Pincode=db.Column(db.integer,nullable=False)
    ServiceID=db.Column(db.integer,nullable=False)
    ExperienceInYrs=db.Column(db.integer,nullable=False)
    documents=db.Column(LargeBinaryObject)
    #ForeignKey
    UserId=db.Column(db.Integer, db.ForeignKey('user.UserId'), nullable=False)

class Service(db.Model):
    __tablename__='service'
    ServiceId=db.Column(db.integer,primary_key=True);
    ServiceName=db.Column(db.string,nullable=False);
    ServiceCode=db.Column(db.string,nullable=False)
    ServiceDescription=db.Column(db.string)
    BasePrice=db.Column(numeric(10,2),nullable=False)
    DateCreated=db.Column(db.datetime,nullable=False,default=datetime.datetime)
    #Service_Professional_Relationship 
    service_opted= db.relationship('professional',backref='prof_ser',uselist=False)