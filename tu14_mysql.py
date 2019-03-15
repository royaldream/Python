import mysql.connector
# from tu10_class import Student1

"""
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd=''
)"""


# print mydb.connect()

# Crete Database
def creteDataBase():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd=''
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE pythonDatabase")


# Show DataBases
def showDatabase():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd=''
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='pythonDatabase'
)
mycursor = mydb.cursor()


# Crete Table
# mycursor.execute("Create Table Student (name Text,enrollment Text)")
def getData():
    a = raw_input()
    b = raw_input()
    return a, b


def insertData(name, enrollment):
    sql = "INSERT INTO student (name, enrollment) VALUES (%s, %s)"
    val = (name, enrollment)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def choice():
    return int(input())


def insertChoice():
    while choice() != 0:
        name, enrollment = getData()
        insertData(name, enrollment)

def showData():
    mycursor.execute("SELECT * FROM student")

    myresult = mycursor.fetchall()

    for x in myresult:
        print x[0], x[1]

showData()