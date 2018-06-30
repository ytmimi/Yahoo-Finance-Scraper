import pandas as pd
import numpy as np
import datetime as dt
from collections import OrderedDict
from requests_html import HTMLSession


class Stock_Data():
	url = 'https://finance.yahoo.com/quote/_/history?p=_'
	session = HTMLSession()

	def __init__(self, ticker, start=dt.date.today()+dt.timedelta(days=365), 
				end=dt.date.today()):
		self.ticker = ticker
		self.start = start
		self.end = end


	def request_data(self):
		# period1=1498795200&period2=1530331200&interval=1d&filter=history&frequency=1d
		url = self.url.replace('_', self.ticker)
		return self.session.get(url)

	def get_data_table(self):
		response = self.request_data()
		# <table class="W(100%) M(0)" data-test="historical-prices">
		table = response.html.find('table[data-test=historical-prices]', first=True)
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
		headers = self.column_headers()
		table = OrderedDict((head, []) for head in headers)
		for tr in self.table_body(self.get_data_table()).find('tr'):
			for i, td in enumerate(tr.find('td')):
				if headers[i] == 'Date':
					value = dt.datetime.strptime(td.text, '%b %d, %Y')
				else:
					value = float(td.text.replace(',', ''))
				table[headers[i]].append(value)
		return table


	def data_frame(self):
		table = self.table_to_dict()
		df = pd.DataFrame(table, index=table['Date'])
		return df


		