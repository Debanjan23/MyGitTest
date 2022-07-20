import mysql.connector as con4
import logging

logging.basicConfig(filename= 'groupby.log',filemode= 'w',level= logging.DEBUG , format= '%(asctime)s %(message)s')

try:
    mydb = con4.connect(host='localhost', username='root', password='Skhan87!', db='debanjan')
    cursor = mydb.cursor()

    s ="call select_pre()"

    #s1 = "delimiter && 'create procedure select_pre_filter2(IN var int ,IN var1 varchar(30))'BEGIN''select * from bank_details where job = var1 and balance > var'
         #'END &&'"


    cursor.execute(s)

    for i in cursor.fetchall():
        logging.info(i)

except Exception as e:
    logging.exception(e)