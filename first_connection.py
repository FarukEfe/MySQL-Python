import mysql.connector as provider


# DB Connection
mydb = provider.connect(
    host = "localhost",
    user = "root",
    password = "farukefesql1234"
)

# DB Creation
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES") # This is an SQL script

# DB Display
for x in mycursor:
    print(x)
print(mydb)

mycursor.execute("CREATE DATABASE mydatabase")

mydb = provider.connect(
    host = "localhost",
    user = "root",
    password = "farukefesql1234",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# SQL scripts to create tables, databases, etc. (it's a table in this case)
mycursor.execute('CREATE TABLE customers (name VARCHAR(100), adress VARCHAR(500))')