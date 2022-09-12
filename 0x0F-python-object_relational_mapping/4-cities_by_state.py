#!/usr/bin/python3
"""List all cities from the db
Username, password, and database name given as user args
Can only use execute() once
Sort ascending order by cities.id
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
    cmd = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    cur.execute(cmd)
    allCities = cur.fetchall()

    for city in allCities:
        print(city)

    cur.close()
    db.close()
