baseCurrency = 'USD'
currency = 'INR'


blockurl = 'https://btc.com'
blockselector = '.table > tr:nth-child(2) > td.text-right > a'

baserateurl = f'https://api.kraken.com/0/public/Ticker?pair=XBT{baseCurrency}'

rateurl = f'https://api.exchangeratesapi.io/latest?base={baseCurrency}&symbols={currency}'

quoteurl = 'https://www.bitcoin-quotes.com/quotes/random.json'
