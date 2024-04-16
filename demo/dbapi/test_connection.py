# Test connection

import sqlite3
from dbutil import DBNAME

try:
    con = sqlite3.connect(DBNAME)
    print("Connected Successfully!")
    con.close()
except Exception as ex:
    print('Error :', ex)

