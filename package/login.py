
from flask_restful import Resource, Api, request
from package.model import conn

class login(Resource):

    def login(self):

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            doctors = conn.execute(
                "SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password)")
            return doctors
            # Fetch one record and return result
            # account = cursor.fetchone()

