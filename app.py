from sqlalchemy import or_
from Model.model import *
from flask import Flask,render_template

app=Flask(__name__) 
app.config['SECRET_KEY']="East"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///gs_store.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False  
app.config['SQLALCHEMY_SILENCE_UBER_WARNING']=1    

db.init_app(app)


#before_first_request():
#	db.create_all()


with app.app_context():
    db.create_all()