from sys import executable
import mysql.connector as connector
from mysql.connector.errors import Error

class SQLMaster:
    connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "farukefesql1234",
    database = "node-app"
    )
    cursor = connection.cursor()

    def commit(func):
        def wrapper(*args):
            func(*args)
            try:
                SQLMaster.connection.commit() # Bütün sorguların çalışması için en sonda commit demek gerek, error throw edebilir
                print(f'{SQLMaster.cursor.rowcount} records have been added. Last element ID: {SQLMaster.cursor.lastrowid}')
            except connector.Error as err:
                print(f'There has been an error: {err}')
            finally:
                SQLMaster.connection.close()
                print('Connection Ended.')
        return wrapper
    
    @commit
    def insertElem(self,rowList:list):
        # Refer to the table 
        insertion = "INSERT INTO products(name,price,description,imgUrl) VALUES(%s,%s,%s,%s)" # The order of the keys and values should match (%s is a placeholder)
        #cursor.execute(insertion, rowList[0]) # For one item
        self.cursor.executemany(insertion,rowList) # For a list of items

    def selectElems(self,displayAllInfo:bool):
        if displayAllInfo:
            self.cursor.execute("SELECT * from products")
        else:
            self.cursor.execute("SELECT name,price,description from products")

        result = self.cursor.fetchall()
        for r in result:
            if displayAllInfo:
                print(f"\nID: {r[0]}\nProduct: {r[1]}\nPrice: {r[2]}\nDescription: {r[4]}\nImage URL: {r[3]}\n")
            else:
                print(f"\nProduct: {r[0]}\nPrice: {r[1]}\nDescription: {r[2]}\n")

    def selectCondition(self, conditionQuery:str):
        self.cursor.execute(f"SELECT * from products Where {conditionQuery}")
        # id=3, name='Samsung S6' and price>=2500, name LIKE '%Samsung%' (% means there are other characters in-between)
        try:
            result = self.cursor.fetchall()
            for r in result:
                print(f"\nID: {r[0]}\nProduct: {r[1]}\nPrice: {r[2]}\nDescription: {r[4]}\nImage URL: {r[3]}\n")
        except Error as err:
            print(err)

    def selectByID(self,id):
        executable = "SELECT * from products Where id=%s"
        param = (id,)
        self.cursor.execute(executable,param)
        try:
            r = self.cursor.fetchone()
            print(f"\nID: {r[0]}\nProduct: {r[1]}\nPrice: {r[2]}\nDescription: {r[4]}\nImage URL: {r[3]}\n")
        except Error as err:
            print(err)
            
    def getByOrder(self):
        self.cursor.execute("SELECT * from products Order By name, price") # 1st Priority name, 2nd one price

        try:
            result = self.cursor.fetchall()
            for r in result:
                print(f"\nID: {r[0]}\nProduct: {r[1]}\nPrice: {r[2]}\nDescription: {r[4]}\nImage URL: {r[3]}\n")
        except Error as err:
            print(err)

    def getInfo(self):
        # executable = "SELECT COUNT(*) from products" # Counts the number of rows in the table
        # executable = "SELECT AVG(price) from products" # Gets the average of the column given
        #executable = "SELECT SUM(price) from products" # Gets the sum of the values in the column given
        #executable = "SELECT MAX(price) from products" # Gets the max value in the column given
        #executable = "SELECT MIN(price) from products" # Gets the min value in the column given
        executable  = "SELECT name,price from products where price=(SELECT MAX(price) from products)"
        self.cursor.execute(executable)
        result = self.cursor.fetchone()
        print(result)

Master = SQLMaster()

#Master.selectElems(False)

'''
myList = [
    ("lll",678,"nice","nc.jpg"),
    ("090909",890,"degil","yt.jpg")
]

Master.insertElem(myList)
'''

#Master.selectByID(3)
#Master.getByOrder()
Master.getInfo()
