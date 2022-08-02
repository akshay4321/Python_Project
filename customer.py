import sqlite3
from sqlite3 import Error
from datetime import datetime
import database as db
import pandas as panda

crypto_password1 = ""
file_contact = panda.read_excel("en_dn/chyper-code.xlsx")
data = file_contact.values.tolist()

def update_customer(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        result = db.customer_data_only(r"Data\rackDB.db", "Customer")
        print("------------------------------------------------------------------------------------------")
        print("Customer_Id \t\t Name \t\t\t Email ID \t\t\t\t Password")
        print("------------------------------------------------------------------------------------------")
        for row in result:
            print(row[0],"\t\t\t\t\t",row[1],"\t\t\t",row[2],"\t\t",row[3])

        Customer_Id=input("Enter Customer Id:- ")
        name = input("Enter Customer name:- ")
        email_id = input("Enter Customer Email ID:- ")
        password = input("Enter your password:-")

        password = password.upper()
        crypto_password1 = ""
        for i in password:
            for sheet_cryp_data in data:
                if i == str(sheet_cryp_data[0]):
                    crypto_password1 = crypto_password1 + str(sheet_cryp_data[1])

        Update_Date_Time = datetime.now()
        cur.execute("select * from Customer where Customer_Id=" + Customer_Id)
        results = cur.fetchall()
        print(len(results))
        if len(results) > 0:
                cur.execute(
                    "UPDATE Customer SET Customer_Id=?,name=?,email_id=?,password=?,password_text=?,Update_Date_Time=? WHERE Customer_Id=?",
                    (Customer_Id, name, email_id,crypto_password1,password,Update_Date_Time,Customer_Id))
                conn.commit()
                print("Customer data updated successfully....")
                crypto_password1 = ""
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_customer(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        Customer_Id=input("Enter Customer ID which you want to delete:-")
        update_Date = datetime.now()
        delete_status=1
        cur.execute("select * from Customer where Customer_Id="+Customer_Id)
        results=cur.fetchall()
        print(len(results))
        if len(results) > 0:
            cur.execute("UPDATE Customer SET Delete_Status=?,Update_Date_Time=? WHERE Customer_Id=?",(delete_status,update_Date,Customer_Id))
            conn.commit()
            print("Customer data deleted successfully....")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def Customer_main():
    repeate= True
    while repeate != False:
        try:
            result= db.customer_data_only(r"Data\rackDB.db","Customer")
            print("------------------------------------------------------------------------------------------")
            print("Customer_Id \t\t Name \t\t\t\t Email ID \t\t\t\t Password")
            print("------------------------------------------------------------------------------------------")
            for row in result:
                print(row[0],"\t\t\t\t\t",row[1],"\t\t\t\t",row[2],"\t\t\t",row[3])
            print("******************************************************************************************")
            print("1. Update \n2. Delete \n3. Home ")
            print("******************************************************************************************")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                update_customer(r"Data\rackDB.db")
            elif choice==2:
                delete_customer(r"Data\rackDB.db")
            elif choice==3:
                print("Go to Home")
                repeate=False
                break
            else:
                check=[1,2,3]
                if choice not in check:
                    repeate=False
                    print("Choose from given option only")
                    break
        except ValueError:
            print("Choose from given option only!!")
            continue

# Customer_main()

