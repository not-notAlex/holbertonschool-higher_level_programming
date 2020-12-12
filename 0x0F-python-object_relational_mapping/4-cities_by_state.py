#!/usr/bin/python3
"""
module for task 4
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
    cur.execute("""SELECT cities.id, cities.name, states.name FROM states
                   INNER JOIN cities ON states.id = cities.state_id
                   ORDER BY cities.id ASC""")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
