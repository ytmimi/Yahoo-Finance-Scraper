import json
import datetime as dt
from datetime import date, timedelta
from collections import OrderedDict

from urllib.parse import urlencode
from utc_converter import UTC_Converter
from requests_html import HTMLSession
import requests

session = HTMLSession()
utc = UTC_Converter()


class Base_Scraper:
	_base_url = 'https://finance.yahoo.com/quote/_'
	def __init__(self, ticker):
		'''ticker: str, stock ticker'''
		self.ticker = ticker

	def request_data(self):
		'''
		makes an HTTP GET request and returns json data
		'''
		resp = requests.get(self._process_url())
		if resp.status_code < 400:
			return self._process_response(resp)
		return json.loads(resp.text)
	
	@property
	def base_url(self):
		'''includes the ticker in the base url'''
		return self._base_url.replace('_', self.ticker)

	def _process_url(self):
		''' formats the url string'''
		return f'{self.base_url}?{self._default_query_string()}'

	def _default_query_string(self):
		'''returns p=ticker'''
		return urlencode({'p':self.ticker})

	@staticmethod
	def _process_response(resp):
		'''
		resp: request.Response object

		when examining the response from Yahoo finance, I noticed that
		I wasn't getting back HTML, but instead the html was being rendered with
		JavaScript. Instead of trying to get the html, and then parsing that I think its more effective
		to simply parse the text. This function parses the text from the response and returns a json
		object with the data that would have been rendered to HTML  
		'''
		#after splitting and inspecting the string It was determined that the 44th index
		#contained the information that we needed
		block = resp.text.split('\n')[44]
		#removes the unessessary "root.App.main = " and trailing ";" so that we are left with 
		#a string representation of the json, and then we convert the json string into a python dict
		return json.loads(block[16:-1])



class Stock_Scraper(Base_Scraper):
	endpoint = '/history'
	frequency_options = ['1d', '1wk', '1mo']
	
	def __init__(self, ticker, start_date=date.today()-timedelta(days=365),
		end_date=date.today(),frequency='1d', date_fmt_str=None):
		'''
		start_date: str, or datetime object
		end_date: str or datetime object
		frequency: str: '1d', '1wk', '1mo' for 1 day ,1 week, and 1 month respectively
		date_fmt_str: standard datetime format string in case the string provided for 
						start_date and end_date is unrecognized by the program.
		'''
		super().__init__(ticker)
		self.start_date = start_date
		self.end_date = end_date
		self.frequency = self._validate_frequency(frequency)
		self.date_fmt = date_fmt_str

	@classmethod
	def _validate_frequency(cls, frequency):
		if frequency not in cls.frequency_options:
			raise ValueError(f'frequency must be either {" or ".join(self.frequency_options)}.')
		return frequency

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

	def _process_url(self):
		if (self.end_date != date.today() or self.start_date != date.today()-timedelta(days=365)
			or self.frequency != '1d'):
			return f'{self.base_url}?{self._advanced_query_string()}'
		return super()._process_url()

	def _advanced_query_string(self):
		url_params = {
		'period1': utc(self.start_date, fmt_str=self.date_fmt),
		'period2': utc(self.end_date, fmt_str=self.date_fmt),
		'interval': self.frequency,
		'filter':'history',
		'frequency': self.frequency,
		}
		return urlencode(url_params)

class Statistics_Scraper(Base_Scraper):
	endpoint = '/key-statistics'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Profile_Scraper(Base_Scraper):
	endpoint = '/profile'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint


class Income_Statement_Scraper(Base_Scraper):
	endpoint = '/financials'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Balance_Sheet_Scraper(Base_Scraper):
	endpoint = '/balance-sheet'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Cash_Flow_Scraper(Base_Scraper):
	endpoint = '/cash-flow'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Analysis_Scraper(Base_Scraper):
	endpoint = '/analysis'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Options_Scraper(Base_Scraper):
	endpoint = '/options'
	def __init__(self, ticker, expiration_date=None, date_fmt=None):
		'''
		expiration_date: a str or datetime object
		date_fmt: an appropriate date formate string if expiration_date is provided as a string
		'''
		super().__init__(ticker)
		self.date = expiration_date
		self.date_fmt = date_fmt

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

	def _process_url(self):
		if (self.date):
			return f'{self.base_url}?{self._advanced_query_string()}'
		return super()._process_url()

	def _advanced_query_string(self):
		url_params = {
		'p':self.ticker,
		#offset by -4 hours to get to midnight
		'date': utc(self.date, dt.timedelta(hours=-4), self.date_fmt),
		}
		return urlencode(url_params)

class Holders_Scraper(Base_Scraper):
	endpoint = '/holders'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint

class Sustainability_Scraper(Base_Scraper):
	endpoint = '/sustainability'
	def __init__(self, ticker):
		super().__init__(ticker)

	@property
	def base_url(self):
		'''adds the endpoint to the base url'''
		return super().base_url + self.endpoint



if __name__ == '__main__':
	
	stock = Stock_Scraper('JWN', start_date='10/20/2014', end_date='10/30/2017', frequency='1wk').request_data()
	options = Options_Scraper('JWN').request_data()
	print(stock.keys())
	print('\n')
	print(options['context']['dispatcher']['stores']['OptionContractsStore'].keys())
	







