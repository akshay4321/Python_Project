import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db


def booking_list_admin(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute("SELECT booking_id,hotel_name,package_name,name,from_date,to_date,total_amount FROM Booking b LEFT JOIN Hotel h ON h.hotel_id = b.hotel_id LEFT JOIN Package p ON p.package_id = b.package_id LEFT JOIN Customer c ON c.customer_id = b.customer_id")
        conn.commit()
        result = cur.fetchall()

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("Id \t Hotel Name  \t\t\t Package Name \t\t\t Customer Name \t\t From Date \t\t To Date \t\t Total Amount  ")
        print("-------------------------------------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t", row[1], "\t\t\t", row[2], "\t\t\t", row[3], "\t\t", row[4], "\t\t", row[5], "\t\t", row[6])

        print("*************************************************************************************************************************")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



