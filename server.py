#Make sure that flask_login and bcrypt are installed
from flask_login import login_user,logout_user,current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from flask import Flask,redirect,url_for,render_template,request

#Position all of this after the db and app have been initialised
app=Flask(__name__)
bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# @login_manager.user_loader
# def user_loader(user_id):
#     #TODO change here
#     return User.query.get(user_id)

# A route to display the home page
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

#TODO preethivi: integrate the QR code function to the server and Generate QR code when they hit sumbit

#TODO preethivi: add a route to display the feedback data

#TODO preethivi: in the feedback display route, add a filter to select feedbacks between selected date

#TODO preethivi: [optional] create a dashboard with visualization for the feedback data

#TODO jivi: connect server with db

#TODO jivi: create route to get specific data from db

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)