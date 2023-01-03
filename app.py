# Importing Flask,render templates,request and redirect module
from flask import Flask,render_template,request,redirect
# importing DataBase class from db file
from db import DataBase
# importing API python file
import api

dbo=DataBase()      # creating object of DataBase class to access database related code
app=Flask(__name__)

# creating log in page 
@app.route('/')
def index():
    return render_template('login.html')

# Creating registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Registration will get perform and it user data will be store in database file i.e. user.json
@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=dbo.register(name,email,password)
    if response:
        return render_template('login.html',message='Registration succesfull')
    else:
        return render_template('register.html',message='user already exist')

# Log-in is perform here and it will redirect to profile page
@app.route('/perform_login',methods=['POST'])
def perform_login():
    email=request.form.get('email')
    password=request.form.get('password')
    response=dbo.log_in(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect username or password')
# It will open profile page which shows us various options 
@app.route('/profile')
def profile():
    return render_template('profile.html')
# it will open name entity recognistion page where you can add page
@app.route('/ner')
def ner():
    return render_template('ner.html')
# it will dectect all the name according to their type
@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    text=request.form.get('ner_text')
    res=api.ner(text)
    return render_template('ner.html',res=res)
# it will open Sentimental analysis page where you can add page
@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')
#  It will perform sentimental analysis
@app.route('/perform_sentiment',methods=['POST'])
def perform_sentiment():
    text=request.form.get('sent')
    res=api.sentiment(text)
    return render_template('sentiment.html',res=res)
# It will open abuse detection page
@app.route('/abuse')
def abuse():
    return render_template('abuse.html')
# it will detect whether the language is abusive or not
@app.route('/perform_abuse',methods=['POST'])
def perform_abuse():
    text=request.form.get('abuse')
    res=api.abuse(text)
    return render_template('abuse.html',res=res)
app.run(debug=True)
