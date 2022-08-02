import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
def insert_location(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        location_name=input("Enter location name:- ")
        province=input("Enter province name:- ")
        country = input("Enter country name:- ")
        postal_code=input("Enter postal code:-")
        create_updateDate = datetime.now()
        delete_status=0
        cur.execute("INSERT INTO Location(location_name,province,country,postal_code,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?)",(location_name,province,country,postal_code,create_updateDate,create_updateDate,delete_status))
        conn.commit()
        print("Data inserted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def update_location(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        locationid=input("Enter location ID which you want to update:-")
        location_name = input("Enter location name:- ")
        province = input("Enter province name:- ")
        country = input("Enter country name:- ")
        postal_code = input("Enter postal code:-")
        update_Date = datetime.now()
        cur.execute("select * from Location where location_id=" + locationid)
        results = cur.fetchall()
        print(len(results))
        if len(results) > 0:
            cur.execute(
                "UPDATE Location SET location_name=?,province=?,country=?,postal_code=?,update_datetime=? WHERE location_id=?",
                (location_name, province, country, postal_code,update_Date,locationid))
            conn.commit()
            print("Location updated successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_location(db_file):
    print("delete")
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        locationid=input("Enter location ID which you want to update:-")
        update_Date = datetime.now()
        delete_status=1
        print(locationid)
        cur.execute("select * from Location where location_id="+locationid)
        results=cur.fetchall()
        print(len(results))
        if len(results) > 0:
            cur.execute("UPDATE Location SET delete_status=?,update_datetime=? WHERE location_id=?",(delete_status,update_Date,locationid))
            conn.commit()
            print("Location deleted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def location_main():
    repeate= True
    while repeate != False:
        try:
            result= db.select_table(r"Data\rackDB.db","Location")
            print("------------------------------------------------------------------------------------------")
            print("Location_Id \t Name \t Province \t Country \t Postal Code ")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0],"\t\t\t",row[1],"\t\t",row[2],"\t", row[3],"\t",row[4])
            print("*****************************************************")
            print("1. Insert \n2. Update \n3. Delete \n4. Home")
            print("*****************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                insert_location(r"Data\rackDB.db")
            elif choice==2:
                update_location(r"Data\rackDB.db")
            elif choice==3:
                delete_location(r"Data\rackDB.db")
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

# location_main()

