from flask import flash, render_template, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
import datetime as dt
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/', methods=['GET', 'POST'])
def index():
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
        redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have been registered successfully!")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)


@app.route('/add_stock', methods=['GET', 'POST'])
@login_required
def add_stock():
    stock_name = request.args.get("stock_name")
    print(stock_name)
    return redirect(url_for('index'))
