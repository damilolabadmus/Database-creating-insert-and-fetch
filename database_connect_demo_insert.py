# first import the mysql connector
import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error


# define the connector function
def connect_insert():
    ''' function to connect and fetch rows in a database '''


# create a variable for the connector object
conn = None

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='firsttable',
        user='damilicious',
        password='Atilola0672')
    print("Connected to the database")

    # cursor variable
    db_cursor = conn.cursor()

    # create a list variable to contain the sql query to be executed
    sql = "INSERT INTO human (HumanId, Name, Color, Gender, Bloodgroup) VALUES (%s, %s, %s, %s, %s)"

    # create a list variable to contain all the values we want to insert into the database
    val = [
         ('1008', 'Hannah', 'White','Female', 'B-'),
         # ('1009', 'Michael', 'Brown','Male', 'B-'),
         # ('1010', 'Sandy', 'Black','Male', 'O-'),
         # ('1011', 'Green', 'Yellow','Male', 'O+'),
         # ('1012', 'Richard', 'Black','Male', 'B+')
        ]

    # Execute the query using the execute many function
    db_cursor.executemany(sql, val)

    # commit to the database
    conn.commit()

    # print a success message
    print(db_cursor.rowcount, "row was inserted.")

    # close the cursor
    db_cursor.close()


except Error as e:
    print('Connection failed due to the following: ', e)
finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print('Disconnected from database')

    # call the function we just created
    connect_insert()
