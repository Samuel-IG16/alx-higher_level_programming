#!/usr/bin/python3
"""List all states where 'name' matches the argument
Username, password, database name, and state name given as user args
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name LIKE BINARY '{}'
         ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
