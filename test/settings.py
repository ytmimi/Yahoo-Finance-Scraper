import os

#DEFINE PATHS
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOCK_PATH = os.path.join(BASE_PATH, 'mock_data')

#VARIABLE USED TO TOGGLE LIVE TESTS
LIVE_TEST = False

#CONSTATNS USED TO GENERATE MOCK DATA
MOCK_DATA_START = '09/26/2017'
MOCK_DATA_END = '09/26/2018'


STOCK_DATA_1D = os.path.join(MOCK_PATH, 'JWN_1d.json')
STOCK_DATA_1WK = os.path.join(MOCK_PATH,'JWN_1wk.json')
STOCK_DATA_1MO = os.path.join(MOCK_PATH,'JWN_1mo.json')

OPTION_DATA_1 = os.path.join(MOCK_PATH,'JWN_1539907200.json')
OPTION_DATA_2 = os.path.join(MOCK_PATH,'JWN_1542326400.json')
OPTION_DATA_3 = os.path.join(MOCK_PATH,'JWN_1547769600.json')
OPTION_DATA_4 = os.path.join(MOCK_PATH,'JWN_1555545600.json')
OPTION_DATA_5 = os.path.join(MOCK_PATH,'JWN_1579219200.json')
OPTION_DATA_6 = os.path.join(MOCK_PATH,'JWN_1610668800.json')