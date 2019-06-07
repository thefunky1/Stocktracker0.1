from datetime import date
from dateutil.rrule import rrule, DAILY

class Stock():
    def __init__(self, name, symbol, prices):
        '''
        prices = {date:[open,close,high,low,volume]}
        '''
        self.name = name
        self.symbol = symbol
        self.prices = prices
    
    def __str__(self):
        return  'Symbol: ' + self.symbol + ' Name: ' + self.name
    
    def max_close_price(self, start_date=date.today(), end_date=date.today()):
        '''
        Returns the highest close price for the period specified
        If no dates is entered, the most recent close price is returned
        If only a start_date is entered then the end_date is the last close date
        If an end_date is specified then a start_date must be specified
        end_date must be more recent or equal to sart_date
        '''
        result = 0 # for now
        
        for dt in rrule(DAILY, dtstart=start_date, until=end_date):
            a = self.prices[dt.date()]['close']
            print a
#            if self.prices[dt.date()][1] < result:
#                result = prices[dt.date()]['close']
        
        #a = date(2009, 5, 30)
        #b = date(2009, 6, 9)

        #for dt in rrule(DAILY, dtstart=a, until=b):
        #    print dt.strftime("%Y-%m-%d")

        
        return result