#Adrian Romero - Efip 1 Marzo 2020

import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
print("debug para confirmar la conexion - info DB ", config)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """Funcion para formatear el Json cuando saco datos de la base"""

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        print("print de las queries a la base convertidas en Json\n", d)
    return d


conn.row_factory = dict_factory



conn.execute('''CREATE TABLE if not exists patient
(pat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_first_name TEXT NOT NULL,
pat_last_name TEXT NOT NULL,
pat_insurance_no TEXT NOT NULL,
pat_ph_no TEXT NOT NULL,
pat_date DATE DEFAULT (datetime('now','localtime')),
pat_address TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists doctor
(doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
doc_first_name TEXT NOT NULL,
doc_last_name TEXT NOT NULL,
doc_ph_no TEXT NOT NULL,
doc_date DATE DEFAULT (datetime('now','localtime')),
doc_address TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists appointment
(app_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_id INTEGER NOT NULL,
doc_id INTEGER NOT NULL,
appointment_date DATE NOT NULL,
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id));''')