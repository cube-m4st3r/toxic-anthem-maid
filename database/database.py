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
        password=os.getenv("DB.PW"),
        port=os.getenv("DB.PORT"),
        database=os.getenv("DB")
    )

    global cursor
    cursor = mydb.cursor()

    if mydb.is_connected():
        return True
    else:
        return False


def insert_role(role_id, role_name):
    sql = "INSERT INTO role VALUES(%s, %s)"
    val = str(role_id), role_name
    cursor.execute(sql, val)
    mydb.commit()


def check_role(role_id):
    sql = "SELECT role_id FROM role WHERE role_id = %s"
    val = str(role_id)
    cursor.execute(sql, (val,))
    cursor.fetchall()
    if cursor.rowcount == 0:
        return False
    else:
        return True


def check_role_menu_embed(menu_embed_id):
    sql = "SELECT menu_embed_id FROM embed WHERE menu_embed_id = %s"
    val = str(menu_embed_id)
    cursor.execute(sql, (val,))
    cursor.fetchall()
    if cursor.rowcount == 0:
        return False
    else:
        return True