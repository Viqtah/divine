from flask import Flask
from patient import Patient
from flask import Flask, render_template, request, redirect, url_for
from psycopg2 import *

app = Flask(__name__)


@app.route('/')
def home():

    allpatients = Patient.select()

    return render_template("index.html", displaypatients=allpatients)


# CALL THE FORM

@app.route("/addpatient")
def patient():
    return render_template("addpatient.html")


@app.route("/savepatient", methods=["POST"])
def savePatient():
    Patient.create(fname=request.form['form_fname'],
                   lname=request.form['form_lname'],
                   contact=request.form['form_contact'],
                   history=request.form['form_history'],
                   )

    allpatients = Patient.select()

    return redirect(url_for("home"))


# CALL THE FORM
@app.route("/updatepatient/<id>", methods=['POST'])
def updatePatient(id):
    # fetch the patient
    emp = Patient.select().where(Patient.patient_id == id).get()

    # update the patient
    emp.fname = request.form['form_fname']
    emp.lname = request.form['form_lname']
    emp.contact = request.form['form_contact']
    emp.history = request.form['form_history']
    emp.save()

    return redirect(url_for("home"))


@app.route("/deletepatient/<id>", methods=["GET"])
def delPatient(id):
    # fetch the patient using their id

    emp = Patient.select().where(Patient.patient_id == id).get()
    emp.delete_instance()
    return redirect(url_for("home"))


app.run
if __name__ == "__main__":
    app.run(debug=True, port=5005)
