import mysql.connector as con3
import logging

logging.basicConfig(filename= 'bulddata.log',filemode= 'w',level= logging.DEBUG , format= '%(asctime)s %(message)s')

try:
    mydb = con3.connect(host='localhost', username='root', password='Skhan87!', db='debanjan')
    cursor = mydb.cursor()
    s1 = "select * from bank_detail1"
    cursor.execute(s1)

    for i in cursor.fetchall():
        print(i)

except Exception as e:
    logging.exception(e)
