# -*- coding: utf-8 -*-

import pymysql.cursors
import pymysql.converters as converters
# Connect to the database
Host = "localhost"
User = 'root'
Password = 'sandi'
DB = 'petdb'
Charset = 'utf8mb4'


def init(host, user, password, db, charset):
    global Host
    global User
    global Password
    global DB
    global Charset
    Host = host
    User = user
    Password = password
    DB = db
    Charset = charset


def connect():
    conv = converters.conversions.copy()
    conv[10] = str  # convert dates to strings
    return pymysql.connect(host=Host,
                           user=User,
                           password=Password,
                           db=DB,
                           charset=Charset,
                           cursorclass=pymysql.cursors.DictCursor,
                           conv=conv)


def updatePet(petId, pet):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            sql = "UPDATE pets set name=%s, species=%s,gender=%s,birthday=%s where id=%s;"
            cursor.execute(sql, (pet['name'], pet['species'], pet['gender'], pet['birthday'], petId))
        connection.commit()
    finally:
        connection.close()


def getPet(petId):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM pets WHERE id=%s"
            cursor.execute(sql, petId)
            result = cursor.fetchone()
    finally:
        connection.close()
    return result


def getPets():
    try:
        connection = connect()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM pets"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
    return result
