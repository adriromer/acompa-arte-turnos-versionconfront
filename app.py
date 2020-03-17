#Adrian Romero - Efip 1 Marzo 2020

from package.model import conn
from flask import Flask, send_from_directory, render_template, request, redirect, url_for, session, flash
from flask_restful import Resource, Api, request
from package.patient import Patients, Patient
from package.doctor import Doctors, Doctor
from package.login import login
from package.appointment import Appointments, Appointment
from package.common import Common
import json
from functools import wraps

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='', template_folder='static')

def login_required(f):
    @wraps(f)
    def warps(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
#            Flash("tenes que ingresar primero")
            return redirect(url_for('login'))
    return warps


#secret key hay que moverla a un config file
app.secret_key = "una key muy segura"

api = Api(app)

#api.add_resource(login, '/login')
api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:id>')
api.add_resource(Common, '/common')

# Routes

@app.route('/')
@login_required
def index():
    return app.send_static_file('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Credenciales invalidas'
        else:
            session['logged_in'] = True
#            flash('acabas de ingresar!!')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
#    flash('acabas de salir!!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])

