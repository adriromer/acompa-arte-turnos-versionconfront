#Adrian Romero - Efip 1 Marzo 2020

from flask_restful import Resource, Api, request
from package.model import conn



class Appointments(Resource):
    """Apis de actividades de turnos"""

    def get(self):
        """trae todos los turnos en forma de Json"""

        appointment = conn.execute("SELECT p.*,d.*,a.* from appointment a LEFT JOIN patient p ON a.pat_id = p.pat_id LEFT JOIN doctor d ON a.doc_id = d.doc_id ORDER BY appointment_date DESC").fetchall()
        return appointment

    def post(self):
        """crea un turno asociando paciente y terapista con fecha de turno"""

        appointment = request.get_json(force=True)
        pat_id = appointment['pat_id']
        doc_id = appointment['doc_id']
        appointment_date = appointment['appointment_date']
        appointment['app_id'] = conn.execute('''INSERT INTO appointment(pat_id,doc_id,appointment_date)
            VALUES(?,?,?)''', (pat_id, doc_id,appointment_date)).lastrowid
        conn.commit()
        return appointment



class Appointment(Resource):
    """Api que contiene toda la actividad con un turno unico"""

    def get(self,id):
        """Obtiene un detalles de un turno por su ID"""

        appointment = conn.execute("SELECT * FROM appointment WHERE app_id=?",(id,)).fetchall()
        return appointment


    def delete(self,id):
        """Borra turno por ID"""

        conn.execute("DELETE FROM appointment WHERE app_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Actualiza un turno por ID"""

        appointment = request.get_json(force=True)
        pat_id = appointment['pat_id']
        doc_id = appointment['doc_id']
        conn.execute("UPDATE appointment SET pat_id=?,doc_id=? WHERE app_id=?",
                     (pat_id, doc_id, id))
        conn.commit()
        return appointment