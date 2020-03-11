
from flask import Blueprint, redirect, url_for, render_template
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return redirect(url_for('database.home'))
    # return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html')
