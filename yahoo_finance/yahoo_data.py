import os, sys
from base64 import b64encode

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_PATH, 'yahoo_finance'))

import yahoo_finance.yahoo_finance as yf 


class CacheData:
	'''
	Mixin to be used with any class that defines a scraper.
	checks if the base _request_data function has already been cached
	'''
	#cache of data being received from yahoo finance
	cache = dict()	

	@staticmethod
	def _data_key(url):
		'''establishes a unique key for each endpoint'''
		return b64encode(bytes(url, encoding='UTF-8'))

	def to_cache(self, key, data):
		self.cache[key] = data

	def _request_data(self, scraper, use_cache=True):
		'''returns the base dictionary of data from the scraper
		although this method doesn't use self
		'''
		key = self._data_key(scraper._process_url())
		if self.cache.get(key) and use_cache:
			print('From Cache')
			return self.cache.get(key)
		else:
			print('From Yahoo')
			data = scraper.request_data()['context']['dispatcher']['stores']
			self.to_cache(key, data)
			return data


class Stock_Data(CacheData):
	scraper = yf.Stock_Scraper
	
	@staticmethod
	def _get_ticker(*args, **kwargs):
		if args:
			return args[0]
		if kwargs: 
			return kwargs['ticker']
	
	def stock_data(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		data = self._request_data(scraper)['HistoricalPriceStore']['prices']
		#filters the data we get back from dividends and blank values
		return [item for item in data if not item.get('type') and item.get('open') != None]

	@staticmethod
	def _filter_ticker_data(data_dict):
		'''data_dict: a dict that contains info on the stock like:
		symbol, regularMarketOpen, 'regularMarketHigh', or 'fiftyTwoWeekRange'
		'''
		return {
				'symbol':data_dict['symbol'],
				'openToday':data_dict['regularMarketOpen'],
				'highToday':data_dict['regularMarketDayHigh'],
				'lowToday':data_dict['regularMarketDayLow'],
				'closePrevious':data_dict['regularMarketPreviousClose'],
				'recentPrice':data_dict['regularMarketPrice'],
				'volumeToday':data_dict['regularMarketVolume'],
				'sharesOutstanding':data_dict['sharesOutstanding'],
				'marketCap':data_dict['marketCap'],
				'fiftyTwoWeekHigh':data_dict['fiftyTwoWeekHigh'],
				'fiftyTwoWeekLow':data_dict['fiftyTwoWeekLow'],
				'fiftyTwoWeekRange':data_dict['fiftyTwoWeekRange'],
				} 
			
	def relate_tickers(self, *args, **kwargs):
		ticker = self._get_ticker(*args, **kwargs)
		scraper = self.scraper(*args, **kwargs)
		data = self._request_data(scraper)['RecommendationStore']['recommendedSymbols'][ticker]
		return [self._filter_ticker_data(item) for item in data]

	def overview(self, *args, **kwargs):
		'''return info on 52 week high, close, open previous close...'''
		ticker = self._get_ticker(*args, **kwargs)
		related_ticker = kwargs.pop('related_tickers', None)
		scraper = self.scraper(ticker)
		if related_ticker:
			data = self._request_data(scraper)['StreamDataStore']['quoteData']
			return [self._filter_ticker_data(data[symbol] for symbol in data)]
		else:
			data = self._request_data(scraper)['StreamDataStore']['quoteData'][ticker]
			#although it only returns one, its a list to be consistent
			return [self._filter_ticker_data(data)]


class Option_Data(CacheData):
	scraper = yf.Options_Scraper
	
	def strike_prices(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		return self._request_data(
			scraper)['OptionContractsStore']['meta']['strikes']

	def expirations(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		return self._request_data(scraper
			)['OptionContractsStore']['meta']['expirationDates']

	def calls(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		return self._request_data(scraper
			)['OptionContractsStore']['contracts']['calls']

	def puts(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		return self._request_data(scraper
			)['OptionContractsStore']['contracts']['puts']


