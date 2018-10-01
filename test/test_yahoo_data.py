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


STOCK_DATA_FIELDS = ['date', 'open', 'high', 'low', 'close', 
	'volume', 'adjclose']

RELATED_STOCK_FIELDS = ['symbol', 'openToday','highToday','lowToday',
	'closePrevious', 'recentPrice', 'volumeToday','sharesOtstanding',
	'marketCap','fiftyTwoWeekHigh', 'fiftyTwoWeekLow','fiftyTwoWeekRange',]

OPTION_DATA_FIELDS = ['contractSymbol','impliedVolatility','expiration',
	'change','currency','strike','contractSize','lastPrice','inTheMoney',
	'openInterest','percentChange','ask','volume','lastTradeDate','bid']


def assert_dictionary_list(lst, keys):
	'''lst: list containing dict items. keys: list of expected keys'''
	for dictionary in lst:
		assert isinstance(dictionary, dict)
		assert list(dictionary.keys()) == keys

def assert_number_list(lst):
	for num in lst:
		assert isinstance(num, float) or isinstance(num, int)


class Test_Mock_Stock_Data:
	def test_stock_data_return_list(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.stock_data('JWN')
		assert isinstance(data, list)

	def test_stock_data_values(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.stock_data('JWN')
		assert_dictionary_list(data, STOCK_DATA_FIELDS)

	def test_related_tickers_return_list(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.relate_tickers('JWN')
		assert isinstance(data, list)

	def test_related_tickers_values(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.relate_tickers('JWN')
		assert_dictionary_list(data, RELATED_STOCK_FIELDS)

	def test_overview_return_list(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.overview('JWN')
		assert isinstance(data, list)

	def test_overview_default(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.overview('JWN')
		assert_dictionary_list(data, RELATED_STOCK_FIELDS)

	def test_overview_related_tickers(self, stock_mock_factory):
		stock = stock_mock_factory(settings.STOCK_DATA_1D)
		data = stock.overview('JWN', relate_tickers='True')
		assert_dictionary_list(data, RELATED_STOCK_FIELDS)


class Test_Mock_Option_Data:
	def test_option_strike_prices(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.strike_prices('JWN')
		assert isinstance(data, list)
		assert_number_list(data)

	def test_option_expirations(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.expirations('JWN')
		assert isinstance(data, list)

	def test_option_calls(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.calls('JWN')
		assert_dictionary_list(data, OPTION_DATA_FIELDS)

	def test_option_puts(self, option_mock_factory):
		option = option_mock_factory(settings.OPTION_DATA_1)
		data = option.puts('JWN')
		assert_dictionary_list(data, OPTION_DATA_FIELDS)


@pytest.mark.skipif(not settings.LIVE_TEST, 
	reason='These tests make request to yahoo finance or use cached requests')
class Test_Live_Stock_Data:
	stock = yd.Stock_Data()
	def test_stock_data_return_list(self):
		data = self.stock.stock_data('JWN')
		assert isinstance(data, list)

	def test_stock_data_values(self):
		data = self.stock.stock_data('JWN')
		assert_dictionary_list(data, STOCK_DATA_FIELDS)


@pytest.mark.skipif(not settings.LIVE_TEST, 
	reason='These tests make request to yahoo finance or use cached requests')
class Test_Live_Option_Data:
	option = yd.Option_Data()
	def test_option_strike_prices(self):
		data = self.option.strike_prices('JWN')
		assert isinstance(data, list)
		assert_number_list(data)

	def test_option_expirations(self):
		data = self.option.expirations('JWN')
		assert isinstance(data, list)

	def test_option_calls(self):
		data = self.option.calls('JWN')
		assert_dictionary_list(data, OPTION_DATA_FIELDS)

	def test_option_puts(self):
		data = self.option.puts('JWN')
		assert_dictionary_list(data, OPTION_DATA_FIELDS)



if __name__ == '__main__':
	pass