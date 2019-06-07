#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  StockFinder.py
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

import urllib
import StringIO
import csv
import string
import datetime
from db_fun import *

def get_existing_symbols():
    symbols = []
    for row in extract_stocks():
        symbols.append(row[0].strip())
    return symbols

def main():
    # extract existing stock symbols from database table, stocks
    db_stocks = get_existing_symbols()
    
    # update existing with latest data
    for symbol in db_stocks:
        try:
            print extract_pricehistory(symbol)
        except:
            print "Error - symbol: %s" % symbol
    
    return 0

if __name__ == '__main__':
        main()

