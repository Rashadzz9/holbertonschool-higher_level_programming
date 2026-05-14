#!/usr/bin/python3
"""This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name = sys.argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE NAME = %s ORDER BY id ASC",
                   (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
