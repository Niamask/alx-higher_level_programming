#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of 
that state, database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    if (len(sys.argv) == 5):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        sql = "SELECT cities.name FROM cities INNER \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE '{}' ORDER BY \
        cities.id".format(sys.argv[4])
        cur.execute(sql)
        query_rows = cur.fetchall()
        _len = len(query_rows)
        if _len != 0:
            for i in range(_len - 1):
                print("{}, ".format(query_rows[i][0]), end="")
            print(query_rows[_len-1][0])
        cur.close()
        conn.close()
