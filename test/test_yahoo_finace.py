import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))


from yahoo_finance import Stock_Data
from collections import OrderedDict
import pandas as pd
import unittest




class Test_Data_Request(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.ticker = 'AMD'
		cls.stock_data = Stock_Data(cls.ticker)
		cls.response = cls.stock_data.request_data()

	
	def test_good_request_yahoo_finance(self):
		self.assertEqual(self.response.status_code, 200)

	@unittest.skip('Need to figure this out')
	def test_bad_request_yahoo_finance(self):
		pass


	def test_get_data_table(self):
		table = self.stock_data.get_data_table()
		self.assertIn('<table', table.html )


	def test_table_head(self):
		table = self.stock_data.get_data_table()
		head = self.stock_data.table_head(table)
		self.assertIn('<thead', head.html)

	def test_table_body(self):
		table = self.stock_data.get_data_table()
		body = self.stock_data.table_body(table)
		self.assertIn('<tbody', body.html)

	def test_column_headers(self):
		headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
		self.assertEqual(headers, self.stock_data.column_headers())

	def test_table_to_dict(self):
		table_dict = self.stock_data.table_to_dict()
		self.assertIsInstance(table_dict, OrderedDict,)

	def test_data_frame(self):
		df = self.stock_data.data_frame()
		self.assertIsInstance(df , pd.DataFrame,)






if __name__ == '__main__':
	unittest.main()