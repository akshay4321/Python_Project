import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import sqlite3

def connection():
    #query = "select * from Customer;"
    conn= sqlite3.connect(r"Data\rackDB.db")
    # print(sqlite3.version)

    cur = conn.cursor()
    # print("connection success..")
    #cur.execute("create table demo(demo_id INTEGER primary key autoincrement not null,name varchar(50) not null)")
    cur.execute("select * from Customer")
    conn.commit()
    #print("table is created..")

    #results = cur.fetchall()
    #for row in results:
     #   print(row)
    return conn

def report1():
    conn = connection()
    #df=cur.execute("select * from Customer")
    #connection()
    df=pd.read_sql_query("select sum(total_amount) as total_booking_amount,package_name from Booking b left join Package p on p.package_id=b.package_id where b.package_id IS NOT NULL  group by p.package_id",conn)

    #df=row
    df.head()
    fig = plt.figure(figsize=(5,4))
    axis = fig.add_axes([0,0,1,1])
    #df["package_name"]
    axis.pie(df["total_booking_amount"],labels=df["package_name"],
            autopct='%.1f%%')
    axis.set_title('Package wise total booking amount', size=15, pad=10)
    plt.show()

def report2():
    conn=connection()
    df1=pd.read_sql_query("select count(hotel_id) as hotel_count,name from Booking as b LEFT JOIN Customer as c on c.customer_id = b.customer_id where hotel_id is NOT NULL group by b.customer_id",conn)
    #df=row
    df1.head()

    #----------------Report 2:-Customer wise total hotel booking  ----------------------------------
    fig = plt.figure(figsize=(5,4))
    axis = fig.add_axes([0,0,1,1])
    #df["package_name"]
    axis.pie(df1["hotel_count"],labels=df1["name"],
            autopct='%.1f%%')
    axis.set_title('Customer wise total hotel booking', size=15, pad=10)
    plt.show()

def report3():
    #----------------Report 3:-  --------------------
    conn = connection()
    df2=pd.read_sql_query("SELECT count(*) as 'number_of_hotels',l.location_name as 'location_name' from Hotel h JOIN Location l on h.location_id=l.location_id group by h.location_id",conn)
    df2.head()
    fig = plt.figure(figsize=(5,4))
    axis = fig.add_axes([0,0,1,1])
    #df["package_name"]
    axis.pie(df2["number_of_hotels"],labels=df2["location_name"],
            autopct='%.1f%%')
    axis.set_title('location wise total number of hotels', size=15, pad=10)
    # show plot
    plt.show()

def main_reports():
    repeate = True
    while repeate != False:
        try:
            connection()
            print("*****************************************************")
            print(" 1. Package wise total booking amount \n 2. Customer wise total hotel booking \n 3. location wise total number of hotels \n 4.Home")
            print("*****************************************************")
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                report1()
            elif choice == 2:
                report2()
            elif choice == 3:
                report3()
            elif choice == 4:
                print("Go to Home")
                repeate = False
                break
            else:
                check = [1, 2, 3, 4]
                if choice not in check:
                    repeate = False
                    print("Choose from given option only")
                    break
        except ValueError:
            print("Choose from given option only!!")
            continue

# main_reports()