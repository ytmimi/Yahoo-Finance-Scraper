'''
a script that will pull data from Yahoo and save it to /moch_data
'''
import os
import sys
import json
from functools import wraps

BASE_PATH = os.path.abspath('.')
sys.path.append(os.path.join(BASE_PATH, 'yahoo_finance'))
import yahoo_data as yd
import yahoo_finance as yf

stock_scraper = yf.Stock_Scraper
option_scraper = yf.Options_Scraper

stock = yd.Stock_Data()
option = yd.Option_Data()


def stock_scraper_kwargs(ticker, frequency):	
	return {'ticker':ticker, 'frequency':frequency, 
			'start_date':'09/26/2018', 'end_date':'09/26/2017'}

def option_scraper_kwargs(ticker, expiration):
	return {'ticker':ticker, 'expiration_date':expiration}

def make_directory(name):
	#creates a new directory if it doesn't exist
	path = os.path.join(BASE_PATH, name)
	os.makedirs(path, exist_ok=True)
	return path

def write_to_json(path, filename, data):
	#writes data to a file
	with open(os.path.join(path, filename),'w') as f:
		f.write(data)

def run_function(base_scraper, data_generator, function, *func_args, **func_kwargs):
	'''
	base_scraper: a scraper object from the yahoo_finance module
	data_generator: a data object form the yahoo_data module
	function: a function from the data_generator that scrapees data from yahoo finance.
	*func_args: positional arguments for the function
	**func_kwargs: named arguments for the function
	'''
	#instantiate the scraper
	new_scraper = base_scraper(**func_kwargs)
	#executes the function. Uses data_generator in place of self
	function(*func_args, **func_kwargs)
	url = new_scraper._process_url()
	key = data_generator._data_key(url)
	#returns the data stored that was just collected from yahoo finance
	return data_generator.cache[key]



if __name__ == '__main__':
	data_directory = make_directory('mock_data')
	ticker = 'JWN'
	frequencies = ['1d', '1wk', '1mo']
	for frequency in frequencies:
		kwargs = stock_scraper_kwargs(ticker, frequency)
		data = json.dumps(run_function(stock_scraper, stock, 
						stock.stock_data, **kwargs), indent=4)	
		write_to_json(data_directory, f'{ticker}_{frequency}.json', data)

	exp_months = option.expirations(ticker)
	for timestamp in exp_months:
		kwargs = option_scraper_kwargs(ticker, timestamp)
		data = json.dumps(run_function(option_scraper, option, 
					option.calls, **kwargs), indent=4)
		write_to_json(data_directory, f'{ticker}_{timestamp}.json', data)







