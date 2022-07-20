import mysql.connector as con1
import logging

logging.basicConfig(filename="mysql.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

try :

    mydb = con1.connect(host="localhost", user="root", passwd="Skhan87!", db = "debanjan")
    cursor = mydb.cursor()
    s= "create table if not exists debanjan.bank_detail1(age int, job varchar(30),marital_status varchar(30),account_no varchar(60), mobile_no varchar(40))"
    cursor.execute(s)
    s1 = "insert into bank_detail1 values(26, 'Salaried', 'Married','343525090254','84024024924') "

    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)
    cursor.execute(s1)

    mydb.commit()

except Exception as e :
    logging.exception(e)