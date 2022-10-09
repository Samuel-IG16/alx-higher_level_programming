#!/usr/bin/python3
"""Displays all cities of arguments state"""
import MySQLdb
import sys


def list_cities():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cur = db.cursor()

        cur.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(sys.argv[4]))

        rows = cur.fetchall()

        res = []
        for i in rows:
            res.append(i[0])

        print(", ".join(res))

        cur.close()
        db.close()

if __name__ == "__main__":
    list_cities()
