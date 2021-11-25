import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

##SQL alchemy Configuration##

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI']=#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db=SQLAlchemy(app)
Migrate(app,db)


class EmployeeModel(db.Model):
    __tablename__='table'

    id= db.Column(db.Integer(),primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)    
    name=db.Column(db.String())
    age=db.Column(db.Integer())
    position=db.Column(db.String(81))

    def __init__(self,employee_id,name,age,position):
        self.employee_id=employee_id
        self.name=name
        self.age=age
        self.position=position

    def __repr__(self):
          return f"{self.name}:{self.employee_id}"

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/create',methods=["GET","POST"])
def create():
    if request.method == 'POST':
        employee_id = request.form.get('emplpoyee_id')
        name = request.form.get('name')
        age = request.form.get('age')
        position = request.form.get('position')

         #adding to create data
        employee=EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
    return render_template('createpage.html')

@app.route('/data')
def Retrivedata():
    employees=EmployeeModel.query.all()
    return render_template('datalist.html',employees=employees)


@app.route('/data/<int:id>')
def RetriveSingleEmployee(id):
    employee=EmployeeModel.query.filter_by(employee_id=id).first()
    if  employee:
        return render_template('data.html',employee=employee)
    return "Employee with id {} doesnt exist".format(id)

if __name__== "__main__":
    app.run(debug=True)