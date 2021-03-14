from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_migrate import Migrate
from app.forms import LoginForm
import datetime as dt
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


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
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    return render_template("register.html", form=form)

if __name__ == '__main__':
    app.run()
