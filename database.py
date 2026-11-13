import mysql.connector # Allows python enquires to communicate with SQL database 
import os 

def get_connection(): # Establish connection to property management database 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ["MYSQL_PASSWORD"],
        database="property_management"
    )
