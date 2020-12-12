#!/usr/bin/python3
"""
module for task 2
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
    cur.execute("""SELECT * FROM states WHERE name
                   LIKE '{}' ORDER BY id ASC""".format(argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
