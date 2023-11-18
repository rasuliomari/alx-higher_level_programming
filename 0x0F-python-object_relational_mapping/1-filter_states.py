#!/usr/bin/python3
"""
lists all states with a name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    MySQL Connection
    """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    [print(row) for row in rows if row[1][0] == "N"]
