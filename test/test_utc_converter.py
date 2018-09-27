import os
import sys
import datetime as dt
from pytz import UTC

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(path, 'yahoo_finance'))
import utc_converter as utc_c

import pytest

@pytest.fixture(scope='module')
def dt_string():
	return '09/28/2018' 

@pytest.fixture(scope='module')
def dt_date():
	return dt.date(2018, 9, 28)
	
@pytest.fixture(scope='module')
def dt_datetime():
	return dt.datetime(2018, 9, 28, tzinfo=UTC)

@pytest.fixture(scope='module')
def dt_error_str():
	return '2018/09/28'

@pytest.fixture(scope='module')
def dt_timestamp():
	#utc imestamp for 09/28/2018
	return 1538092800

def test_default_str_fmt(dt_datetime):
	for code in utc_c.time_codes:
		date_str = dt_datetime.strftime(code)
		assert isinstance(utc_c._default_str_formats(date_str), dt.datetime)

def test_default_str_fmt_error(dt_datetime):
	#the format of '%d/%m/%Y' is not a default format
	date_str = dt_datetime.strftime('%d/%m/%Y')
	with pytest.raises(ValueError) as error:
		utc_c._default_str_formats(date_str)
	assert str(error.value) == 'Unable to parse string. Please supply the fmt_str kwarg.'

def test_custom_str_fmt(dt_string, dt_datetime):
	dt_str = utc_c._custom_str_format(dt_string, '%m/%d/%Y')
	assert dt_str == dt_datetime

def test_custom_str_fmt_error(dt_string):
	with pytest.raises(ValueError) as error:
		utc_c._custom_str_format(dt_string, '%Y/%m/%d')
	# assert str(error.value) == 'The fmt_str did not match the date provided.'

def test_date_string_to_utc(dt_string, dt_timestamp):
	assert utc_c._date_string_to_utc(dt_string) == dt_timestamp

def test_date_string_to_utc_error(dt_error_str):
	with pytest.raises(ValueError) as error:
		utc_c._date_string_to_utc(dt_error_str)
	# assert str(error.value) == 'Unable to parse string. Please supply the fmt_str kwarg.'

def test_date_string_to_utc_custom_fmt(dt_error_str, dt_timestamp):
	assert utc_c._date_string_to_utc(
		dt_error_str, '%Y/%m/%d') == dt_timestamp

def test_date_string_to_utc_custom_fmt_error(dt_error_str):
	with pytest.raises(ValueError) as error:
		#actual format is '%Y/%m/%d'
		utc_c._date_string_to_utc(dt_error_str, '%m/%d/%y')
	# assert str(error.value) == 'The fmt_str did not match the date provided.'

def test_date_to_utc(dt_date, dt_timestamp):
	assert utc_c._date_to_utc(dt_date) == dt_timestamp

def test_datetime_to_utc(dt_datetime, dt_timestamp):
	assert utc_c._date_to_utc(dt_datetime) == dt_timestamp

def test_utc_with_date(dt_date, dt_timestamp):
	assert utc_c.utc(dt_date) == dt_timestamp

def test_utc_with_datetime(dt_datetime, dt_timestamp):
	assert utc_c.utc(dt_datetime) == dt_timestamp

def test_utc_with_default_str(dt_string, dt_timestamp):
	assert utc_c.utc(dt_string) == dt_timestamp

def test_utc_custom_fmt(dt_error_str, dt_timestamp):
	assert utc_c.utc(dt_error_str, fmt_str='%Y/%m/%d') == dt_timestamp

def test_utc_wrong_input(dt_timestamp):
	with pytest.raises(ValueError) as error:
		utc_c.utc(dt_timestamp,)
	# assert str(error.value) == 'date must be a date string, datetime object, or date object'

def test_date_str_from_timestamp_default(dt_timestamp, dt_string):
	assert utc_c.date_str_from_timestamp(dt_timestamp) == dt_string
	
def test_date_str_from_timestamp_custom_fmt(dt_timestamp, dt_error_str):
	assert utc_c.date_str_from_timestamp(
		dt_timestamp, fmt_str='%Y/%m/%d') == dt_error_str


if __name__ == '__main__':
	pytest.main()











