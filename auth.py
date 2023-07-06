import sqlite3
 
def createTable():
 	connection = sqlite3.connect("authenticate.db")
 	connection.execute("CREATE TABLE minipuser (USERNAME TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT)")
 	connection.execute("INSERT INTO minipuser VALUES(?,?,?)",('ssaral','ssaral@gmail.com','passsword'))
 	connection.commit()
 	result = connection.execute("SELECT * FROM USERS")

 	for data in result:
 		print("USERNAME: ", data[0])
 		print("EMAIL_ID: ", data[1])
 		print("PASSWORD: ", data[2])

 	connection.close()

createTable()
