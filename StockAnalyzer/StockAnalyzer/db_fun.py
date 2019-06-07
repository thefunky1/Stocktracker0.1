import psycopg2
import sys
import datetime

database_name = 'StockTracker'
user_name = 'funkynunu'
userpw = 'thefunky1'

def connect_db(con):
    try:
        return psycopg2.connect(database=database_name, user=user_name, password=userpw)
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        

def extract_stocks():
    con = None
    con = connect_db(con)
    try:
        cur = con.cursor()
        SQL = "SELECT * FROM stocks;"
        cur.execute(SQL)
        content = cur.fetchall()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()

    return content

def extract_pricehistory(symbol):
    con = None
    con = connect_db(con)
    try:
        cur = con.cursor()
        SQL = "SELECT * FROM pricehistory WHERE symbol = '" + symbol + "'"
        cur.execute(SQL)
        content = cur.fetchall()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()

    return content

def insert_stocks(symbol,stockname):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO stocks (symbol, stockname) VALUES (%s, %s)"
        cur.execute(SQL, (symbol,stockname))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_multi_stocks(stockdata):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO stocks (symbol, stockname) VALUES (%(symbol)s, %(stockname)s)"
        cur.executemany(SQL, stockdata)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def update_stocks(symbol,stockname):
    # Note: if the symbol is not present in the stocks table, there will be NO change to the table
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "UPDATE stocks SET stockname = %s WHERE symbol = %s"
        cur.execute(SQL, (stockname,symbol))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def delete_stocks(symbol):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "DELETE FROM stocks WHERE symbol = '" + symbol + "'"
        cur.execute(SQL)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_dividendhistory(symbol,date,amount):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO dividendhistory (symbol, date, amount) VALUES (%s, %s, %s)"
        cur.execute(SQL, (symbol,date,amount))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_multi_dividendhistory(stockdata):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO dividendhistory (symbol, date, amount) VALUES (%(symbol)s, %(date)s, %(amount)s)"
        cur.executemany(SQL, stockdata)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""


def update_dividendhistory(symbol,date,amount):
    # Note: if the symbol is not present in the stocks table, there will be NO change to the table
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "UPDATE dividendhistory SET amount = %s WHERE symbol = %s AND date = %s"
        cur.execute(SQL, (amount,symbol,date))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def delete_dividendhistory(symbol,date):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "DELETE FROM dividendhistory WHERE symbol = '" + symbol + "' AND date = '" + date + "'"
        cur.execute(SQL)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_pricehistory(symbol,date,open,close,high,low,vol):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO pricehistory (symbol, date, open, close, high, low, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(SQL, (symbol,date,open,close,high,low,vol))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_multi_pricehistory(stockdata):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO pricehistory (symbol, date, open, close, high, low, volume) VALUES (%(symbol)s, %(date)s, %(open)s, %(close)s, %(high)s, %(low)s, %(volume)s)"
        cur.executemany(SQL, stockdata)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def update_pricehistory(symbol,date,open,close,high,low,vol):
    # Note: if the symbol is not present in the stocks table, there will be NO change to the table
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "UPDATE pricehistory SET open = %s, close = %s, high = %s, low = %s, volume = %s WHERE symbol = %s AND date = %s"
        cur.execute(SQL, (open,close,high,low,vol,symbol,date))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def delete_pricehistory(symbol,date):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "DELETE FROM pricehistory WHERE symbol = '" + symbol + "' AND date = '" + date + "'"
        cur.execute(SQL)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_stockexchanges(exchange,name,symbol,country):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO stockexchanges (exchange, exchangename, symbol, country) VALUES (%s, %s, %s, %s)"
        cur.execute(SQL, (exchange,name,symbol,country))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_multi_stockexchanges(stockdata):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO stockexchanges (exchange, exchangename, symbol, country) VALUES (%(exchange)s, %(exchangename)s, %(symbol)s, %(country)s)"
        cur.executemany(SQL, stockdata)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def update_stockexchanges(exchange,exchangename,symbol,country):
    # Note: if the symbol is not present in the stocks table, there will be NO change to the table
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "UPDATE stockexchanges SET exchange = %s, exchangename = %s, symbol = %s, country = %s"
        cur.execute(SQL, (exchange,exchangename,symbol,country))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def delete_stockexchanges(exchange,symbol):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "DELETE FROM stockexchanges WHERE exchange = '" + exchange + "' AND symbol = '" + symbol + "'"
        cur.execute(SQL)
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return ""

def insert_log(symbol,date,logtype,refid):
    con = None
    con = connect_db(con)

    try:
        cur = con.cursor()
        SQL = "INSERT INTO log (symbol, date, type, refid) VALUES (%s, %s, %s, %s)"
        cur.execute(SQL, (symbol,date,logtype,refid))
        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        if con:
            con.close()
    return

def update_log():
    return

def delete_log():
    return


def insert_websites():
    return

def update_websites():
    return

def delete_websites():
    return


