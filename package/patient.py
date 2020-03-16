#Adrian Romero - Efip 1 Marzo 2020


from flask_restful import Resource, Api, request
from package.model import conn




class Patients(Resource):

    """ Clase que contiene de los pacientes """

    def get(self):
        """Api que obtiene todos los pacientes de la base"""

        patients = conn.execute("SELECT * FROM patient  ORDER BY pat_date DESC").fetchall()
        return patients



    def post(self):
        """Api para agregar un paciente a la base"""

        patientInput = request.get_json(force=True)
        pat_first_name=patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInput['pat_ph_no']
        pat_address = patientInput['pat_address']
        patientInput['pat_id']=conn.execute('''INSERT INTO patient(pat_first_name,pat_last_name,pat_insurance_no,pat_ph_no,pat_address)
            VALUES(?,?,?,?,?)''', (pat_first_name, pat_last_name, pat_insurance_no,pat_ph_no,pat_address)).lastrowid
        conn.commit()
        return patientInput

class Patient(Resource):
    """Contiene todas las apis que ejecutan actividades con un solo paciente"""

    def get(self,id):
        """api que obtiene todos los detalles de un paciente por ID"""

        patient = conn.execute("SELECT * FROM patient WHERE pat_id=?",(id,)).fetchall()
        return patient

    def delete(self,id):
        """Api que borra un paciente por su ID"""

        conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Api que actualiza un paciente por su id"""

        patientInput = request.get_json(force=True)
        pat_first_name = patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInput['pat_ph_no']
        pat_address = patientInput['pat_address']
        conn.execute("UPDATE patient SET pat_first_name=?,pat_last_name=?,pat_insurance_no=?,pat_ph_no=?,pat_address=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name, pat_insurance_no,pat_ph_no,pat_address,id))
        conn.commit()
        return patientInput