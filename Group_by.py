import mysql.connector as con4
import logging

logging.basicConfig(filename= 'groupby.log',filemode= 'w',level= logging.DEBUG , format= '%(asctime)s %(message)s')

try:
    mydb = con4.connect(host='localhost', username='root', password='Skhan87!', db='debanjan')
    cursor = mydb.cursor()

    """Now need to type the query"""

    s1 = "select avg(balance), age , job, marital from bank_details group by job having sum(balance)>20"

    cursor.execute(s1)

    for i in cursor.fetchall():
            logging.info(i)

except Exception as e:
    logging.exception(e)
