import mysql.connector

config = {
  'user': 'ienac',
  'password': 'ienac',
  'host': 'localhost',
  'database': 'test_ienac',
  'raise_on_warnings': True
    }

#connexion à la base de données
def connect_BD():
    try:
        cnx = mysql.connector.connect(**config)
        cnx.autocommit=False
        print("connexion ok")
    except:
        print("Something is wrong with your user name or password")
    return cnx


def close_BD(cursor,cnx):
    cursor.close()
    cnx.close()

#insertion dans la table commentaires
def insertComment(name='',email='',message=''):
    cnx=connect_BD()
    query = ("INSERT INTO `test_ienac`.`commentaires` (nom, comment, email) VALUES (%s, %s, %s);")
    param=(name, message, email)
    try:
        cursor = cnx.cursor()
        cursor.execute(query, param)
        cnx.commit()
    except:
        cnx.rollback()
    close_BD(cursor,cnx)

#Affichage de la table commentaires
def affichComment():
    cnx=connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id, nom, comment, email FROM `test_ienac`.`commentaires` ")
    cursor.execute(query)
    liste=list(cursor)
    close_BD(cursor,cnx)
    return liste