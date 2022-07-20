import mysql.connector as con1
import logging

logging.basicConfig(filename = "mysql.log",filemode= "w",level=logging.DEBUG, format = "%(asctime)s %(levelname)s %(msg)s")

try:
    mydb = con1.connect( host = "localhost", username = "root", password = "Skhan87!", use_pure = True)
    print(mydb)
    cursor = mydb.cursor()
    #s = "create table mydata.ineuron1(emp_id int(10),emp_name varchar(20),emp_salary varchar(20),emp_age int(10))"
    #cursor.execute(s)

    s1 = "insert into mydata.ineuron1 values(101,'Debanjan','60000',34)"

    cursor.execute(s1)

    mydb.commit()
    cursor.execute("select * from mydata.ineuron1")

    for i in cursor.fetchall():
        print(i)

except Exception as e:
    raise ValueError(e)


