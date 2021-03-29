import os
import requests


class DataManager:
    def __init__(self):
        self.alpha_api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        self.alpha_api_endpoint = "https://www.alphavantage.co/query"

    def search_stock(self, stock_description):
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": stock_description,
            "apikey": self.alpha_api_key,
        }
        response = requests.get(self.alpha_api_endpoint, params)
        return response.json()
