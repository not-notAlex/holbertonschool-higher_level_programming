#!/usr/bin/python3
"""
module for task 5
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states
                   INNER JOIN cities ON states.id = cities.state_id
                   WHERE states.name LIKE %s
                   ORDER BY cities.id ASC""", (argv[4],))
    sep = ""
    for row in cur.fetchall():
        print(sep, end="")
        print(row[0], end="")
        sep = ", "
    print()
    cur.close()
    db.close()
