from flask_wtf import FlaskForm
from wtforms.validators import Optional, DataRequired, Length
from wtforms import StringField, SelectField, SubmitField


class ViewRecords(FlaskForm):
    tablelist = [ ('car', 'Car'),
                  ('person', 'Person'),
                  ('owns', 'Owns'),
                  ('accidents', 'Accident')]
    query   = StringField('Search', validators=[Optional(), Length(max=100)])
    db      = SelectField('Database', choices=tablelist)
    search  = SubmitField('Search')
