#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

database_name = 'StockTracker'
user_name = 'funkynunu'
userpw = 'thefunky1'

con = None

try:
     
    con = psycopg2.connect(database=database_name, user=user_name, password=userpw)
# stocks    
    cur = con.cursor()
    SQL = "DELETE FROM stocks"

# dividend
    cur.execute(SQL)
    SQL = "DELETE FROM dividendhistory"

# price
    cur.execute(SQL)
    SQL = "DELETE FROM pricehistory"

# log
    cur.execute(SQL)
    SQL = "DELETE FROM log"

    cur.execute(SQL)
    con.commit()
   
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)

except IOError, e:    

    if con:
        con.rollback()

    print 'Error %s' % e   
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
