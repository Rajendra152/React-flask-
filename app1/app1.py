import os
#from config import Config
from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
#pip install Flask-SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
#pip install Flask-Migrate
from flask_migrate import Migrate



app=Flask(__name__)

##SQL alchemy Configuration##

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI']=#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initially log creation is false when we deploy we will change

db=SQLAlchemy(app)
Migrate(app,db)
#------------------------------------------------------#

#--------------- create a model -----------------------#

class color(db.Model):
    __tablename__ = 'sabjis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    mrp=db.Column(db.Integer)#schema

    def __init__(self,name,mrp):
        self.name= name
        self.mrp= mrp
      
    def __repr__(self):
        return "color Name - {} and MRP - {}".format(self.name,self.mrp)

#--------------------------------------------------------------#
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        name = request.form.get('in_1')
        mrp = request.form.get('in_2')

        #adding to create data
        new_color= color(name,mrp)
        db.session.add(new_color)
        db.session.commit()


    return render_template('add.html')

@app.route('/search')
def search():
    name = request.args.get("in_1")
    colors=color.query.filter_by(name=name).first()
    return render_template('s.html',col=colors)

@app.route('/dispaly')
def display_all():
    colors=color.query.all()
    return render_template('display.html',colors=colors)



if __name__ == "__main__":
    app.run(debug=True)