import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor
import os

cursor: MySQLCursor | CMySQLCursor = NotImplemented
mydb = None

async def init_database():
    global mydb
    mydb = mysql.connector.connect(
        host=os.getenv("DB.HOST"),
        user=os.getenv("DB.USER"),
        password=os.getenv("DB.PW")
    )

    global cursor
    cursor = mydb.cursor()

    if mydb.is_connected():
        return True
    else:
        return False