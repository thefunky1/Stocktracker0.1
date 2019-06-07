# try http://uk.finance.yahoo.com/lookup/stocks?s=.L&t=S&m=GB&r=&b=980
#     http://uk.finance.yahoo.com/lookup/stocks?s=.L&t=S&b=0&m=GB
import string
import psycopg2
import sys
import urllib
import db_fun

def get_web_links():
    web_links = []
    prefix = "http://uk.finance.yahoo.com/lookup/stocks?s=.L&t=S&m=GB&r=&b="
    postfix = "&LSE.html=Submit"
    #for x in list(string.lowercase):
    #    web_links.append(prefix + x + postfix)
    for x in range(50):
        #web_links.append(prefix + str(x*20) + postfix)
        web_links.append(prefix + str(x*20))
    return web_links

def get_page(url):
    print url
    try:
        return urllib.urlopen(url).read()
    except:
        print "Fail to retreive url"
        return ""

def get_stock_details(links):
    details = {}

    for url in links:
        # get web page
        page = get_page(url)
        
        page = page[page.find('Exchange</a>'):]
        page = page[:page.find('</tbody>')]
        
        # extract data
        while(True):
            detail = []
            
            # exit point
            if page.find('</td></tr>') == -1:
                break
                
            page = page[page.find('href="')+6:]
            detail.append(page[:page.find('"')])#link
            page = page[page.find('>')+1:]
            symbol = page[:page.find('</a></td>')]
            page = page[page.find('</a></td><td>')+13:]
            detail.append(page[:page.find('</td>')])#name
            page = page[page.find('</td><td>')+9:]
            detail.append(page[:page.find('</td>')])#Isin
            page = page[page.find('</td><td')+8:]
            detail.append(page[page.find('>')+1:page.find('</td>')])#Last price
            page = page[page.find('</td><td>')+9:]
            detail.append(page[:page.find('</td><td>')])#Type - 'Stock'
            page = page[page.find('</td><td>')+9:]
            detail.append(page[:page.find('</td></tr>')])#Exchange - 'LSE'
            page = page[page.find('</td></tr>')+10:]
            
            symbol = symbol[:symbol.find('.L')]
            
            details[symbol[:4]] = detail
            
    return details

def update_db(details):
    symbols = []
    symbols_to_upload = []
    for symbol in details.keys():
        symbols.append(symbol)
    
    con = None
    try:
        con = psycopg2.connect(database='StockTracker', user='funkynunu', password='thefunky1')
        cur = con.cursor()

        SQL = """SELECT * FROM stocks"""
        cur.execute(SQL)
        db_records = cur.fetchall()
        
        db_symbols = []
        for db_symbol in db_records:
            db_symbols.append(db_symbol[0].rstrip())

        for symbol in symbols:
            if symbol not in db_symbols:
                symbols_to_upload.append(symbol)

        SQL = "INSERT INTO stocks (stock, stockname) VALUES (%s, %s)"
        for symbol in details.keys():
            if symbol in symbols_to_upload:
                print symbol
                detail = details[symbol]
                name = detail[1]
                cur.execute(SQL, (symbol,name))

        con.commit()
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)        
        
    finally:
        
        if con:
            con.close()

    return

print "Get web links"
web_links = get_web_links()

print "Extract data from web links"
stock_details = get_stock_details(web_links)

print "Updating db"
update_db(stock_details)
print "Updating db complete"

