from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_PARAMS = {
    'function': 'TIME_SERIES_MONTHLY',
    'symbol': 'SPY',
    'apikey': ALPHAVANTAGE_API_KEY,
}


@app.route('/', methods=['GET', 'POST'])
def home_page():
    response = requests.get(ALPHAVANTAGE_ENDPOINT, ALPHAVANTAGE_PARAMS)
    data = response.json()['Monthly Time Series']
    prices = {key: value['4. close'] for (key, value) in data.items()}
    print(prices)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
