from datetime import datetime as dt
import mysql.connector as connector

class Student:
    stConnector = connector.connect(
    host = "localhost",
    user = "root",
    password = "farukefesql1234",
    database = "node-app"
    )
    stCursor = stConnector.cursor()

    def __init__(self,number:int,name:str,surname:str,bd:dt,gender:str):
        self.number = number
        self.name = name
        self.surname = surname
        self.bd = bd
        self.gender = gender

    def saveStudent(self):
        table = "INSERT INTO students (stNumber,name,surname,bd,gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.number,self.name,self.surname,self.bd,self.gender)
        self.stCursor.execute(table, value)

        try:
            self.stConnector.commit()
            print("Student added to the databank.")
        except connector.Error as err:
            print(f"An error has occured: {err}")
        finally:
            self.stConnector.close()
    
    @staticmethod # Lets you define methods not containing the 'self' parameter
    def saveStudents(students):
        table = "INSERT INTO students (stNumber,name,surname,bd,gender) VALUES (%s,%s,%s,%s,%s)"
        Student.stCursor.executemany(table, students)

        try:
            Student.stConnector.commit()
            print("Student(s) added to the databank.")
        except connector.Error as err:
            print(f"An error has occured: {err}")
        finally:
            Student.stConnector.close()

sts = [
    (11362,'Faruk Efe','Yencilek',dt(2018,8,4),"Male"),
    (348,'Fruq F','Ync',dt(2004,1,26),"Male")
]

mySt = Student(7,"DN","KBK",dt(1971,12,11),"Female")
mySt.saveStudents(sts)