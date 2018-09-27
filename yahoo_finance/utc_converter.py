import datetime as dt
from pytz import UTC

time_codes = ['%m/%d/%Y', '%m/%d/%y', '%m-%d-%Y','%b %d, %Y',]


def date_str_from_timestamp(timestamp, fmt_str='%m/%d/%Y'):
	date = dt.datetime.utcfromtimestamp(timestamp)
	return date.strftime(fmt_str)

def utc(date, fmt_str=None):
	'''converts either a date or a string to utc '''
	if type(date) == dt.datetime or type(date) == dt.date:
		utc = _date_to_utc(date)
	elif type(date) == str:
		utc = _date_string_to_utc(date, fmt_str)
	else:
		raise ValueError('date must be a date string, datetime object, or date object')
	return int(utc)

def _date_string_to_utc(date, fmt_str=None):
	'''
	returns a timestamp
	date: a date string
	offset: timedelta
	'''
	if fmt_str != None:
		date = _custom_str_format(date, fmt_str)
	else:
		date = _default_str_formats(date)
	return date.replace(tzinfo=UTC).timestamp()

def _default_str_formats(date):
	found_format = False
	i = 0
	#either you find a format or you get to the end of the format list 
	while ((i < len(time_codes)) and not found_format):
		try:
			date = dt.datetime.strptime(date, time_codes[i]).replace(tzinfo=UTC)
			found_format = True
		except Exception as e:
			i+=1
	if not found_format:
		raise ValueError('Unable to parse string. Please supply the fmt_str kwarg.')	
	return date

def _custom_str_format(date, fmt_str):
	''' 
	parses dates using a custom format returns a datetime object
	date: string representing a date	
	fmt_str: a proper datetime formate used to parse the date
	'''
	try:
		date = dt.datetime.strptime(date, fmt_str)
		return date.replace(tzinfo=UTC)
	except Exception as e:
		raise ValueError('The fmt_str did not match the date provided.')
	
def _date_to_utc(date):
	#takes a date or datetime object and returns a timestamp
	date_str = date.strftime('%m/%d/%Y')
	date_obj = dt.datetime.strptime(date_str, '%m/%d/%Y')
	return date_obj.replace(tzinfo=UTC).timestamp()




if __name__ == '__main__':
	print(_date_string_to_utc('10/20/2013'))
	print(_date_string_to_utc('10/20/2014'))

