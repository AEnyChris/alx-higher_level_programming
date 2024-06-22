#!/usr/bin/python3
"""This module queries the states table
and lists all its content according to condition
"""

import sys
import MySQLdb
import re


def query_state(user, passwd, db, state_name):
    """queries the state table to return all states"""
    pattern = r'^[A-Z][a-z]+$'
    if re.match(pattern, state_name):
        db = MySQLdb.connect(
                host="localhost",
                port=3306, user=user,
                passwd=passwd,
                db=db)

        cur = db.cursor()

        cur.execute(
            "SELECT * FROM states\
            WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(state_name))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    query_state(args[0], args[1], args[2], args[3])
