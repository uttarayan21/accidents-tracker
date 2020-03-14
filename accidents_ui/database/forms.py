from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SelectField, SubmitField, IntegerField, ValidationError

from accidents_db.models import Person, Car, Owns, Accident
# from flask_login import current_user

class AddPerson(FlaskForm):
    driver_id = StringField('Driver ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    address = StringField('Address', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Person')

    def validate_driver_id(self, driver_id):
        person = Person.query.filter_by(driver_id=driver_id.data).first()
        if person:
            raise ValidationError('Driver ID is already present')


class AddCar(FlaskForm):
    reg_no = StringField('Registration Number', validators=[DataRequired()])
    model = StringField('Model Number', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    submit = SubmitField('Add Car')

    def validate_reg_no(self, reg_no):
        car = Car.query.filter_by(reg_no=reg_no.data).first()
        if car:
            raise ValidationError('Car with that registration already exists')


class AddOwner(FlaskForm):
    def __init__(self):
        super(AddOwner, self).__init__()
        self.driver_id.choices = [(i[0], i[1] + ' (' + str(i[0]) + ')') for i in Person.query.with_entities(Person.driver_id, Person.name).all()]
        self.reg_no.choices = [(i[0], i[1] + ' (' + str(i[0]) + ')') for i in Car.query.with_entities(Car.reg_no, Car.model).all()]
    driver_id = SelectField('Driver Id', validators=[DataRequired()])
    reg_no = SelectField('Registration Number', validators=[DataRequired()])
    submit = SubmitField('Add Owner')

    def validate_driver_id(self, driver_id):
        person = Person.query.filter_by(driver_id=driver_id.data).first()
        if not person:
            raise ValidationError('Driver ID not found')
        person = Owns.query.filter_by(driver_id=driver_id.data).first()
        if person:
            raise ValidationError('Person already owns a car')

    def validate_reg_no(self, reg_no):
        car = Car.query.filter_by(reg_no=reg_no.data).first()
        if not car:
            raise ValidationError('Car with that registration was not found')
        car = Owns.query.filter_by(reg_no=reg_no.data).first()
        if car:
            raise ValidationError('Car with that registration is already owned')


class AddAccident(FlaskForm):
    report_no = StringField('Report Number', validators=[DataRequired()])
    location = StringField('Location Of Accident', validators=[DataRequired()])

    submit = SubmitField('Add Accident')
    
    def validate_report_no(self, report_no):
        accident = Accident.query.filter_by(report_no=report_no.data).first()
        if accident:
            raise ValidationError("A accident already happened with that report number")

class AddParticipation(FlaskForm):
    def __init__(self):
        super(AddParticipation, self).__init__()
        self.driver_id.choices = [(i[0], i[1] + ' (' + str(i[0]) + ')') for i in Person.query.with_entities(Person.driver_id, Person.name).all()]
        self.reg_no.choices = [(i[0], i[1] + ' (' + str(i[0]) + ')') for i in Car.query.with_entities(Car.reg_no, Car.model).all()]
        self.report_no.choices = [(i[0], i[1] + ' ( At ' + str(i[1]) + ' on ' + str(i[2])) for i in Accident.query.with_entities(Accident.report_no, Accident.location, Accident.date).all()]

    driver_id = SelectField('Driver ID', validators=[DataRequired()])
    reg_no = SelectField('Registration Number', validators=[DataRequired()])
    report_no = SelectField('Accident Report Number', validators=[DataRequired()])
    damage_amt = IntegerField('Damage Amount', validators=[DataRequired()])
    submit = SubmitField('Add Participation')

    def validate_driver_id(self, driver_id):
        person = Person.query.filter_by(driver_id=driver_id.data).first()
        if not person:
            raise ValidationError('Driver ID not found')
        person = Owns.query.filter_by(driver_id, driver_id.data).first()
        if person:
            raise ValidationError('Person already owns a car')

    def validate_reg_no(self, reg_no):
        car = Car.query.filter_by(reg_no=reg_no.data).first()
        if not car:
            raise ValidationError('Car with that registration was not found')
        car = Owns.query.filter_by(reg_no=reg_no.data).first()
        if car:
            raise ValidationError('Car with that registration is already owned')

class EditForm(FlaskForm):
    driver_id = StringField('Driver ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    address = StringField('Address', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Person')

    def validate_driver_id(self, driver_id):
        person = Person.query.filter_by(driver_id=driver_id.data).first() 
        if person:
            if not person.driver_id == driver_id.data:
                raise ValidationError('Driver ID is already present')

