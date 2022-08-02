import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
def insert_hotel(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    location_id_exists=False
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Location")
        print("------------------------------------------------------------------------------------------")
        print("Location_Id \t Name \t Province \t Country \t Postal Code ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[1], "\t\t", row[2], "\t", row[3], "\t", row[4])
        location_id=int(input("Enter location_id from above locations:- "))
        for row in result:
            if row[0]== location_id:
                location_id_exists=True
                break

        if location_id_exists:
            hotel_name=input("Enter hotel name:- ")
            description = input("Enter description about hotel:- ")
            price=float(input("Enter price:-"))
            total_number_room = int(input("Enter total number of room:-"))
            create_updateDate = datetime.now()
            delete_status=0
            cur.execute("INSERT INTO Hotel(location_id,hotel_name,description,price,total_number_rooms,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?,?)",(location_id,hotel_name,description,price,total_number_room,create_updateDate,create_updateDate,delete_status))
            conn.commit()
            print("Data inserted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def update_hotel(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Hotel")
        print("------------------------------------------------------------------------------------------")
        print("Hotel_Id \t Name \t Price \t Description \t Total_number_room ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[2], "\t\t\t", row[3], "\t\t", row[4], "\t", row[6], "\t", row[5])

        hotel_id=input("Enter hotel Id:- ")
        result = db.select_table(r"Data\rackDB.db", "Location")
        print("------------------------------------------------------------------------------------------")
        print("Location_Id \t Name \t Province \t Country \t Postal Code ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[1], "\t\t", row[2], "\t", row[3], "\t", row[4])
        location_id = int(input("Enter location_id from above locations:- "))
        for row in result:
            if row[0] == location_id:
                location_id_exists = True
                break

        if location_id_exists:
            hotel_name = input("Enter hotel name:- ")
            description = input("Enter description about hotel:- ")
            price = float(input("Enter price:-"))
            total_number_room = int(input("Enter total number of rooms:-"))

            update_Date = datetime.now()
            cur.execute("select * from Hotel where hotel_id=" + hotel_id)
            results = cur.fetchall()
            print(len(results))
            if len(results) > 0:
                cur.execute(
                    "UPDATE Hotel SET location_id=?,hotel_name=?,description=?,price=?,total_number_rooms=?,update_datetime=? WHERE hotel_id=?",
                    (location_id, hotel_name, description, price,total_number_room,update_Date,hotel_id))
                conn.commit()
                print("Hotel updated successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_hotel(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        hotel_id=input("Enter Hotel ID which you want to delete:-")
        update_Date = datetime.now()
        delete_status=1
        cur.execute("select * from Hotel where hotel_id="+hotel_id)
        results=cur.fetchall()
        print(len(results))
        if len(results) > 0:
            cur.execute("UPDATE Hotel SET delete_status=?,update_datetime=? WHERE hotel_id=?",(delete_status,update_Date,hotel_id))
            conn.commit()
            print("Hotel deleted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def hotel_main():
    repeate= True
    while repeate != False:
        try:
            result= db.select_table(r"Data\rackDB.db","Hotel")
            print("------------------------------------------------------------------------------------------")
            print("hotel_id \t Name \t Description \t Price\t Total_number_rooms ")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0],"\t\t\t",row[2],"\t\t\t",row[3],"\t\t",row[4],"\t", row[6],"\t",row[5])
            print("******************************************************************************************")
            print("1. Insert \n2. Update \n3. Delete \n4. Home")
            print("******************************************************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                insert_hotel(r"Data\rackDB.db")
            elif choice==2:
                update_hotel(r"Data\rackDB.db")
            elif choice==3:
                delete_hotel(r"Data\rackDB.db")
            elif choice==4:
                print("Go to Home")
                repeate=False
                break
            else:
                check=[1,2,3,4]
                if choice not in check:
                    repeate=False
                    print("Choose from given option only")
                    break
        except ValueError:
            print("Choose from given option only!!")
            continue

# hotel_main()

