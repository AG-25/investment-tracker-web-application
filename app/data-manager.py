import os

ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'SPY',
    'apikey': ALPHAVANTAGE_API_KEY,
}
