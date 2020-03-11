# accident/accidents_db

from accidents_db import db
from flask_login import UserMixin
from accidents_ui import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)


class Person(db.Model):
    __tablename__ = 'people'
    driver_id   = db.Column(db.String(50), primary_key = True)
    name        = db.Column(db.String(100), nullable = False)
    address     = db.Column(db.String(50), nullable = False)
   
    def __repr__(self):
        return f"Driver ID: {self.driver_id} | Name: {self.name} | Address: {self.address}"


class Car(db.Model):
    __tablename__ = 'cars'
    reg_no      = db.Column(db.String(50), primary_key = True)
    model       = db.Column(db.String(50), nullable = False)
    year        = db.Column(db.String(50), nullable = False)


class Accident(db.Model):
    __tablename__ = 'accidents'
    report_no   = db.Column(db.String(50), primary_key = True)
    date        = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    location    = db.Column(db.String(100), nullable = False)


class Owns(db.Model):
    __tablename__ = 'owns'
    driver_id   = db.Column(db.String(50), db.ForeignKey('people.driver_id'), primary_key = True)
    reg_no      = db.Column(db.String(50), db.ForeignKey('cars.reg_no'), nullable = False)


class Participated(db.Model):
    __tablename__ = 'participated'
    driver_id   = db.Column(db.String(50), db.ForeignKey('people.driver_id'), primary_key = True)
    reg_no      = db.Column(db.String(50), db.ForeignKey('cars.reg_no'), nullable = False)
    report_no   = db.Column(db.String(50), db.ForeignKey('accidents.report_no'), nullable = False)
    damage_amt  = db.Column(db.String(50), nullable = False)
