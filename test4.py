import mysql.connector as con1
import logging

logging.basicConfig(filename="mysql.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

try :

    mydb = con1.connect(host="localhost", user="root", passwd="Skhan87!")
    cursor = mydb.cursor()

    s = "select emp_id, emp_name from mydata.ineuron1"
    cursor.execute(s)

    for i in cursor.fetchall() :
        print(i)

except Exception as e :
    logging.exception(e)
