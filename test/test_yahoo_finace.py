import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))


from yahoo_finance import Stock_Data, UTC_Converter
from collections import OrderedDict
import pandas as pd
import datetime as dt
import unittest




class Test_Data_Request(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.ticker = 'AMD'
		cls.stock_data = Stock_Data(cls.ticker)
		cls.response = cls.stock_data.request_data()

	
	@unittest.skip('Testing other')
	def test_good_request_yahoo_finance(self):
		self.assertEqual(self.response.status_code, 200)

	@unittest.skip('Need to figure this out')
	def test_bad_request_yahoo_finance(self):
		pass

	@unittest.skip('Testing other')
	def test_get_data_table(self):
		table = self.stock_data.get_data_table()
		self.assertIn('<table', table.html )

	@unittest.skip('Testing other')
	def test_table_head(self):
		table = self.stock_data.get_data_table()
		head = self.stock_data.table_head(table)
		self.assertIn('<thead', head.html)

	@unittest.skip('Testing other')
	def test_table_body(self):
		table = self.stock_data.get_data_table()
		body = self.stock_data.table_body(table)
		self.assertIn('<tbody', body.html)

	@unittest.skip('Testing other')
	def test_column_headers(self):
		headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
		self.assertEqual(headers, self.stock_data.column_headers())

	@unittest.skip('Testing other')
	def test_table_to_dict(self):
		table_dict = self.stock_data.table_to_dict()
		self.assertIsInstance(table_dict, OrderedDict,)

	@unittest.skip('Testing other')
	def test_data_frame(self):
		df = self.stock_data.data_frame()
		self.assertIsInstance(df , pd.DataFrame,)
		#if today is a weekend or non trading day, the most recent trading day is first
		self.assertTrue(df['Date'].iloc[0] <= dt.date.today())
		#if last day is a weekend or non trading day, the closest subsequent trading day is last
		self.assertTrue(df['Date'].iloc[-1] >= dt.date.today() - dt.timedelta(days=365))

	
class Test_Time_Conversion(unittest.TestCase):
	def test_utc_string_right_fmt(self):
		# 1530331200 = 06/30/2018 @ 4:00am (UTC)
		# 1498795200 = 06/30/2017 @ 4:00am (UTC)
		utc = UTC_Converter('06/30/2018').__call__(fmt_str='%m/%d/%Y')
		self.assertEqual(utc, 1530331200)

	def test_utc_string_right_fmt(self):
		with self.assertRaises(ValueError) as ve:
			utc = UTC_Converter('06/30/2018').__call__(fmt_str='%Y/%m/%d')
			self.assertEqual(ve.msg, 'The fmt_str did not match the date provided.')

	def test_utc_string_default(self):
		utc = UTC_Converter('06/30/2018').__call__()
		self.assertEqual(utc, 1530331200)

	def test_utc_string_default_error(self):
		with self.assertRaises(ValueError) as ve:
			utc = UTC_Converter('June 30, 2018').__call__()
			self.assertEqual(ve.msg, 'Unable to parse string. Please supply the fmt_str kwarg.')


		


if __name__ == '__main__':
	unittest.main()










