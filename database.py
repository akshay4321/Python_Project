import sqlite3
from sqlite3 import Error
def database_creation(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Location (location_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, location_name VARCHAR(100) NOT NULL,province VARCHAR(100) NOT NULL,country VARCHAR(100) NOT NULL,postal_code VARCHAR(50) NOT NULL,createdate_time DATETIME NOT NULL,update_datetime DATETIME NOT NULL,delete_status INTEGER NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS Hotel (hotel_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,location_id INTEGER NOT NULL,hotel_name VARCHAR(100) NOT NULL,description VARCHAR(255) NOT NULL,price float NOT NULL,total_number_rooms INTEGER  NOT NULL,createdate_time DATETIME NOT NULL,update_datetime DATETIME NOT NULL,delete_status INTEGER NOT NULL, CONSTRAINT FK_LocationHotel FOREIGN KEY (location_id) REFERENCES Location(location_id))")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Package (package_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,location_id INTEGER NOT NULL,package_name VARCHAR(100) NOT NULL,description VARCHAR(255) NOT NULL,price float NOT NULL,total_number_package INTEGER  NOT NULL,package_type VARCHAR(100) NOT NULL,createdate_time DATETIME NOT NULL,update_datetime DATETIME NOT NULL,delete_status INTEGER NOT NULL, CONSTRAINT FK_LocationHotel FOREIGN KEY (location_id) REFERENCES Location(location_id))")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Specific_requirement_request (require_request_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,customer_id INTEGER NOT NULL,description VARCHAR(255) NOT NULL,request_status VARCHAR(50) NOT NULL,createdate_time DATETIME NOT NULL,update_datetime DATETIME NOT NULL,delete_status INTEGER NOT NULL, CONSTRAINT FK_Customer_requirement FOREIGN KEY (customer_id) REFERENCES Customer(customer_id))")
        cur.execute(
           "CREATE TABLE IF NOT EXISTS Booking (booking_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,hotel_id INTEGER NULL,package_id INTEGER NULL,customer_id INTEGER NOT NULL,from_date DATE NOT NULL,to_date DATE NOT NULL,total_amount FLOAT NOT NULL,createdate_time DATETIME NOT NULL,update_datetime DATETIME NOT NULL,delete_status INTEGER NOT NULL, CONSTRAINT FK_BookingHotel FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id), CONSTRAINT FK_CustomerBooking FOREIGN KEY (customer_id) REFERENCES Customer(customer_id), CONSTRAINT FK_PackageBooking FOREIGN KEY (package_id) REFERENCES Package(package_id))")

        cur.execute("CREATE TABLE IF NOT EXISTS Customer (Customer_Id	INTEGER,name TEXT,email_id TEXT,password TEXT,password_text	TEXT,Create_DateTime TEXT,Update_Date_Time TEXT,Delete_Status INTEGER DEFAULT 0,PRIMARY KEY(Customer_Id AUTOINCREMENT))")
        conn.commit()
        print("Table is created")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def select_table(db_file,table_nm):
    """ Display Table """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute("select * from "+table_nm+" where delete_status=0")
        conn.commit()
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def customer_data_only(db_file,table_nm):
    """ Display Table """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        # cur.execute("select * from "+table_nm+" where delete_status=0")
        cur.execute("SELECT * FROM  "+table_nm+" WHERE customer_id > 1 AND Delete_Status=0")
        conn.commit()
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def package_data(db_file,table_nm):
    """ Display Table """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute("select package_id,location_name,package_name,description,price from Package p LEFT JOIN Location l ON l.location_id = p.package_id where p.delete_status=0")
        conn.commit()
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def hotel_data(db_file,table_nm):
    """ Display Table """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        cur.execute("select hotel_id,location_name,hotel_name,description,price from Hotel h LEFT JOIN Location l ON l.location_id = h.hotel_id where h.delete_status=0")
        conn.commit()
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


