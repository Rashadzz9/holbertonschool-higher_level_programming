#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line
    # sys.argv[0] is the script name, so we start from 1
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    # We use localhost and port 3306 as per requirements
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute the query and sort by states.id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print results in the specified format
    for row in rows:
        print(row)

    # Close all connections (Clean up)
    cur.close()
    db.close()
