from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///Dating.db')

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email
        }

class Medico(Base):
    __tablename__ = 'medicos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    especialidad_id = Column(Integer, ForeignKey('especialidades.id'), nullable=False)

    especialidad = relationship("Especialidad")

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'especialidad': self.especialidad.nombre
        }

class Especialidad(Base):
    __tablename__ = 'especialidades'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

class Cita(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True)
    detalles = Column(String(2550))
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    medico_id = Column(Integer, ForeignKey('medicos.id'), nullable=False)

    paciente = relationship("Paciente")
    medico = relationship("Medico")

    def to_dict(self):
        return {
            'id': self.id,
            'detalles': self.detalles,
            'paciente': self.paciente.nombre,
            'medico': self.medico.nombre
        }
