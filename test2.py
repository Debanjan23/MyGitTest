import mysql.connector as con

mydb = con.connect(host = "localhost" , user ="root" , passwd = "Skhan87!" )
cursor = mydb.cursor()
s = "insert into debanjan.ineuron values(101 , 'sudhanshu kumar', 'sudhanshu@ineuron.ai' ,100 , 30)"

cursor.execute(s)
mydb.commit()