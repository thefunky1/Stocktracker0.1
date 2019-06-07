from Stock import Stock
from db_fun import *

from datetime import date
def test():
    """
    test to access stock data
    """
    for stock in stock_list:
        print stock.name
        print stock.symbol
        try:
            print stock.prices[datetime.date(2010,12,23)].keys()
            a = stock.prices[datetime.date(2010,12,23)]['volume']
            print a # works
            print stock.prices[datetime.date(2012,12,23)].get('open') # does not work!!!
        except:
            print "No data for 2010-12-23"


def extract_stock_data():
    """
    Extracts data from database - takes a few seconds
    """
    print 'Extracting stock data from database'
    stocks_db = extract_stocks()

    # stock_list = list of stock objects
    stock_list = []

    # populate stock_list with data    
    for stock in stocks_db:
        symbol = list(stock)[0].strip()
        name = list(stock)[1].strip()

        prices = {}
        prices_tuple = extract_pricehistory(symbol)
        for dt in prices_tuple:
            daily_price_details = {}
            daily_price_details['open'] = list(dt)[2]
            daily_price_details['close'] = list(dt)[3]
            daily_price_details['high'] = list(dt)[4]
            daily_price_details['low'] = list(dt)[5]
            daily_price_details['volume'] = list(dt)[6]

            prices[list(dt)[1]] = daily_price_details
        stock_list.append(Stock(name,symbol,prices))

    return stock_list

def output_screen(output):
    print output
    
if __name__ == "__main__":
    # load stocks from db
    print 'Initialising program'
    stock_list = extract_stock_data()
    
    #test()

    # analyse stock_list, any stocks meeting criteria append to output_list:
    print 'Starting analyses'
    output_list = []
    start_date = date(2012,12,17)
    end_date = date(2012,12,19)
    
    for stock in stock_list:
        #try:
        print stock, stock.max_close_price(start_date, end_date)
        #except:
            #print 'Error on: ', stock
        #if stock.max_close_price() / stock.max_close_price(start_date, end_date) < 0.9:
        #    output_list.append(stock)

    output_screen(output_list)
