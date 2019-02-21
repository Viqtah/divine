from peewee import *
import datetime

try:
    db = PostgresqlDatabase('Hospital', user='postgres', password='Stima101', host='localhost', port=5432)
    print ('connection success')
except:
    print ('connection fail')

class Patient(Model):

    patient_id = PrimaryKeyField()
    fname = CharField('100')
    lname = CharField('100')
    contact= CharField()
    history= TextField()
    year = IntegerField(default=datetime.datetime.now().year)
    patient_no = CompositeKey('patient_id', 'year')


    class Meta:
        database = db #  This model uses the "Hospital.db" database.
        table_name_='patients'

Patient.create_table(fail_silently= True)
