# Sistema de Turnos para Centro de terapias Acompa-Arte

Systema desarrollado en Python:
 - FrameWork Flask
 - DB SQLite
 - librerias de sqlalchemy para mappeo de objetos relacionales
 - Front End con HTTML/CSS, JS, Angle - Bootstrap Admin App + jQuery

## Ejecucion

Intruciones

```sh
python app.py
```

## Configuracion

json para conectar la DB (puede usarse la local dentro con el dump del proyecto o conectar una base externa)

```
{
  "database": "database.db",
  "port": 5000,
  "host": "127.0.0.1"
}
```
## documentation

Apis pueden ser accedidas desde Postman importando el archivo Acompa-arte.postman_collections.json o desde linea de comando con los siguientes curls:

GET getPatient
curl --location --request GET 'http://127.0.0.1:5000/patient'

POST addPatient
curl --location --request POST 'http://127.0.0.1:5000/patient' \
--header 'Content-Type: application/json' \
--data-raw '{
  "pat_first_name": "Nancy",
  "pat_last_name": "Joes",
  "pat_insurance_no": "IN-3123",
  "pat_ph_no": "2178013290",
  "pat_address": "3 cadlelight 2"
}'

PUT updatePatient
curl --location --request PUT 'http://127.0.0.1:5000/patient/2' \
--header 'Content-Type: application/json' \
--data-raw '{
  "pat_first_name": "Tushar",
  "pat_last_name": "posst",
  "pat_insurance_no": "posst",
  "pat_ph_no": "posst",
  "pat_address": "posst"
}'

DEL deletePatient
curl --location --request DELETE 'http://127.0.0.1:5000/patient/1'

GET getDoctor
curl --location --request GET 'http://127.0.0.1:5000/doctor'


POST addDoctor
curl --location --request POST 'http://127.0.0.1:5000/doctor' \
--header 'Content-Type: application/json' \
--data-raw '{
  "doc_first_name": "Tony",
  "doc_last_name": "Jonson",
  "doc_ph_no": "9967544572",
  "doc_address": "2 candlewood tree"
}'

PUT updateDoctor
curl --location --request PUT 'http://127.0.0.1:5000/doctor/1' \
--header 'Content-Type: application/json' \
--data-raw '{
  "doc_first_name": "satish",
  "doc_last_name": "posst",
  "doc_ph_no": "posst",
  "doc_address": "posst"
}'


DEL deleteDoctor
curl --location --request DELETE 'http://127.0.0.1:5000/doctor/1'

GET getPatientById
curl --location --request GET 'http://127.0.0.1:5000/patient/2'

GET getDoctorById
curl --location --request GET 'http://127.0.0.1:5000/doctor/2'

POST addAppointment
curl --location --request POST 'http://127.0.0.1:5000/appointment' \
--header 'Content-Type: application/json' \
--data-raw '{
  "doc_id": 1,
  "pat_id": 1,
  "appointment_date":"2007-01-01 10:00:00"
}'

GET getAppointment
curl --location --request GET 'http://127.0.0.1:5000/appointment'

PUT updateAppoinetment
curl --location --request PUT 'http://127.0.0.1:5000/appointment/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "doc_id":1,
    "pat_id": 2
    
}'

GET getAppointmentById
curl --location --request GET 'http://127.0.0.1:5000/appointment/1'


DEL deleteAppointment
curl --location --request DELETE 'http://127.0.0.1:5000/appointment/1'


GET getCount
curl --location --request DELETE 'http://127.0.0.1:5000/appointment/1'



## Contribuciones

Quien quiera contribuir envie un pull request, gracias! ;)

