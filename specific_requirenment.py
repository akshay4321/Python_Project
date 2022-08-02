import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db


def insert_specific_requirenment(db_file,customer_id):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        description = input("Enter Your Specific Package Requirements Description:- ")
        request_status = 0
        customer_id = customer_id
        create_updateDate = datetime.now()
        delete_status = 0
        cur.execute(
            "INSERT INTO Specific_requirement_request(customer_id,description,request_status,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?)",
            (customer_id, description, request_status, create_updateDate, create_updateDate, delete_status))
        conn.commit()
        print("***********************************************")
        print("Specific Requirements inserted successfully....")
        print("***********************************************")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def display_specific_requirenment(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute("SELECT require_request_id,name,description FROM Specific_requirement_request s JOIN Customer c ON s.customer_id = c.customer_id where s.delete_status=0")
        conn.commit()
        result = cur.fetchall()

        print("------------------------------------------------------------------------------------------")
        print("Id \t Customer Name \t\t Description  ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t", row[1], "\t\t", row[2])

        print("*******************************************************************************************")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



