from flask import Blueprint, flash, redirect, url_for, request,\
    render_template
from accidents_ui import db
from accidents_db.models import Person, Car, Accident, Owns, Participated
from accidents_ui.database.forms import AddCar, AddPerson, AddOwner, AddAccident, AddParticipation
from accidents_ui.database.views import ViewRecords
from flask_login import login_required

database = Blueprint('database', __name__)


@database.route('/add', methods=['GET', 'POST'])
@login_required
def add_records():
    return render_template('add_records.html', title="Add Records")


@database.route('/view', methods=['GET'])
def view_records():
    query = request.args.get('query', type=str)
    query_db = request.args.get('db', type=str)
    form = ViewRecords(request.args)

    if query_db is None:
        return render_template('view_records.html', form=form, results=None)
    elif query_db == 'person':
        if query:
            results = Person.query.filter(Person.name.contains(form.query.data) | Person.address.contains(form.query.data)).all()
        else:
            results = Person.query.all()
    elif query_db == 'car':
        if query:
            results = Car.query.filter(Car.model.contains(form.query.data) | Car.reg_no.contains(form.query.data)).all()
        else:
            results = Car.query.all()
    elif query_db == 'accidents':
        if query:
            results = Accident.query.filter(Accident.location.contains(form.query.data) | Accident.report_no.contains(form.query.data))
        else:
            results = Accident.query.all()
        print(results)
    elif query_db == 'owns':
        if query:
            results = Owns.query.filter(Owns.reg_no.contains(form.query.data) | Owns.driver_id.contains(form.query.data))
        else:
            results = Owns.query.all()
    elif query_db == 'participation':
        if query:
            results = Participated.query.filter(Participated.reg_no.contains(form.query.data) | Participated.driver_id.contains(form.query.data))
        else:
            results = Participated.query.all()
    return render_template('view_records.html', form=form, results=results)


@database.route("/", methods=['GET'])
def home():
    return render_template('database.html', title="Manager")


@database.route("/add/car", methods=['GET', 'POST'])
@login_required
def add_car():
    form = AddCar()
    if form.validate_on_submit():
        car = Car(reg_no=form.reg_no.data, model=form.model.data, year=form.year.data)
        db.session.add(car)
        db.session.commit()
        flash('Car added successfully', 'success')
        return redirect(url_for('database.add_car'))
    return render_template('add_car.html', form=form, title="Add Car")


@database.route('/add/person', methods=['GET', 'POST'])
@login_required
def add_person():
    form = AddPerson()
    if form.validate_on_submit():
        person = Person(driver_id=form.driver_id.data, name=form.name.data, address=form.address.data)
        db.session.add(person)
        db.session.commit()
        flash("Person added succesfully", "success")
        return redirect(url_for('database.add_person'))
    return render_template('add_person.html', form=form, title="Add person")


@database.route('/add/owner', methods=['GET', 'POST'])
@login_required
def add_owner():
    form = AddOwner()
    if form.validate_on_submit():
        owner = Owns(driver_id=form.driver_id.data, reg_no=form.reg_no.data)
        db.session.add(owner)
        db.session.commit()
        flash("Owner added successfully", 'success')
        return redirect(url_for('database.add_owner'))
    # else:
    #     flash("Failed to add Owner", 'danger')

    return render_template('add_owner.html', form=form, title="Add Owner")


@database.route('/add/participation', methods=['GET', 'POST'])
@login_required
def add_participation():
    form = AddParticipation()
    if form.validate_on_submit():
        participation = Participated(driver_id=form.driver_id.data, reg_no=form.reg_no.data, report_no=form.report_no.data, damage_amt=form.damage_amt.data)
        db.session.add(participation)
        db.session.commit()
        flash("Added Participation successfully", 'success')
        return redirect(url_for('database.add_participation'))
    return render_template('add_participation.html', form=form, title="Add Participation")


@database.route('/add/accident', methods=['GET', 'POST'])
@login_required
def add_accident():
    form = AddAccident()
    if form.validate_on_submit():
        accident = Accident(report_no=form.report_no.data, location=form.location.data)
        db.session.add(accident)
        db.session.commit()
        flash("Added accident successfully", 'success')
        return redirect(url_for('database.add_accident'))
    print("WTF is happening")
    return render_template('add_accident.html', form=form, title="Add Accident")
