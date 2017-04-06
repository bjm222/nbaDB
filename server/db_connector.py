import mysql.connector

def db_connect():
    db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                            user="root",         # your username
                            #passwd="1234566",  # your password
                            passwd="bjmkobe56110839!",
                            db="nba_db")        # name of the data base

    return db
