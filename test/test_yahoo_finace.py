import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))

from yahoo_finance import Stock_Data
from collections import OrderedDict
import pandas as pd
import datetime as dt
import unittest
from unittest.mock import patch


class Test_Data_Request(unittest.TestCase):
	#mocking to prevent a get request
	@classmethod
	@patch.object(Stock_Data, 'request_data')
	def setUpClass(cls, mock_request):
		mock_request.return_value = 'some response'
		cls.ticker = 'AMD'
		cls.stock_data = Stock_Data(cls.ticker)
		mock_request.assert_called()
		
	def expect_url(self, data_obj):
		utc = data_obj.utc
		base_url = data_obj.url.replace('_', data_obj.ticker)
		append_url = data_obj.url_append.replace('start', f'{utc(data_obj.start)}'
			).replace('end', f'{utc(data_obj.end)}').replace('rate', data_obj.frequency)
		return base_url.replace(f'p={data_obj.ticker}', append_url)


	def test_process_url_default(self):
		result = self.stock_data.process_url(self.stock_data.url)
		expected = self.stock_data.url.replace('_', self.stock_data.ticker)
		self.assertEqual(result, expected)


	def test_process_url_custom_start(self):
		start='07/01/2018'
		data = Stock_Data(self.ticker, start=start)
		result = data.process_url(data.url)
		expected = self.expect_url(data)
		self.assertEqual(result, expected)
		self.assertIn(f'{data.utc(data.start)}', expected)


	def test_process_url_custom_end(self):
		end='07/01/2016'
		data = Stock_Data(self.ticker, end=end)
		result = data.process_url(data.url)
		expected = self.expect_url(data)
		self.assertEqual(result, expected)
		self.assertIn(f'{data.utc(data.end)}', expected)


	def test_process_url_custom_frequency(self):
		frequency = 'mo'
		data = Stock_Data(self.ticker, frequency=frequency)
		result = data.process_url(data.url)
		expected = self.expect_url(data)
		self.assertEqual(result, expected)
		self.assertIn(f'{data.frequency}', expected)


@unittest.skip('Only run when testing full functionality')
class Test_Request_Data_Handling(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.ticker = 'AMD'
		cls.stock_data = Stock_Data(cls.ticker)

	def test_good_request(self):
		self.assertEqual(self.stock_data.response.status_code, 200)
	
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
		#if today is a weekend or non trading day, the most recent trading day is first
		self.assertTrue(df['Date'].iloc[0] <= dt.date.today())
		#if last day is a weekend or non trading day, the closest subsequent trading day is last
		self.assertTrue(df['Date'].iloc[-1] >= dt.date.today() - dt.timedelta(days=365))


class Test_Request_Data_Handling_Custom_Inputs(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.ticker = 'AMD'
		cls.start = '02/02/2017'
		cls.end = '02/02/2018'
		cls.frequency = 'mo'
		cls.stock_data = Stock_Data(cls.ticker, start=cls.start,
						end=cls.end, frequency=cls.frequency)

	def test_data_frame_custom_date_range(self):
		df = self.stock_data.data_frame()
		self.assertIsInstance(df , pd.DataFrame,)
		first = dt.datetime.strptime(self.end, '%m/%d/%Y').date()
		last = dt.datetime.strptime(self.start, '%m/%d/%Y').date()
		#test that the data in the dataframe corresponds with the custom start and end
		self.assertTrue(df['Date'].iloc[0].year == first.year )
		self.assertTrue(df['Date'].iloc[0].month == first.month )
		self.assertTrue(df['Date'].iloc[-1].year == last.year)
		self.assertTrue(df['Date'].iloc[-1].month == last.month)



if __name__ == '__main__':
	unittest.main()










