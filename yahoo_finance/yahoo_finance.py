import pandas as pd
import numpy as np
import datetime as dt
from collections import OrderedDict
from utc_converter import UTC_Converter
from requests_html import HTMLSession


class Stock_Data():
	url = 'https://finance.yahoo.com/quote/_/history?p=_'
	url_append = 'period1=start&period2=end&interval=1rate&filter=history&frequency=1rate'
	frequency_options = ['d', 'wk', 'mo']
	session = HTMLSession()
	utc = UTC_Converter()

	def __init__(self, ticker, start=dt.date.today()+dt.timedelta(days=365), 
				end=dt.date.today(), frequency='d', date_fmt_str=None):
		self.ticker = ticker.upper()
		self.start = start
		self.end = end
		self.frequency = frequency
		self.date_fmt = date_fmt_str
		self.response = self.request_data()


	def request_data(self):
		url = self.process_url(self.url)
		return self.session.get(url)

	def process_url(self, url):
		url = self.url.replace('_', self.ticker)
		default_start = dt.date.today()+dt.timedelta(days=365)
		default_end = dt.date.today()
		default_freq = 'd'
		#if any of the default options are changed
		if (self.start != default_start or self.end != default_end 
			or self.frequency != default_freq):
			start = self.utc(self.start, self.date_fmt)
			end = self.utc(self.end, self.date_fmt)
			append = self.url_append.replace('start', f'{start}')
			append = append.replace('end', f'{end}')
			append = append.replace('rate', self.frequency)
			url = url.replace(f'p={self.ticker}', append)
			return url

		else:
			return url



	def get_data_table(self):
		# <table class="W(100%) M(0)" data-test="historical-prices">
		table = self.response.html.find('table[data-test=historical-prices]', first=True)
		return table

	def table_head(self, table):
		return table.find('thead',)[0]

	def table_body(self, table):
		return table.find('tbody',)[0]

	def column_headers(self):
		head = self.table_head(self.get_data_table())
		cols = []
		for item in head.find('tr>th'):
			cols.append(item.text.replace('*',''))
		return cols

	def table_to_dict(self):
		'''Convert html table into dictionary'''
		headers = self.column_headers()
		table = OrderedDict((head, []) for head in headers)
		#searches the table body for tr tags
		for tr in self.table_body(self.get_data_table()).find('tr'):
			#searches for all td tags within each tr tag
			for i, td in enumerate(tr.find('td')):
				if headers[i] == 'Date':
					value = dt.datetime.strptime(td.text, '%b %d, %Y').date()
				else:
					value = float(td.text.replace(',', ''))
				table[headers[i]].append(value)
		return table


	def data_frame(self):
		table = self.table_to_dict()
		df = pd.DataFrame(table, index=table['Date'])
		return df













		