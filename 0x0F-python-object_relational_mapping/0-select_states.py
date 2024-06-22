#!/usr/bin/python3
"""This module queries the states table
and lists all its content
"""

import sys
import MySQLdb

def query_state(user, passwd, db):
    """queries the state table to return all states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)

    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    query_state(args[0], args[1], args[2])
