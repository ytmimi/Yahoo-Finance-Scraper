import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))

from utc_converter import UTC_Converter
import datetime as dt
import unittest



class Test_Time_Conversion(unittest.TestCase):
	def setUp(self):
		self.utc = UTC_Converter()


	def test_utc_string_right_fmt(self):
		# 1530331200 = 06/30/2018 @ 4:00am (UTC)
		# 1498795200 = 06/30/2017 @ 4:00am (UTC)
		utc = self.utc('06/30/2018', fmt_str='%m/%d/%Y')
		self.assertEqual(utc, 1530331200)

	def test_utc_string_wrong_fmt(self):
		with self.assertRaises(ValueError) as ve:
			utc = self.utc('06/30/2018', fmt_str='%Y/%m/%d')
			self.assertEqual(ve.msg, 'The fmt_str did not match the date provided.')

	def test_utc_string_None_fmt(self):
		utc = self.utc('06/30/2018', fmt_str=None)
		self.assertEqual(utc, 1530331200)

	def test_utc_incorrect_fmt_type(self):
		with self.assertRaises(ValueError) as ve:
			utc = self.utc('06/30/2018', fmt_str=1)
			self.assertEqual(ve.msg, 'The fmt_str did not match the date provided.')

	def test_utc_string_default(self):
		utc = self.utc('06/30/2018')
		self.assertEqual(utc, 1530331200)

	def test_utc_string_default_error(self):
		with self.assertRaises(ValueError) as ve:
			utc = self.utc('2018, June 30')
			self.assertEqual(ve.msg, 'Unable to parse string. Please supply the fmt_str kwarg.')

	def test_utc_from_datetime(self):
		# 1498795200 = 06/30/2017 @ 4:00am (UTC)
		date = dt.datetime.strptime('06/30/2017','%m/%d/%Y')
		utc = self.utc(date)
		self.assertEqual(utc, 1498795200)

	def test_utc_from_date(self):
		# 1498795200 = 06/30/2017 @ 4:00am (UTC)
		date = dt.datetime.strptime('06/30/2017','%m/%d/%Y').date()
		utc = self.utc(date)
		self.assertEqual(utc, 1498795200)


if __name__ == '__main__':
	unittest.main()











