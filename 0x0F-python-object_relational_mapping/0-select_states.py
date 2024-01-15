#!/usr/bin/python3
"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
