from db_fun import *

#print extract_stocks()

#insert_stocks('AAA','A terrible test')

#update_stocks('AAA','A terrible testtesttesttesttesttest')

#delete_stocks('AAA')

#stockdata = ({"symbol":"AAAA", "stockname":"A test"},
            #{"symbol":"AAAB", "stockname":"B test"},
            #{"symbol":"AAAC", "stockname":"C test"})
#insert_multi_stocks(stockdata)
##########
#insert_dividendhistory('AAA','1976-06-26','1140')

#stockdata = ({"symbol":"AAAA", "date":"1976-06-26", "amount":"8565"},
            #{"symbol":"AAAB", "date":"1986-06-26", "amount":"2342"},
            #{"symbol":"AAAD", "date":"1996-06-26", "amount":"342234"})
#insert_multi_dividendhistory(stockdata)

#update_dividendhistory('AAA','1976-06-26','20140')

#delete_dividendhistory('AAA','1976-06-26')
###########
#insert_pricehistory('AAA','2012-06-26','1140','1140','1140','1140','1140')

#stockdata = ({"symbol":"AAAA", "date":"1976-06-26", "open":"8565.21", "close":"4213", "high":"4213", "low":"4213", "volume":"4213"},
            #{"symbol":"AAAB", "date":"1986-06-26", "open":"18565", "close":"14213.32", "high":"14213", "low":"14213", "volume":"14213"},
            #{"symbol":"AAAD", "date":"1996-06-26", "open":"28565", "close":"24213", "high":"24213", "low":"24213.1", "volume":"24213"})
#insert_multi_pricehistory(stockdata)

#update_pricehistory('AAA','2012-06-26','11140','21140','31140','41140','51140')

#delete_pricehistory('AAA','2012-06-26')
###########
#insert_stockexchanges('LSE','London stock Exchange','AAA','England')

#stockdata = ({"exchange":"LSE", "exchangename":"London", "symbol":"AAAA", "country":"USA"},
            #{"exchange":"JSE", "exchangename":"asd", "symbol":"AAAC", "country":"England"},
            #{"exchange":"JSE", "exchangename":"das", "symbol":"AAAD", "country":"England"},
            #{"exchange":"NASDAX", "exchangename":"Nasd", "symbol":"AAAD", "country":"JAPan"})
#insert_multi_stockexchanges(stockdata)

#update_stockexchanges('LSE','London stock muhaha Exchange','AAA','England')

#delete_stockexchanges('LSE','AAA')
###########
#symbol,logtype,refid,date
insert_log('LSE',datetime.date.today(),1,0)

#logdata = ({"exchange":"LSE", "exchangename":"London", "symbol":"AAAA", "country":"USA"},
            #{"exchange":"JSE", "exchangename":"asd", "symbol":"AAAC", "country":"England"},
            #{"exchange":"JSE", "exchangename":"das", "symbol":"AAAD", "country":"England"},
            #{"exchange":"NASDAX", "exchangename":"Nasd", "symbol":"AAAD", "country":"JAPan"})
#insert_multi_log(stockdata)

#update_log()

#delete_log()
###########
