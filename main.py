from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from app.forms import LoginForm
import datetime as dt
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    stocks = {
        'S&P 500': {
            "points": 65, "percentage": 2.5, "ticker": "SPX:IND"},
        'FTSE 100': {
            "points": 15, "percentage": 2.1, "ticker": "UKX:IND"},
        'Nikkei 225': {
            "points": -245, "percentage": -1.2, "ticker": "NKY:IND"},
    }

    bonds = {
        'Global Aggregate': {
            "points": 0.05, "percentage": 1, "ticker": "LEGATRUU:IND"},
        'US Aggregate': {
            "points": 0.11, "percentage": 2.1, "ticker": "LBUSTRUU:IND"},
        'Asia-Pacific': {
            "points": -0.1, "percentage": -1.2, "ticker": "LAPCTRJU:IND"},
    }

    date = dt.datetime.now(dt.timezone.utc).strftime("%d-%m-%Y")

    return render_template("index.html", stocks=stocks, bonds=bonds, date=date)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run()
