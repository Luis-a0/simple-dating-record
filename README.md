# simple-dating-record

Aplicación de registro de pacientes, médicos y citas médicas, desarrollada en Flask y SQLAlchemy.

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/dating-record.git

```
2. Instalación de dependencias:
```bash
cd dating-record
pip install -r requirements.txt

```
## Configuración de la Base de Datos

Antes de ejecutar la aplicación, necesitas inicializar la base de datos y cargar algunos datos de prueba.

1. Ejecuta el script init_db.py para crear las tablas en la base de datos:
```bash
python init_db.py
```
2. Opcionalmente, puedes ejecutar el script data_test_init.py para insertar información básica de médicos y especialidades:
```bash
python data_test_init.py
```
## Ejecución

Para ejecutar la aplicación, simplemente ejecuta "app.py":
```bash
python app.py
```
La aplicación estará disponible en http://localhost:5000/

## Uso
Endpoints API
#### Pacientes

- `GET /pacientes`: Obtiene la lista de todos los pacientes.
- `GET /pacientes/<id>`: Obtiene los detalles de un paciente específico.
- `POST /pacientes`: Crea un nuevo paciente.
- `PUT /pacientes/<id>`: Actualiza la información de un paciente existente.

#### Médicos

- `GET /medicos`: Obtiene la lista de todos los médicos.
- `POST /medicos`: Crea un nuevo médico.
- `PUT /medicos/<id>`: Actualiza la información de un médico existente.
- `GET /doctores`: Obtiene la lista de médicos con sus citas y pacientes.

#### Citas

- `GET /citas`: Obtiene la lista de todas las citas.
- `POST /citas`: Crea una nueva cita.
- `DELETE /citas/<id>`: Elimina una cita existente.

## Interfaz de Usuario

La interfaz de usuario permite registrar pacientes, médicos y citas a través de formularios web.

- La página principal (`/`) muestra formularios para registrar  citas.
- Los campos de paciente y médico son listas desplegables que muestran los pacientes y médicos registrados en la base de datos.
- El formularios envían datos a través de la API para su procesamiento.