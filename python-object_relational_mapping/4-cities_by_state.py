#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It uses a JOIN to fetch state names for each city.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # 3 arqument qəbul edirik: user, passwd, db
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Yalnız bircə dəfə execute() işlədirik və JOIN sorğusunu yazırıq
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
