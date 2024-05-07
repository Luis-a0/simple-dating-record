from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Medico, Especialidad, engine

# Crear el motor de la base de datos y la sesión
engine = create_engine('sqlite:///Dating.db')
Session = sessionmaker(bind=engine)
session = Session()

# Definir los médicos y sus especialidades
medicos_especialidades = [
    ("Juan", "Pérez", "Pediatría"),
    ("Ana", "Gómez", "Ginecología"),
    ("Carlos", "Rodríguez", "Cardiología"),
    ("Laura", "Martínez", "Dermatología"),
    ("José", "García", "Neurología")
]

# Ingresar los médicos y sus especialidades en la base de datos
for nombre, apellido, nombre_especialidad in medicos_especialidades:
    # Verificar si la especialidad ya existe en la base de datos
    especialidad = session.query(Especialidad).filter_by(nombre=nombre_especialidad).first()
    if not especialidad:
        # Si no existe, crearla
        especialidad = Especialidad(nombre=nombre_especialidad)
        session.add(especialidad)
        session.commit()

    # Crear el médico con la especialidad correspondiente
    medico = Medico(nombre=nombre, apellido=apellido, especialidad_id=especialidad.id)
    session.add(medico)
    session.commit()

print("Se han ingresado correctamente los médicos con sus especialidades.")
