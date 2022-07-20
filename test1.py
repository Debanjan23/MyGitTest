import mysql.connector as con

mydb = con.connect(host = "localhost" , user ="root" , passwd = "Skhan87!" )
cursor = mydb.cursor()
s = "create table debanjan.ineuron(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20), emp_salary int(6), emp_attendence int(3))"
cursor.execute(s)

