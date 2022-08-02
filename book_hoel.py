import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
def insert_hotel(db_file, customer_id):
    """ create a database connection to a SQLite database """
    conn = None
    hotel_id_exists=False
    #package_id_exists = False

    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Hotel")
        print("------------------------------------------------------------------------------------------")
        print("Hotel_Id \t Name \t Description \t Price  ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "\t\t\t", row[2], "\t\t", row[3], "\t", row[4])
        hotel_id=int(input("Enter Hotel_id from above Hotel List:- "))

        result_hotel_id = cur.execute("SELECT * FROM Hotel WHERE hotel_id=" + str(hotel_id))
        hotel = result_hotel_id.fetchone()

        if hotel:
            from_date=input("Enter from date (must be in YYYY-MM-DD):- ")
            from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = input("Enter to date (must be in YYYY-MM-DD):- ")
            to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
            create_updateDate = datetime.now()
            delete_status=0
            hotel_amout = hotel[4]

            from datetime import date
            dt1 = to_date.split("-")
            dt2 = from_date.split("-")

            total_days = date(int(dt1[0]), int(dt1[1]), int(dt1[2])) - date(int(dt2[0]), int(dt2[1]), int(dt2[2]))

            total_days = total_days.days
            total_hotel_amount_daywise = total_days * hotel_amout
            hst = (total_hotel_amount_daywise * (13 / 100))
            total_amount = total_hotel_amount_daywise + hst

            cur.execute("INSERT INTO Booking(hotel_id,customer_id,from_date,to_date,total_amount,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?,?)",(hotel_id,customer_id,from_datetime,to_datetime,total_amount,create_updateDate,create_updateDate,delete_status))
            conn.commit()
            print("**************************************")
            print("Hotel Booking is Done successfully....")
            print("**************************************")
        else:
            print("Hotel does not exist!!!")
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

            print("******** Hotel List ********")
            result = db.hotel_data(r"Data\rackDB.db", "Hotel")
            print("------------------------------------------------------------------------------------------")
            print("Hotel Id \t Location Name \t\t Hotel Name \t Description \t\t Price  ")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0], "\t\t\t", row[1], "\t\t", row[2], "\t\t", row[3], "\t", row[4])

            print("*****************************************************")
            print("1. Book Hotel \n2. Home")
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

# package_main(3)

