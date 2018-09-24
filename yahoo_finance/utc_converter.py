import datetime as dt


class UTC_Converter():
	time_codes = ['%m/%d/%Y', '%m-%d-%Y','%b %d, %Y',]
	
	def __call__(self, date, offset=dt.timedelta(), fmt_str=None):
		if type(date) == dt.datetime or type(date) == dt.date:
			utc = self.date_to_utc(date, offset)
		elif type(date) == str:
			utc = self.parse_date_string(date, offset, fmt_str)
		return int(utc)

	def parse_date_string(self, date, offset, fmt_str=None):
		'''
		date: a date string
		offset: timedelta
		'''
		if fmt_str != None:
			date = self.custom_str_format(date, fmt_str)
		else:
			date = self.default_str_formats(date)
		stamp = (date + offset).timestamp()
		return stamp

	def default_str_formats(self, date):
		found_format = False
		i = 0
		#either you find a format or you get to the end of the format list 
		while ((i < len(self.time_codes)) and not found_format):
			try:
				date = dt.datetime.strptime(date, self.time_codes[i])
				found_format = True
			except Exception as e:
				i+=1
		if not found_format:
			raise ValueError('Unable to parse string. Please supply the fmt_str kwarg.')	
		return date

	@staticmethod
	def custom_str_format(date, fmt_str):
		''' 
		date: string representing a date	
		fmt_str: a proper datetime formate used to parse the date
		'''
		try:
			date = dt.datetime.strptime(date, fmt_str)
			return date
		except Exception as e:
			raise ValueError('The fmt_str did not match the date provided.')

	@staticmethod
	def date_to_utc(date, offset):
		date_str = date.strftime('%m/%d/%Y')
		date_obj = dt.datetime.strptime(date_str, '%m/%d/%Y')
		return (date_obj + offset).timestamp()

	@staticmethod
	def date_str_from_timestamp(timestamp, fmt_str='%m/%d/%Y'):
		date = dt.datetime.fromtimestamp(timestamp)
		return date.strftime(fmt_str)
			
