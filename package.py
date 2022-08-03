import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
def insert_package(db_file):
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
            package_name=input("Enter package name:- ")
            description = input("Enter description name:- ")
            price=float(input("Enter price:-"))
            total_number_package = int(input("Enter total number of packages:-"))
            package_type = input("Enter package type:- ")
            create_updateDate = datetime.now()
            delete_status=0
            cur.execute("INSERT INTO Package(location_id,package_name,description,price,total_number_package,package_type,createdate_time,update_datetime,delete_status) values(?,?,?,?,?,?,?,?,?)",(location_id,package_name,description,price,total_number_package,package_type,create_updateDate,create_updateDate,delete_status))
            conn.commit()
            print("Data inserted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def update_package(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        result = db.select_table(r"Data\rackDB.db", "Package")

        print("------------------------------------------------------------------------------------------")
        print("Package_Id \t Name \t Price \t Package Type \t Total_number_package ")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0],"\t\t\t",row[2],"\t\t",row[4],"\t", row[6],"\t",row[5])
        package_id=input("Enter package ID:- ")
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
            package_name = input("Enter package name:- ")
            description = input("Enter description name:- ")
            price = float(input("Enter price:-"))
            total_number_package = int(input("Enter total number of packages:-"))
            package_type = input("Enter package type:- ")
            update_Date = datetime.now()
            cur.execute("select * from Package where package_id=" + package_id)
            results = cur.fetchall()
            print(len(results))
            if len(results) > 0:
                cur.execute(
                    "UPDATE Package SET location_id=?,package_name=?,description=?,price=?,total_number_package=?,package_type=?,update_datetime=? WHERE package_id=?",
                    (location_id, package_name, description, price,total_number_package,package_type,update_Date,package_id))
                conn.commit()
                print("Package updated successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_package(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        package_id=input("Enter Package ID which you want to delete:-")
        update_Date = datetime.now()
        delete_status=1
        cur.execute("select * from Package where package_id="+package_id)
        results=cur.fetchall()
        print(len(results))
        if len(results) > 0:
            cur.execute("UPDATE Package SET delete_status=?,update_datetime=? WHERE package_id=?",(delete_status,update_Date,package_id))
            conn.commit()
            print("Package deleted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def package_main():
    repeate= True
    while repeate != False:
        try:
            result= db.select_table(r"Data\rackDB.db","Package")
            print("------------------------------------------------------------------------------------------")
            print("Package_Id \t Name \t Price \t Package Type \t Total_number_package ")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0],"\t\t\t",row[2],"\t\t",row[4],"\t", row[6],"\t",row[5])
            print("*****************************************************")
            print("1. Insert \n2. Update \n3. Delete \n4. Home")
            print("*****************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                insert_package(r"Data\rackDB.db")
            elif choice==2:
                print("2")
                update_package(r"Data\rackDB.db")
            elif choice==3:
                delete_package(r"Data\rackDB.db")
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

# package_main()

