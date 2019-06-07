#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  StockTrackerYahoo0.1.py
#  
#  Copyright 2012 Spills <Spills@MOTHERSHIP>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# seed is http://uk.finance.yahoo.com/losers?e=ftse
# and http://uk.finance.yahoo.com/gainers?e=ftse
# and http://uk.finance.yahoo.com/actives?e=ftse

import urllib
import StringIO
import csv
import string
import datetime
from db_fun import *

def get_next_symbol(page):
    marker = page.find('.L')
    if marker == -1: 
        return None, 0
    symbol = page[marker-4:marker]
    # quick fix -> validates stock symbol .. might need work
    while symbol[0] not in string.uppercase:
        symbol = symbol[1:]
        if len(symbol) == 0:
            break
    return symbol, marker + 2

def get_all_symbols(page):
    symbols = []
    while True:
        symbol,endpos = get_next_symbol(page)
        if symbol:
            if symbol not in symbols:
                symbols.append(symbol)
            page = page[endpos:]
        else:
            break
    return symbols

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
    return ""

def extract_history(page,symbol):
    stock_list = []

    page = page[page.find('\n')+1:]
    f = StringIO.StringIO(page)
    r = csv.reader(f)

    for line in r:
        data = {}
        data['symbol'] = symbol
        data['date'] = line[0]
        data['open'] = line[1]
        data['close'] = line[4]
        data['high'] = line[2]
        data['low'] = line[3]
        data['volume'] = line[5]
        stock_list.append(data)
        
    return tuple(stock_list)

def extract_dividend(page,symbol):
    stock_list = []

    page = page[page.find('\n')+1:]
    f = StringIO.StringIO(page)
    r = csv.reader(f)

    for line in r:
        data = {}
        data['symbol'] = symbol
        data['date'] = line[0]
        data['amount'] = line[1]
        stock_list.append(data)
    
    return tuple(stock_list)
    
def extract_stock_details(page,symbol):
    
    details = {}
#title
    title_start = page.find('class="title"') + 18
    title_end = title_start + page[title_start:].find("("+symbol.upper()) - 2
    details['name'] = page[title_start:title_end]
    
#date - today
    details['date'] = datetime.date.today()

#open
    open_start = page.find('Open:</th><td') + 13
    open_start = page[open_start:].find('>') + open_start + 1
    open_end = open_start + page[open_start:].find("</td>")
    details['open'] = page[open_start:open_end].replace(',','')

#close
    close_start = page.find('<span class="time_rtq_ticker">') + 30
    close_start = page[close_start:].find('>') + close_start + 1
    close_end = close_start + page[close_start:].find("</span>")
    details['close'] = page[close_start:close_end].replace(',','')

#low - high
    range_start = page.find("Day's Range:") + 12
    range_start = page[range_start:].find("span id") + range_start + 7
    range_start = page[range_start:].find('>') + range_start + 1
    range_end = range_start + page[range_start:].find("</span></span>")
    details['low'] = page[range_start:range_end].replace(',','')

    range_start = page[range_start:].find('span id') + range_start + 7
    range_start = page[range_start:].find('>') + range_start + 1
    range_end = range_start + page[range_start:].find("</span></span>")
    details['high'] = page[range_start:range_end].replace(',','')

#volume
    volume_start = page.find('Volume:') + 7
    volume_start = page[volume_start:].find('span id') + volume_start + 7
    volume_start = page[volume_start:].find('>') + volume_start + 1
    volume_end = volume_start + page[volume_start:].find("</span>")
    details['volume'] = page[volume_start:volume_end].replace(',','')

    return details

def get_existing_symbols():
    symbols = []
    for row in extract_stocks():
        symbols.append(row[0].strip())
    return symbols

def union(p,q): 
    for e in q:
        if e not in p:
            p.append(e)

def get_lwv_symbols():
    symbols = []

    symbols = get_all_symbols(get_page("http://uk.finance.yahoo.com/gainers?e=ftas"))
    union(symbols,get_all_symbols(get_page("http://uk.finance.yahoo.com/losers?e=ftas")))
    union(symbols,get_all_symbols(get_page("http://uk.finance.yahoo.com/actives?e=ftas")))

    return symbols
    
def get_history_page(symbol):
    his_prefix = 'http://ichart.finance.yahoo.com/table.csv?s='
    today = datetime.date.today()
    his_postfix = '.L&d='+str(int(today.strftime("%m"))-1)+'&e='+today.strftime("%d")+'&f='+today.strftime("%Y")+'&g=d&a=4&b=15&c=2000&ignore=.csv'
    return get_page(his_prefix + symbol + his_postfix)

def get_dividend_page(symbol):
# e.g. dividend link: http://ichart.finance.yahoo.com/table.csv?s=LLOY.L&a=00&b=1&c=2000&d=10&e=20&f=2012&g=v&ignore=.csv
    div_prefix = "http://ichart.finance.yahoo.com/table.csv?s="
    div_postfix = ".L&a=00&b=1&c=2000&d=10&e=20&f=2012&g=v&ignore=.csv"
    return get_page(div_prefix + symbol + div_postfix)

def get_stock_page(symbol):
# e.g. stock link: http://uk.finance.yahoo.com/q?s=LLOY.L
    div_prefix = "http://uk.finance.yahoo.com/q?s="
    div_postfix = ".L"
    return get_page(div_prefix + symbol + div_postfix)

def main():
    insert_log('Upd8',datetime.date.today(),9,0)
    
	# extract existing stock symbols from database table, stocks
    db_stocks = get_existing_symbols()
    
    # extract stock from winners, losers, volume pages
    lwv_stocks = get_lwv_symbols()

    # any of these stocks that are not in the db need to have their price history, dividend history and details uploaded
    print "Winners, losers and volume stocks:"
    for symbol in lwv_stocks:        
        if symbol not in db_stocks:
            print symbol
            #details - company name
            try:
                stock_detail = extract_stock_details(get_stock_page(symbol),symbol)
                if stock_detail['name'] == "":
                    break
                insert_stocks(symbol,stock_detail['name'])
                insert_log(symbol,datetime.date.today(),1,0)
            except:
                print "Error - details: %s" % symbol
                insert_log(symbol,datetime.date.today(),5,0)

            #price history
            try:
                insert_multi_pricehistory(extract_history(get_history_page(symbol),symbol))
                insert_log(symbol,datetime.date.today(),2,0)
            except:
                print "Error - price history: %s" % symbol
                insert_log(symbol,datetime.date.today(),6,0)

            #dividend history
            try:
                insert_multi_dividendhistory(extract_dividend(get_dividend_page(symbol),symbol))
                insert_log(symbol,datetime.date.today(),3,0)
            except:
                print "Error - dividend history: %s" % symbol
                insert_log(symbol,datetime.date.today(),7,0)
            
    # update existing with latest data
    print "Existing stocks:"
    for symbol in db_stocks:
        print symbol
        try:
            stock_detail = extract_stock_details(get_stock_page(symbol),symbol)
            insert_pricehistory(symbol,stock_detail['date'],stock_detail['open'],stock_detail['close'],stock_detail['high'],stock_detail['low'],stock_detail['volume'])
            insert_log(symbol,datetime.date.today(),2,0)
        except:
            print "Error - latest details: %s" % symbol
            insert_log(symbol,datetime.date.today(),6,0)

    insert_log('Upd8',datetime.date.today(),10,0)
    
    return 0

if __name__ == '__main__':
	main()

