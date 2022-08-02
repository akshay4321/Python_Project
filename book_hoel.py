import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
def insert_hotel(db_file, customer_id):
    """ create a database connection to a SQLite database """
    conn = None
    hotel_id_exists=False
    #package_id_exists = False
    total_amount=0
    hst = 0
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Hotel")
        print("------------------------------------------------------------------------------------------")
        print("Hotel_Id \t Name \t Description \t Price  ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[2], "\t\t", row[3], "\t", row[4])
        hotel_id=int(input("Enter Hotel_id from above Hotel:- "))
        for row in result:
            if row[0]== hotel_id:
                hotel_id_exists=True
                break


        if hotel_id_exists:
            from_date=input("Enter from date (must be in YYYY-MM-DD):- ")
            from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = input("Enter to date (must be in YYYY-MM-DD):- ")
            to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
            create_updateDate = datetime.now()
            delete_status=0
            cur.execute("INSERT INTO Booking(hotel_id,customer_id,from_date,to_date,total_amount,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?,?)",(hotel_id,customer_id,from_datetime,to_datetime,total_amount,create_updateDate,create_updateDate,delete_status))
            conn.commit()
            print("booking is done successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def booking_view(db_file, customer_id):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()

        result = cur.execute("SELECT booking_id, hotel_name, name, from_date, to_date, total_amount FROM Booking b LEFT JOIN Hotel h ON h.hotel_id = b.hotel_id LEFT JOIN Customer c ON c.customer_id = b.customer_id WHERE b.customer_id=" + str(
             customer_id) + " AND b.delete_status=0")
        print("----------------------------------------------------------------------------------------------------------------")

        print("Booking_Id \t Hotel  \t Customer \t\t From_date \t\t\t to_date \t\t\t Total_amount ")
        print("-----------------------------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[1], "\t", row[2], "\t", row[3], "\t", row[4], "\t", row[5], "\t", row[6])

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def package_main(customer_id):
    repeate= True
    while repeate != False:
        try:
            #booking_view(r"Data\rackDB.db",customer_id)
            print("*****************************************************")
            print("1. Book Hotel \n4. Home")
            print("*****************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                insert_hotel(r"Data\rackDB.db",customer_id)
            elif choice==2:
                print("Go to Home")
                repeate=False
                break
            else:
                check=[1,2]
                if choice not in check:
                    repeate=False
                    print("Choose from given option only")
                    break
        except ValueError:
            print("Choose from given option only!!")
            continue

package_main(3)

