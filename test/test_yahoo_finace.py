import os
import sys
import datetime as dt

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))
from yahoo_finance import (Base_Scraper, Stock_Scraper, Statistics_Scraper,Profile_Scraper,
	Income_Statement_Scraper, Balance_Sheet_Scraper, Cash_Flow_Scraper,
	Analysis_Scraper, Options_Scraper, Holders_Scraper, Sustainability_Scraper,)

from unittest.mock import patch
import pytest

LIVE_TEST = False


class Test_Base_Scraper:
	def test_base_url(self):
		assert Base_Scraper('IBM').base_url == 'https://finance.yahoo.com/quote/IBM'

	def test_default_query_string(self):
		assert Base_Scraper('IBM')._default_query_string() == 'p=IBM'

	def test_url_base_qs(self):
		assert Base_Scraper('IBM')._process_url() == (
			'https://finance.yahoo.com/quote/IBM?p=IBM'
			)

class Test_Stock_Scraper:
	def test_base_url(self):
		scraper =  Stock_Scraper('IBM')
		assert scraper.base_url == 'https://finance.yahoo.com/quote/IBM/history'

	def test_advanced_qs(self):
		ticker = 'AAPL'
		start = '10/20/2013'
		end = '10/20/2014'
		freq = '1d'
		scraper = Stock_Scraper(ticker, start, end, freq)
		assert scraper._advanced_query_string() == (
			'period1=1382241600&period2=1413777600&interval=1d&filter=history&frequency=1d'
			)

	def test_url_base_qs(self):
		scraper = Stock_Scraper('AAPL')
		scraper._process_url() == 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
		
	def test_url_advanced_qs(self):
		ticker = 'AAPL'
		start = '10/20/2013'
		end = '10/20/2014'
		freq = '1d'
		scraper = Stock_Scraper(ticker, start, end, freq)
		assert scraper._process_url() == (
			'https://finance.yahoo.com/quote/AAPL/history?'
			'period1=1382241600&period2=1413777600&interval=1d&filter=history&frequency=1d'
			)

class Test_Statistics_Scraper:
	def test_base_url(self):
		assert Statistics_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/key-statistics'
			)

	def test_url_base_qs(self):
		assert Statistics_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/key-statistics?p=NFLX'
			)

class Test_Profile_Scraper:
	def test_base_url(self):
		assert Profile_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/profile'
			)

	def test_url_base_qs(self):
		assert Profile_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/profile?p=NFLX'
			)

class Test_Income_Statement_Scraper:
	def test_base_url(self):
		assert Income_Statement_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/financials'
			)

	def test_url_base_qs(self):
		assert Income_Statement_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/financials?p=NFLX'
			)

class Test_Balance_Sheet_Scraper:
	def test_base_url(self):
		assert Balance_Sheet_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/balance-sheet'
			)

	def test_url_base_qs(self):
		assert Balance_Sheet_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/balance-sheet?p=NFLX'
			)

class Test_Cash_Flow_Scraper:
	def test_base_url(self):
		assert Cash_Flow_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/cash-flow'
			)

	def test_url_base_qs(self):
		assert Cash_Flow_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/cash-flow?p=NFLX'
			)

class Test_Analysis_Scraper:
	def test_base_url(self):
		assert Analysis_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/analysis'
			)

	def test_url_base_qs(self):
		assert Analysis_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/analysis?p=NFLX'
			)

class Test_Options_Scraper:
	def test_base_url(self):
		assert Options_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/options'
			)

	def test_url_base_qs(self):
		assert Options_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/options?p=NFLX'
			)
	
	def test_url_advanced_qs(self):
		assert Options_Scraper('NFLX', '10/12/2018')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/options?p=NFLX&date=1539302400'
			)

class Test_Holders_Scraper:
	def test_base_url(self):
		assert Holders_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/holders'
			)

	def test_url_base_qs(self):
		assert Holders_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/holders?p=NFLX'
			)

class Test_Sustainability_Scraper:
	def test_base_url(self):
		assert Sustainability_Scraper('NFLX').base_url == (
			'https://finance.yahoo.com/quote/NFLX/sustainability'
			)

	def test_url_base_qs(self):
		assert Sustainability_Scraper('NFLX')._process_url() == (
			'https://finance.yahoo.com/quote/NFLX/sustainability?p=NFLX'
			)




@pytest.mark.skipif(not LIVE_TEST, reason='These tests each make seperate request to yahoo finance')
class Test_Requests:
	def test_base(self):
		resp = Base_Scraper('JWN').request_data()
		assert 'context' in resp.keys()

	def test_base_stock(self):
		resp = Stock_Scraper('JWN').request_data()
		assert 'context' in resp.keys()

	def test_advanced_stock(self):
		resp = Stock_Scraper('JWN', '10/20/2013', 
					'10/20/2014').request_data()
		assert 'context' in resp.keys()

	def test_statistics(self):
		resp = Statistics_Scraper('NFLX').request_data()
		assert 'context' in resp.keys()

	def test_profile(self):
		resp = Profile_Scraper('NFLX').request_data()
		assert 'context' in resp.keys()

	def test_income_statement(self):
		resp = Income_Statement_Scraper('NFLX').request_data()
		assert 'context' in resp.keys()

	def test_balance_sheet(self):
		resp = Balance_Sheet_Scraper('NFLX').request_data()
		assert 'context' in resp.keys()

	def test_cash_flow(self):
		resp = Cash_Flow_Scraper('NFLX').request_data()
		assert 'context' in resp.keys()

	def test_analysis(self):
		resp = Analysis_Scraper('MSFT').request_data()
		assert 'context' in resp.keys()

	def test_base_options(self):
		resp = Options_Scraper('MSFT').request_data()
		assert 'context' in resp.keys()

	@pytest.mark.skip('fill out the body')
	def test_advanced_options(self):
		pass

	def test_holders(self):
		resp = Holders_Scraper('MSFT').request_data()
		assert 'context' in resp.keys()

	def test_sustainability(self):
		resp = Sustainability_Scraper('MSFT').request_data()
		assert 'context' in resp.keys()




if __name__ == '__main__':
	pytest.main()










