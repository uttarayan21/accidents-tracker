from flask import Blueprint, redirect, url_for,\
 render_template, flash, request, abort
from flask_login import logout_user, login_user, login_required, current_user

from accidents_ui import db, bcrypt
from accidents_ui.users.forms import LoginForm, RegistrationForm, EditForm
from accidents_db.models import User

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).\
                    decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page)\
                if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('main.home'))


@users.route('/users/<username>')
def account(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('account.html', title='Account', user=user)
    else:
        flash(f'No user exists with the username {username}', 'danger')
        return redirect(url_for('main.home'))


@users.route("/users/<username>/edit", methods=['GET', 'POST'])
@login_required
def edit_account(username):
    user = User.query.filter_by(username=username).first()
    if user == current_user:
        form = EditForm()
        if form.validate_on_submit():
            db.session.commit()
            flash('Accout Info updated successfully', 'success')
            return redirect(url_for('users.account',
                                    username=current_user.username))
        return render_template('edit_account.html', title='Edit', form=form)
    else:
        return abort(403)
