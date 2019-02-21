from peewee import *
from patient import *
try:
    db = PostgresqlDatabase('Hospital', user='postgres', password='Stima101', host='localhost', port=5432)
    print ('connection success')
except:
    print ('connection fail')


    def searchPatient(self):
        self.conn.execute("SELECT * FROM patients WHERE patient_id == 2")
        found_rows = self.conn.fetchall()
        return found_rows
        print (found_rows

x = searchPatient(2)
print(x)
)