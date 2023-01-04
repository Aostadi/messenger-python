import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', database='messenger')
cursor = db.cursor()
cursor.execute(
    'CREATE TABLE USERS (id INT AUTO_INCREMENT PRIMARY KEY , email VARCHAR(80) NOT NULL, password VARCHAR(70) NOT NULL, user VARCHAR(50),register_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,UNIQE (email), UNIQE (user))')