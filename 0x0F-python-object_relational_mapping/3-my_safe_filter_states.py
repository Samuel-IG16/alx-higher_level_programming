#!/usr/bin/python3
"""Display name argument of states table"""
import MySQLdb
import sys


def filter_names_safe():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                    ORDER BY id ASC".format(sys.argv[4]))
        rows = cur.fetchall()
        for i in rows:
            print(i)

        cur.close()
        db.close()
    else:
        return

if __name__ == "__main__":
    filter_names_safe()
