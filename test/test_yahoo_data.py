import os, sys
import json

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import yahoo_finance.yahoo_data as yd
import test.settings as settings

from unittest.mock import Mock, patch
import pytest
	
def load_moch_json(file_name):
	#file_name: full path to a jason file (from settings.py)
	#returns data from json file as a dictionary
	with open(file_name, 'r') as f:
		return json.loads(f.read())

@pytest.fixture(scope='module')
def stock_mock_factory():
	#patches the _request_data method, and replaces it with stored json
	@patch('yahoo_data.Stock_Data._request_data')
	def factory(file_name, mock_func):
		mock_func.return_value = load_moch_json(file_name)
		stock = yd.Stock_Data()
		stock._request_data = mock_func
		return stock
	return factory

@pytest.fixture(scope='module')
def option_mock_factory():
	#patches the _request_data method, and replaces it with stored json
	@patch('yahoo_data.Option_Data._request_data')
	def factory(file_name, mock_func):
		mock_func.return_value = load_moch_json(file_name)
		option = yd.Option_Data()
		option._request_data = mock_func
		return option
	return factory


class Test_Mock_Stock_Data:
	def test_stock_data_return_list(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.stock_data('JWN')
		assert isinstance(data, list)

	def test_stock_data_values(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.stock_data('JWN')
		for dictionary in data:
			assert isinstance(dictionary, dict)
			assert list(dictionary.keys()) == ['date', 'open', 
					'high', 'low', 'close', 'volume', 'adjclose']



class Test_Mock_Option_Data:
	def test_option_strike_prices(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.strike_prices('JWN')
		assert isinstance(data, list)
		for num in data:
			assert isinstance(num, float) or isinstance(num, int)

	def test_option_expirations(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.expirations('JWN')
		assert isinstance(data, list)

	def test_option_calls(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.calls('JWN')
		for dictionary in data:
			assert isinstance(dictionary, dict)
			assert list(dictionary.keys()) == ['contractSymbol','impliedVolatility','expiration',
			'change','currency','strike','contractSize','lastPrice','inTheMoney',
			'openInterest','percentChange','ask','volume','lastTradeDate','bid']

	def test_option_puts(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.puts('JWN')
		for dictionary in data:
			assert isinstance(dictionary, dict)
			assert list(dictionary.keys()) == ['contractSymbol','impliedVolatility','expiration',
			'change','currency','strike','contractSize','lastPrice','inTheMoney',
			'openInterest','percentChange','ask','volume','lastTradeDate','bid']


@pytest.mark.skipif(not settings.LIVE_TEST, 
	reason='These tests make request to yahoo finance or use cached requests')
class Test_Live_Stock_Data:
	stock = yd.Stock_Data()
	def test_stock_data_return_list(self):
		data = self.stock.stock_data('JWN')
		assert isinstance(data, list)

	def test_stock_data_values(self):
		data = self.stock.stock_data('JWN')
		for item in data:
			assert isinstance(item, dict)
			assert list(item.keys()) == ['date', 'open', 
					'high', 'low', 'close', 'volume', 'adjclose']


@pytest.mark.skipif(not settings.LIVE_TEST, 
	reason='These tests make request to yahoo finance or use cached requests')
class Test_Live_Option_Data:
	option = yd.Option_Data()
	def test_option_strike_prices(self):
		data = self.option.strike_prices('JWN')
		assert isinstance(data, list)
		for num in data:
			assert isinstance(num, float) or isinstance(num, int)

	def test_option_expirations(self):
		data = self.option.expirations('JWN')
		assert isinstance(data, list)

	def test_option_calls(self):
		data = self.option.calls('JWN')
		for dictionary in data:
			assert isinstance(dictionary, dict)
			assert list(dictionary.keys()) == ['contractSymbol','impliedVolatility','expiration',
			'change','currency','strike','contractSize','lastPrice','inTheMoney',
			'openInterest','percentChange','ask','volume','lastTradeDate','bid']

	def test_option_puts(self):
		data = self.option.puts('JWN')
		for dictionary in data:
			assert isinstance(dictionary, dict)
			assert list(dictionary.keys()) == ['contractSymbol','impliedVolatility','expiration',
			'change','currency','strike','contractSize','lastPrice','inTheMoney',
			'openInterest','percentChange','ask','volume','lastTradeDate','bid']




if __name__ == '__main__':
	pass