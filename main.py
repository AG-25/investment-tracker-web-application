from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from app.forms import LoginForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run()
