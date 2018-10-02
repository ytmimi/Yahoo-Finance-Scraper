'''
To avoid clutteing schema.py with descriptions, they have all been defined in this file.
'''
#constants that apear in multiple places
TICKER = 'A valid stock ticker.'
UNDERLYING = 'The ticker of the underlying stock.'
OPTION_EXPIRATION = 'The expiration date of the option contract.'


class Description:
	'''
	A Description class should define a description for all the fields used
	in a corresponding graphQL(graphene) ObjectType. If certain fields require additional arguments,
	each argument should be included as a class atribute of an associaated Meta class.
	'''
	@classmethod
	def desc(cls, attr):
		return getattr(cls, attr)

	@classmethod
	def arg_desc(cls, arg):
		return getattr(cls.Meta, arg)

class Stock_Price_Description(Description):
	date = 'The date when the stock traded.'
	open_ = 'The share price when the market opened.'
	high = 'The highest share price on the given day.'
	low = 'The lowest share price on the given day.'
	close = 'The share price when the market closed.'
	volume = 'The total amount of shares traded during the day.'
	adjclose = 'The close price adjusted for dividends and stock splits.'


class Option_Description(Description):
	contractSymbol = 'A unique identifier giving information on the type, expiration, and strike of an option contract.'
	expiration = OPTION_EXPIRATION
	change = 'Decimal value representing the change in price.'
	lastPrice = 'The last price at which a contract was bought and sold.'
	inTheMoney = 'Defines whether the option contract has intrinsic value.'
	impliedVolatility = 'A measure of the markets expectation of price movements in the underlying asset prior to the option\'s expiration.'
	openInterest = 'The number of open contracts for the underlying at the given strike'
	percentChange = 'Percentage representing the change in price.'
	bid = 'The price offered to buy the option.'
	ask = 'The price offered to sell the option.'
	volume = 'the total number of contracts for each strike that traded during the day.'
	lastTradeDate = 'Date showing the last time the contract was traded.'
	currency =  'The currency the option contract trades in.'
	strike = 'The price at which the underlying asset can be bought or sold.'
	contractSize = 'The units of underlying that is represented by one contract. Typically one option contract covers 100 shares of stock.'
	optionType = 'Indecates whether the option is a call or a put.'

class StockOverview(Description):
	symbol = 'The ticker for the stock.'
	openToday = 'Todays price when the stock opened.'
	highToday = 'The highest price the stock reached today.'
	lowToday = 'The lowest price the stock reached today.'
	closePrevious = 'The last trading days closing price.'
	recentPrice = 'The most recent stock price available.'
	volumeToday = 'The number of shares traded today.'
	sharesOutstanding = 'The total number of shares availabe.'
	marketCap = 'The value of a companies equity.'
	fiftyTwoWeekHigh = 'The stockes highest price over the last year.'
	fiftyTwoWeekLow = 'The stocks lowest price over the last year.'
	fiftyTwoWeekRange = 'The low-high range over the last year.'


class Option_Chain_Description(Description):
	underlying = UNDERLYING
	expiration = OPTION_EXPIRATION
	strikes = 'A list of all available stike prices for the given expiration date.'
	calls = 'A list of all call options for the given expiration date.'
	puts = 'A list of all put options for the given expiration date.'
	allOptions = 'A list of all call and put options for the given expiration date.'


class Ticker_Description(Description):
	ticker = TICKER
	startDate = 'The first date requested for stock data.'
	endDate = 'The last date requested for stock data.'
	frequency = 'Determins the frequency of stock price data. 1d for daily, 1wk for weekly, and 1mo for monthly '
	stockPrices = 'A list of stock price data.'
	stockOverview = 'Basic information on the stock price performace on the day and over the year' 
	relatedStocks ='Current and yearly performance information on a list of related stock tickers' 
	calls = 'A list of near term call options for the given stock'
	puts = 'A list of near term put options for the given stock.'
	optionChains = 'A list of all option contracts that expire on the same day.'

	class Meta:
		limit = 'Limit the number of results returned. Must be > 0.'


class Query_Description(Description):
	ticker = (
		'Data for a single stock.'
		)

	tickers = (
		'Data for a list of stocks.'
		)

	calls = (
		'Data on all call options for the given (optional) expiration date will be returned. '
		'By default calls from the current expiration month will be returned.'
		'If the data provided is not an exact expiration date the closest expiration following the '
		'provided date with be returned. If there aren\'t any options expiring after the provided date, '
		'the query will resolve to its default behavior.'
		)

	puts = (
		'Data on all put options for the given (optional) expiration date will be returned. '
		'By default puts from the current expiration month will be returned.'
		'If the data provided is not an exact expiration date the closest expiration following the '
		'provided date with be returned. If there aren\'t any options expiring after the provided date, '
		'the query will resolve to its default behavior.'
		)

	strikes = (
		'A list of all available strikes for the given expiration date will be returned.'
		)

	exp_dates = (
		'A list of all currently available option expiration dates are return in mm/dd/yy format.'
		)
	class Meta:
		ticker = TICKER
		tickers = 'A list of valid stock tickers.'
		startDate = 'A date in the form mm/dd/yyyy. Defaults to 365 days prior to the current date.'
		endDate = 'A date in the form mm/dd/yyyy. Defaults to the current date.'
		frequency = 'A given frequency for stock data. Values must be one of the following: 1d,  1wk, or, 1mo.'
		underlying = UNDERLYING
		expiration = 'The expiration date of the option contract in mm/dd/yyyy format. Defauts to the closest expiration.'



if __name__ == '__main__':
	print(Ticker_Description.arg_description('limit'))
