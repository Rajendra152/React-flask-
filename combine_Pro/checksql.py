
import cx_Oracle


connection = cx_Oracle.connect('hr/hr@//localhost:1521/xe')
print(connection.version)
cur=connection.cursor()
sql="""INSERT INTO DATALOGIN3 VALUES(:1,:2)"""
cur.execute(sql, ['MANI','TEJA'])


# @app.route('/registration',methods=['POST'])
# def register():
#     name=request.form.get('uname')
#     email=request.form.get('email')
#     phone_number=request.form.get('ph_num')
#     gender=request.form.get('gen')
#     password=request.form.get('password')

#     cursor.execute("""Insert into datalogin ('name','email','phone_number','gender','password') values('{}','{}','{}','{}','{}')""".format(name,email,password)
#     connection.commit()
#     return "User registered successfully"