#Adrian Romero - Efip 1 Marzo 2020

from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """Api comun para resolver datos"""

    def get(self):
        """Obtiene numero de pacientes activos, numero de terapistas y turnos del mes para el dashboard principal """

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM appointment").fetchone()
        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        return getPatientCount