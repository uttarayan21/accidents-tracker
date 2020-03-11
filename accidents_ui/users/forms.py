from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, Optional
from wtforms import StringField, PasswordField, SubmitField, BooleanField,\
 ValidationError
from accidents_db.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username is already taken please something else')

class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=5, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class EditForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=5, max=50),
                                                   Optional()])

    submit = SubmitField('Update Account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username is already taken please try something else')

