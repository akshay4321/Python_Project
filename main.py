import sqlite3
import pandas as panda
import database as db
import location as l
import package as p
import specific_requirenment as s
import booking_admin as b
import hotel as h
import customer as c
import book_package as book
import book_hoel as b_hotel
import report as r

crypto_password = ""
file_contact = panda.read_excel("en_dn/chyper-code.xlsx")

data = file_contact.values.tolist()


def menu():
    print('1) SignUp')
    print('2) Login')
    print('3) Exit')


def adminmenu():
    print('1) Location')
    print('2) Hotel')
    print('3) Package')
    print('4) Specific Requirements List')
    print('5) Manage Customer')
    print('6) Booking Details')
    print('7) Reports')
    print('8) Home')

def usermenu():
    print('1) View Packages')
    print('2) View Hotel')
    print('3) Specific Requirements Package')
    print('4) My Bookings')
    print('5) Home')



error_entry = True
admin_error_entry = True
user_error_entry = True

validate = "False"

if __name__ == '__main__':
    con=db.database_creation(r"Data\rackDB.db")

connection = sqlite3.connect(r"Data\rackDB.db")
cursor = connection.cursor()

while error_entry:
    print("******************************************")
    print("Welcome to RACK Travel Booking Systems")
    print("******************************************")
    menu()

    try:
        option = int(input("Enter Your Option:- "))
    except ValueError:
        continue
    else:
        error_entry = "true"

    if option == 1:

        while validate:
            try:
                print("******************************************")
                name = input("Enter Your Name:- ")
                email = input("Enter New User Email Id:- ")
                password = input("Enter Your Password:- ")
                print("******************************************")
                password = password.upper()

                for i in password:
                    for sheet_cryp_data in data:
                        if i == str(sheet_cryp_data[0]):
                            crypto_password = crypto_password + str(sheet_cryp_data[1])

                cursor.execute("select count(*) from Customer WHERE email_id = '" + email + "' ")
                cur_result = cursor.fetchone()

                count = cur_result[0]
                if count > 0:
                    print("******************************************")
                    print("Email Id is already taken\n")
                    print("******************************************")
                    continue
                else:

                    cursor.execute(
                        "INSERT INTO Customer (name,email_id,password,password_text) values ('" + name + "','" + email + "','" + crypto_password + "','" + password + "');")
                    cursor.execute("COMMIT;")
                    print("\n")

                    crypto_password = ""
                    print("******************************************")
                    print("Customer Create Successfully!")
                    print("******************************************\n")

            except ValueError:
                print("Error:Please Enter proper Input\n")
                continue
            else:
                break

    elif option == 2:

        while validate:
            try:
                email = input("Enter Email Id for Sign In:- ")
                password = input("Enter Paasword for Sign In:- ")

                password = password.upper()

                for i in password:
                    for sheet_cryp_data in data:
                        if i == str(sheet_cryp_data[0]):
                            crypto_password = crypto_password + str(sheet_cryp_data[1])

                cursor.execute(
                    "select * from Customer WHERE email_id = '" + email + "' AND password = '" + crypto_password + "' ")
                cur_result = cursor.fetchone()

                if cur_result:

                    if cur_result[2] == "admin@gmail.com" and cur_result[4] == "admin123":
                        print("******************************")
                        print("Welcome To Admin Panel")
                        print("******************************\n")
                        while admin_error_entry:

                            adminmenu()

                            try:
                                adminoption = int(input("Enter Your Option To perform Admin Task:- "))
                            except ValueError:
                                continue
                            else:
                                admin_error_entry = "true"

                            if adminoption == 1:
                                l.location_main()
                                # print("Location Task")
                            elif adminoption == 2:
                                h.hotel_main()
                            elif adminoption == 3:
                                p.package_main()
                                # print("Package Task")
                            elif adminoption == 4:
                                s.display_specific_requirenment(r"Data\rackDB.db")
                            elif adminoption == 5:
                                c.Customer_main()
                            elif adminoption == 6:
                                b.booking_list_admin(r"Data\rackDB.db")
                            elif adminoption == 7:
                                r.main_reports()
                            else:
                                break
                    else:
                        print("******************************")
                        print("Welcome To User Panel")
                        print("******************************")
                        print("Welcome, " + cur_result[1] + "\n")

                        while user_error_entry:

                            usermenu()

                            try:
                                useroption = int(input("Enter Your Option To perform Customer Task:- "))
                            except ValueError:
                                continue
                            else:
                                user_error_entry = "true"

                            if useroption == 1:
                                # print(cur_result[0])
                                book.package_main(cur_result[0])
                            elif useroption == 2:
                                b_hotel.package_main(cur_result[0])
                            elif useroption == 3:
                                s.insert_specific_requirenment(r"Data\rackDB.db",cur_result[0])
                                # print("Specific Requirments")
                            elif useroption == 4:
                                book.booking_view(r"Data\rackDB.db",cur_result[0])
                            else:
                                break

                    crypto_password = ""
                    break;
                else:
                    print("\n")
                    print("********** Email Id and Paasword Does Not Match ! **********\n")
                    crypto_password = ""
                    continue
            except ValueError:
                print("Error:Please Enter proper Values\n")
                continue
            else:
                break
    elif option == 3:
        break
