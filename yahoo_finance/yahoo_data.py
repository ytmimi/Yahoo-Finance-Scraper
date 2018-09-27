from base64 import b64encode
from yahoo_finance import Stock_Scraper, Options_Scraper


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
	scraper = Stock_Scraper
	
	def stock_data(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		data = self._request_data(scraper)['HistoricalPriceStore']['prices']
		#filters the data we get back from dividends and blank values
		return [item for item in data if not item.get('type') and item.get('open') != None]

	def relate_stocks(self, *args, **kwargs):
		check_out = 'RecommendationStore'
		pass

	#think about useing another streaming serveis like IEX
	def current_price(self, *args, **kwargs):
		scraper = self.scraper(*args, **kwargs)
		check_out=['StreamDataStore', 'quoteData', 'TICKER','regularMarketPrice']
		pass

	#think about useing another streaming serveis like IEX
	def new_current_price(self, *args, **kwargs):
		''' '''
		pass

	def overview(self, *args, **kwargs):
		'''return info on 52 week high, close, open previous close...'''
		pass


class Option_Data(CacheData):
	scraper = Options_Scraper
	
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


