import json
import os
import sys
from datetime import date, timedelta
from functools import wraps

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import yahoo_finance.yahoo_data as yd
from utc_converter import (date_str_from_timestamp as strftimestamp,
	_date_string_to_utc as string_to_utc
)
from schema_description import (
	Stock_Price_Description as sp_desc,
	Option_Description as op_desc,
	Option_Chain_Description as opc_desc,
	Ticker_Description as tik_desc,
	Query_Description as q_desc,
	StockOverview as so_desc,
)

import graphene

stock = yd.Stock_Data()
option = yd.Option_Data()

def convert_timstamp(f):
	'''Decorator that converst timstamps to strings'''
	@wraps(f)
	def wrapper(*args, **kwargs):
		return strftimestamp(f(*args, **kwargs))
	return wrapper

def round_value(f, decimals=2):
	'''Decorator that rounds Floats'''
	@wraps(f)
	def wrapper(*args, **kwargs):
		return round(f(*args, **kwargs), decimals)
	return wrapper

#noramlly resolvers take in root(self) and info. but since I don't use
#info, all custom resolvers dont take info as an argument
@round_value
def round_resolver(root, attr):
	return getattr(root, attr)

@convert_timstamp
def date_resolver(root, date):
	return getattr(root, date)

class StockPrice(graphene.ObjectType):
	date = graphene.String(
		description=sp_desc.desc('date'),
		resolver=lambda root, info: date_resolver(root, 'date')
			)
	open_ = graphene.Float(
		name='open', description=sp_desc.desc('open_'),
		resolver= lambda root, info: round_resolver(root, 'open_')
		)
	high = graphene.Float(
		description=sp_desc.desc('high'),
		resolver= lambda root, info: round_resolver(root, 'high')
		)
	low = graphene.Float(
		description=sp_desc.desc('low'),
		resolver= lambda root, info: round_resolver(root, 'low')
		)
	close = graphene.Float(
		description=sp_desc.desc('close'),
		resolver= lambda root, info: round_resolver(root, 'close')
		)
	volume = graphene.Float(
		description=sp_desc.desc('volume'),
		resolver= lambda root, info: round_resolver(root, 'volume')
		)
	adjclose = graphene.Float(
		description=sp_desc.desc('adjclose'),
		resolver= lambda root, info: round_resolver(root, 'adjclose')
		)


def raw_resolver(root, attr):
	'''Some atributes are stored as dicts. When they are resolved
		we want to access their raw data'''
	return getattr(root, attr)['raw']

@convert_timstamp
def raw_exp_resolver(root, exp_date):
	return getattr(root, exp_date)['raw']

@round_value
def raw_round_resolver(root, attr):
	return getattr(root, attr)['raw']


class Option(graphene.ObjectType):
	contractSymbol = graphene.String(
		description= op_desc.desc('contractSymbol'),
		)
	expiration = graphene.String(
		description=op_desc.desc('expiration'),
		resolver=lambda root, info: raw_exp_resolver(root, 'expiration')
		)
	change = graphene.Float(
		description = op_desc.desc('change'),
		resolver = lambda root, info: raw_resolver(root, 'change'),
		)
	lastPrice = graphene.Float(
		description = op_desc.desc('lastPrice'),
		resolver = lambda root, info: raw_resolver(root, 'lastPrice'),
		)
	inTheMoney = graphene.Boolean(
		description = op_desc.desc('inTheMoney'),
		)
	impliedVolatility = graphene.Float(
		description = op_desc.desc('impliedVolatility'),
		resolver = lambda root, info: raw_round_resolver(root, 'impliedVolatility'),
		)
	openInterest = graphene.Float(
		description = op_desc.desc('openInterest'),
		resolver = lambda root, info: raw_resolver(root, 'openInterest'),
		)
	percentChange = graphene.Float(
		description = op_desc.desc('percentChange'),
		resolver = lambda root, info: raw_resolver(root, 'percentChange'),
		)
	bid = graphene.Float(
		description = op_desc.desc('bid'),
		resolver = lambda root, info: raw_resolver(root, 'bid'),
		)
	ask = graphene.Float(
		description = op_desc.desc('ask'),
		resolver = lambda root, info: raw_resolver(root, 'ask'),
		)
	volume = graphene.Float(
		description = op_desc.desc('volume'),
		resolver = lambda root, info: raw_resolver(root, 'volume'),
		)
	lastTradeDate = graphene.String(
		description = op_desc.desc('lastTradeDate'),
		resolver = lambda root, info: raw_exp_resolver(root, 'lastTradeDate'),
		)
	currency = graphene.String(
		description = op_desc.desc('currency'),
		)
	strike = graphene.Float(
		description = op_desc.desc('strike'),
		resolver = lambda root, info: raw_resolver(root, 'strike'),
		)
	contractSize = graphene.String(
		description = op_desc.desc('contractSize'),
		)


class StockOverview(graphene.ObjectType):
	symbol = graphene.String(
		description = so_desc.desc('symbol'),
		)
	openToday = graphene.Float(
		description = so_desc.desc('openToday'),
		resolver = lambda root, info: raw_round_resolver(root, 'openToday')
		)
	highToday = graphene.Float(
		description = so_desc.desc('highToday'),
		resolver = lambda root, info: raw_round_resolver(root, 'highToday')
		)
	lowToday = graphene.Float(
		description = so_desc.desc('lowToday'),
		resolver = lambda root, info: raw_round_resolver(root, 'lowToday')
		)
	closePrevious = graphene.Float(
		description = so_desc.desc('closePrevious'),
		resolver = lambda root, info: raw_round_resolver(root, 'closePrevious')
		)
	recentPrice = graphene.Float(
		description = so_desc.desc('recentPrice'),
		resolver = lambda root, info: raw_round_resolver(root, 'recentPrice')
		)
	volumeToday = graphene.Float(
		description = so_desc.desc('volumeToday'),
		resolver = lambda root, info: raw_round_resolver(root, 'volumeToday')
		)
	sharesOtstanding = graphene.Float(
		description = so_desc.desc('sharesOtstanding'),
		resolver = lambda root, info: raw_round_resolver(root, 'sharesOtstanding')
		)
	marketCap = graphene.Float(
		description = so_desc.desc('marketCap'),
		resolver = lambda root, info: raw_round_resolver(root, 'marketCap')
		)
	fiftyTwoWeekHigh = graphene.Float(
		description = so_desc.desc('fiftyTwoWeekHigh'),
		resolver = lambda root, info: raw_round_resolver(root, 'fiftyTwoWeekHigh')
		)
	fiftyTwoWeekLow = graphene.Float(
		description = so_desc.desc('fiftyTwoWeekLow'),
		resolver = lambda root, info: raw_round_resolver(root, 'fiftyTwoWeekLow')
		)
	fiftyTwoWeekRange = graphene.String(
		description = so_desc.desc('fiftyTwoWeekRange'),
		resolver = lambda root, info: raw_resolver(root, 'fiftyTwoWeekRange')
		)



def map_options(option_data):
	'''maps given option_data into an Option object'''
	return list( map( lambda data: Option(**data), option_data))

class OptionChain(graphene.ObjectType):
	underlying = graphene.String(
		required=True, description=opc_desc.desc('underlying')
		)
	date = graphene.String(
		required=True, description=opc_desc.desc('expiration'),
		resolver=lambda root, info: date_resolver(root, 'date')
		)
	strikes = graphene.List(
		graphene.String, description=opc_desc.desc('strikes'),
		)
	calls = graphene.List(
		Option, description=opc_desc.desc('calls'),
		)
	puts  = graphene.List(
		Option, description=opc_desc.desc('puts'),
		)
	allOptions = graphene.List(
		Option, description=opc_desc.desc('allOptions')
		)

	def resolve_strikes(self, info):
		return option.strike_prices(self.underlying, self.date)

	def resolve_calls(self, info):
		call_data = option.calls(self.underlying, self.date)
		return map_options(call_data)

	def resolve_puts(self, info):
		put_data = option.puts(self.underlying, self.date)
		return map_options(put_data)

	def resolve_allOptions(self, info):
		return self.resolve_calls(info) +  self.resolve_puts(info)


def default_start():
	return (date.today()-timedelta(days=365)
		).strftime('%m/%d/%y')

def default_end():
	return date.today().strftime('%m/%d/%y')

def map_optionChain(ticker, exp_list):
	'''maps each expiration date to  an OptionChain object
	each OptionChain instance has its own methods to resolve its feilds
	'''
	return list(
		map(lambda date: OptionChain(underlying=ticker, date=date), exp_list)
		)

def mutate_stock_data(data):
	'''changing the data becuase open is reseved in Python '''
	#need to make a copy not to affect the dictionary stored in the cache
	new_data = data.copy()
	new_data['open_'] = new_data.pop('open')
	return new_data

def map_stockPrice(stock_data):
	'''maps stock_stock data to a stockPrice object'''
	return list(map(lambda data: StockPrice(**mutate_stock_data(data)), stock_data))

class Ticker(graphene.ObjectType):
	ticker = graphene.String(
		required=True, description=tik_desc.desc('ticker')
		)
	startDate = graphene.NonNull(
		graphene.String, default_value=default_start(),
		description=tik_desc.desc('startDate')
		)
	endDate = graphene.NonNull(
		graphene.String, default_value=default_end(),
		description=tik_desc.desc('endDate')
		)
	frequency = graphene.String(
		default_value='1d', description=tik_desc.desc('frequency')
		)
	stockPrices = graphene.List(
		StockPrice, description=tik_desc.desc('stockPrices')
		)
	stockOverview = graphene.Field(
		StockOverview, description = tik_desc.desc('stockOverview')
		)
	relatedStocks = graphene.List(
		StockOverview, description = tik_desc.desc('relatedStocks'), 
		)
	calls = graphene.List(
		Option, description=tik_desc.desc('calls')
		)
	puts = graphene.List(
		Option, description=tik_desc.desc('puts')
		)
	optionChains = graphene.List(
		OptionChain, limit = graphene.Int(
		required=False, description= tik_desc.arg_desc('limit')
		),
		description = tik_desc.desc('optionChains')
		)

	def resolve_stockPrices(self, info):
		stock_data = stock.stock_data(**{
		'ticker':self.ticker, 'start_date':self.startDate,
		'end_date':self.endDate, 'frequency':self.frequency,
		})
		return map_stockPrice(stock_data)

	def resolve_stockOverview(self, info):
		stock_data = stock.overview(self.ticker)[0]
		return StockOverview(**stock_data)

	def resolve_relatedStocks(self, info):
		stock_data = stock.relate_tickers(self.ticker)
		return [StockOverview(**data) for data in stock_data]

	def resolve_calls(self, info):
		call_data = option.calls(self.ticker)
		return map_options(call_data)

	def resolve_puts(self, info):
		put_data = option.puts(self.ticker)
		return map_options(put_data)

	def resolve_optionChains(self, info, **kwargs):
		limit = kwargs.get('limit')
		expirations = option.expirations(self.ticker)
		if limit and limit > 0 and limit < len(expirations):
			expirations = expirations[:limit]
		return map_optionChain(self.ticker, expirations)



def map_Tickers(ticker_list, **optional_args):
	'''maps a list of stock tickers to Ticker objects'''
	return list(map(lambda ticker: Ticker(ticker=ticker, **optional_args), ticker_list))

def underlying_expiration(**kwargs):
	return (kwargs.get('underlying'), kwargs.get('expiration'))

def closest_expiration(ticker, exp_date):
	'''returns the closest expiration following or equal to the date provided
		if no date, returns none'''
	if exp_date:
		#maps exp_date to a unix utc timestamp
		exp_utc = string_to_utc(exp_date)
		exp_list = option.expirations(ticker)
		filtered_list = [timestamp for timestamp in exp_list if timestamp >= exp_utc]
		#if their are actually options expiring after the date we selected
		if len(filtered_list) > 0:
			return filtered_list[0]
		#otherwise return the timestamp for the current expiration month
		return exp_list[0]
	return exp_date

#self does not work in the base Query object. Not 100% sure why
class Query(graphene.ObjectType):
	ticker = graphene.Field(
		Ticker,
		ticker=graphene.String(required=True, description=q_desc.arg_desc('ticker')),
		startDate=graphene.String(description=q_desc.arg_desc('startDate')),
		endDate=graphene.String(description=q_desc.arg_desc('endDate')),
		frequency=graphene.String(description=q_desc.arg_desc('frequency')),
		description=q_desc.desc('ticker')
		)
	tickers = graphene.List(
		Ticker,
		tickers=graphene.List(graphene.String, description=q_desc.arg_desc('tickers')),
		startDate=graphene.String(description=q_desc.arg_desc('startDate')),
		endDate=graphene.String(description=q_desc.arg_desc('endDate')),
		frequency=graphene.String(description=q_desc.arg_desc('frequency')),
		description=q_desc.desc('tickers')
		)
	calls = graphene.List(
		Option,
		underlying=graphene.String(required=True, description=q_desc.arg_desc('underlying')),
		expiration=graphene.String(description=q_desc.arg_desc('expiration')),
		description=q_desc.desc('calls')
		)
	puts = graphene.List(
		Option,
		underlying=graphene.String(required=True, description=q_desc.arg_desc('underlying')),
		expiration=graphene.String(description=q_desc.arg_desc('expiration')),
		description=q_desc.desc('puts')
		)

	optionStrikes = graphene.List(
		graphene.Float,
		underlying=graphene.String(required=True, description=q_desc.arg_desc('underlying')),
		expiration=graphene.String(description=q_desc.arg_desc('expiration')),
		description=q_desc.desc('strikes')
		)

	optionExpirationDates = graphene.List(
		graphene.String,
		underlying=graphene.String(required=True, description=q_desc.arg_desc('underlying')),
		description=q_desc.desc('exp_dates')
		)


	def resolve_ticker(self, info, **kwargs):
		'''kwargs: see query arguments'''
		return Ticker(**kwargs)

	def resolve_tickers(self, info, **kwargs):
		'''kwargs: see query arguments'''
		all_args = kwargs
		tickers = all_args.pop('tickers')
		return map_Tickers(tickers, **all_args)

	def resolve_calls(self, info, **kwargs):
		'''kwargs: see query arguments'''
		ticker,  exp = underlying_expiration(**kwargs)
		exp = closest_expiration(ticker, exp)
		call_data = option.calls(ticker, exp)
		return map_options(call_data)

	def resolve_puts(self, info, **kwargs):
		'''kwargs: see query arguments'''
		ticker, exp = underlying_expiration(**kwargs)
		exp = closest_expiration(ticker, exp)
		put_data = option.puts(ticker, exp)
		return map_options(put_data)

	def resolve_optionStrikes(self, info, **kwargs):
		'''kwargs: see query arguments'''
		ticker, exp = underlying_expiration(**kwargs)
		exp = closest_expiration(ticker, exp)
		return option.strike_prices(ticker, exp)

	def resolve_optionExpirationDates(self, info, **kwargs):
		'''kwargs: see query arguments'''
		ticker, _ = underlying_expiration(**kwargs)
		expirations = option.expirations(ticker)
		return list(map(lambda data: strftimestamp(data), expirations))


schema = graphene.Schema(query=Query)
