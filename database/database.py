import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor
import os

from classes.roles import Roles

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


def insert_menu_embed(menu_embed_id, message_id, embed_title: None, embed_description: None):
    sql = "INSERT INTO menu_embed VALUES(%s, %s, %s, %s)"
    val = menu_embed_id, message_id, embed_title, embed_description
    cursor.execute(sql, val)
    mydb.commit()


def insert_role_menu_embed(role_id, menu_embed_id, role_description: None):
    sql = "INSERT INTO role_menu_embed VALUES(%s, %s, %s)"
    val = role_id, menu_embed_id, role_description
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
    sql = "SELECT menu_embed_id FROM menu_embed WHERE menu_embed_id = %s"
    val = str(menu_embed_id)
    cursor.execute(sql, (val,))
    cursor.fetchall()
    if cursor.rowcount == 0:
        return False
    else:
        return True


def load_embed_menu_roles(menu_embed_id):
    sql = "SELECT role_role_id, role_name FROM role_menu_embed rme JOIN role r ON rme.role_role_id = r.role_id WHERE embed_menu_embed_id = %s"
    val = menu_embed_id
    cursor.execute(sql, val)
    res = cursor.fetchall()

    retval = list()

    for ctx in res:
        role = Roles()
        if role.get_role_id(ctx[0]):
            retval.append(role)
        else:
            role = Roles(ctx[0], ctx[1])
            retval.append(role)

    return retval


#def load_embed_menus():
#   sql = "SELECT * FROM "