
from wtforms import Form, StringField, SelectField

class PatientSearchForm(Form):
    choices = [('patient_id', 'patient_id'),
               ('contact', 'contact'),
               ('fname', 'fname')]
    select = SelectField('Search for patient:', choices=choices)
    search = StringField('')