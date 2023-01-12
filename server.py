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


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)