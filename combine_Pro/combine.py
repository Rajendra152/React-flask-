from flask import Flask, render_template, request
import cx_Oracle
app=Flask(__name__)

connection = cx_Oracle.connect('hr/hr@//localhost:1521/xe')


@app.route('/')
def home():
    return render_template("register.html")

@app.route('/registration',methods=['POST'])
def register():
    First_name=request.form.get('uname')
    Last_name=request.form.get('uname')

    email=request.form.get('email')
    phone_number=request.form.get('ph_num')
    gender=request.form.get('gen')
    age=request.form.get('age')
    password=request.form.get('password')
    cursor=connection.cursor()
    cursor.execute("""Insert into datalogin1 ('First_name','Last_name','email','password','phone_number','age','gender') values('{}','{}','{}','{}','{}','{}','{}')""".format(First_name,Last_name,email,password,phone_number,age,gender))
    connection.commit()
    return "User registered successfully"



@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor=connection.cursor()
    cursor.execute("""select * from datalogin1 where email like '{}' and password like '{}' """.format(email,password))
    users=cursor.fetchall()
    return users

if __name__== "__main__":
    app.run(debug=True)