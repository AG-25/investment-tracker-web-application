from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


tracked_securities = db.Table('tracked_securities',
    db.Column('security_id', db.Integer, db.ForeignKey('security.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tracked_securities = db.relationship('Security', secondary=tracked_securities,
                                         backref=db.backref('users', lazy='dynamic'),
                                         lazy='dynamic')

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Security(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    security_name = db.Column(db.String(64), index=True, unique=True)
    region = db.Column(db.String(64))
    price = db.Column(db.Integer)
    date_last_checked = db.Column(db.DateTime)

    def __repr__(self):
        return "<Security: {}>".format(self.security_name)
