import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db

def insert_package(db_file, customer_id):
    """ create a database connection to a SQLite database """
    conn = None
    hotel_id_exists=False
    package_id_exists = False
    total_amount=0
    hst = 0
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Location")
        print("Packages can be selected based on their location")
        print("------------------------------------------------------------------------------------------")
        print("Location_Id \t Name \t Province \t Country \t Postal Code ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[1], "\t\t", row[2], "\t", row[3], "\t", row[4])
        location_id = input("Enter location_id from above location list:- ")

        result = cur.execute("SELECT * FROM Hotel WHERE location_id="+location_id)
        print("Select Hotel for Booking Package")
        print("------------------------------------------------------------------------------------------")
        print("Hotel_Id \t Name \t Description \t Price  ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[2], "\t\t", row[3], "\t", row[4])
        hotel_id=int(input("Enter Hotel Id from above Hotel list:- "))
        for row in result:
            if row[0]== hotel_id:
                hotel_id_exists=True
                break
        result_package = cur.execute("SELECT * FROM Package WHERE location_id="+location_id)
        print("------------------------------------------------------------------------------------------")
        print("Package_Id \t Name \t Description \t Price  ")
        print("------------------------------------------------------------------------------------------")
        for row in result_package.fetchall():
            print(row[0], "\t\t\t", row[2], "\t\t", row[3], "\t", row[4])
        package_id = int(input("Enter package_id from above Package:- "))
        result_package_id = cur.execute("SELECT * FROM Package WHERE package_id=" + str(package_id))
        package=result_package_id.fetchone()
        if package:
            hst = (package[4] * (13 / 100))
            total_amount = package[4] + hst
            from_date = input("Enter from date (must be in YYYY-MM-DD):- ")
            from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = input("Enter to date (must be in YYYY-MM-DD):- ")
            to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
            create_updateDate = datetime.now()
            delete_status = 0

            cur.execute(
                "INSERT INTO Booking(hotel_id,package_id,customer_id,from_date,to_date,total_amount,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?,?,?)",
                (hotel_id, package_id, customer_id, from_datetime, to_datetime, total_amount, create_updateDate,
                 create_updateDate, delete_status))
            conn.commit()
            print("******************************************")
            print("Package Booking Completed Successfully....")
            print("******************************************")
        else:
            print("Package does not exist!!!")
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
        result = cur.execute("SELECT booking_id, hotel_name, package_name, name, from_date, to_date, total_amount FROM Booking b LEFT JOIN Hotel h ON h.hotel_id = b.hotel_id LEFT JOIN Package p ON p.package_id = b.package_id LEFT JOIN Customer c ON c.customer_id = b.customer_id WHERE b.customer_id="+str(customer_id)+" AND b.delete_status=0")
        print("My Booking List")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("Booking_Id \t Hotel \t\t\t\t\t Package \t Customer \t\t From_date \t\t\t\t to_date \t\t\t Total_amount ")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[1], "\t", row[2], "\t", row[3], "\t\t", row[4], "\t\t\t", row[5], "\t", row[6] )
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def package_main(customer_id):
    repeate= True
    while repeate != False:
        try:
            # booking_view(r"Data\rackDB.db",customer_id)

            print("******** Package List ********")
            result=db.package_data(r"Data\rackDB.db","Package")
            print("------------------------------------------------------------------------------------------")
            print("Package Id \t Location Name \t\t Package Name \t Description \t\t Price  ")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0], "\t\t\t", row[1], "\t\t", row[2],"\t\t", row[3], "\t", row[4])

            print("*****************************************************************************************************************")
            print("1. Book Packages \n2. Home")
            print("*****************************************************************************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                insert_package(r"Data\rackDB.db",customer_id)
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

# package_main(3)

