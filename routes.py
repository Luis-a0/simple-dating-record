from flask import jsonify, request
from flask import Flask, render_template, redirect, url_for
from models import Paciente, Medico, Especialidad, Cita

def configure_routes(app, session):
    # PACIENTES
    @app.route('/pacientes', methods=['GET'])
    def get_pacientes():
        pacientes = session.query(Paciente).all()
        return jsonify([paciente.to_dict() for paciente in pacientes])

    @app.route('/pacientes/<int:id>', methods=['GET'])
    def get_paciente_by_id(id):
        paciente = session.query(Paciente).filter_by(id=id).first()
        if paciente is None:
            return jsonify({'error': 'Paciente no encontrado'}), 404
        return jsonify(paciente.to_dict())

    @app.route('/pacientes', methods=['POST'])
    def create_paciente():
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')

        if not all([nombre, apellido, email]):
            return jsonify({'error': 'Faltan datos'}), 400

        paciente = Paciente(nombre=nombre, apellido=apellido, email=email)
        session.add(paciente)
        session.commit()

        return jsonify({'message': 'Paciente creado correctamente'})
    
    @app.route('/pacientes/<int:id>', methods=['PUT'])
    def update_paciente(id):
        paciente = session.query(Paciente).filter_by(id=id).first()
        if paciente is None:
            return jsonify({'error': 'Paciente no encontrado'}), 404
        
        data = request.get_json()
        paciente.nombre = data.get('nombre', paciente.nombre)
        paciente.apellido = data.get('apellido', paciente.apellido)
        paciente.email = data.get('email', paciente.email)

        session.commit()

        return jsonify({'message': 'Información del paciente actualizada correctamente'})
    
    # MEDICOS
    @app.route('/medicos', methods=['GET'])
    def get_medicos():
        medicos = session.query(Medico).all()
        return jsonify([medico.to_dict() for medico in medicos])

    @app.route('/medicos', methods=['POST'])
    def create_medico():
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        especialidad_id = data.get('especialidad_id')

        if not all([nombre, apellido, especialidad_id]):
            return jsonify({'error': 'Faltan datos'}), 400

        medico = Medico(nombre=nombre, apellido=apellido, especialidad_id=especialidad_id)
        session.add(medico)
        session.commit()

        return jsonify({'message': 'Medico creado correctamente'})
    
    @app.route('/medicos/<int:id>', methods=['PUT'])
    def update_medico(id):
        medico = session.query(Medico).filter_by(id=id).first()
        if medico is None:
            return jsonify({'error': 'Medico no encontrado'}), 404
        
        data = request.get_json()
        medico.nombre = data.get('nombre', medico.nombre)
        medico.apellido = data.get('apellido', medico.apellido)
        medico.email = data.get('email', medico.email)

        session.commit()

        return jsonify({'message': 'Información del medico actualizada correctamente'})
    
    @app.route('/doctores', methods=['GET'])
    def get_doctores_con_citas():
        doctores = session.query(Medico).all()
        doctores_con_citas = []
        for doctor in doctores:
            citas = session.query(Cita).filter_by(medico_id=doctor.id).all()
            pacientes = [session.query(Paciente).filter_by(id=cita.paciente_id).first().to_dict() for cita in citas]
            doctores_con_citas.append({
                'doctor': doctor.to_dict(),
                'citas': [cita.to_dict() for cita in citas],
                'pacientes': pacientes
            })
        return jsonify(doctores_con_citas)
    
    # CITAS
    @app.route('/citas', methods=['POST'])
    def solicitar_cita():
        data = request.get_json()
        paciente_id = data.get('paciente_id')
        medico_id = data.get('medico_id')
        detalles = data.get('detalles')

        if not all([paciente_id, medico_id, detalles]):
            return jsonify({'error': 'Faltan datos'}), 400

        cita = Cita(paciente_id=paciente_id, medico_id=medico_id, detalles=detalles)
        session.add(cita)
        session.commit()

        return jsonify({'message': 'Cita solicitada correctamente'})
    
    @app.route('/citas', methods=['GET'])
    def get_citas():
        citas = session.query(Cita).all()
        return jsonify([cita.to_dict() for cita in citas])
    
    @app.route('/citas/<int:id>', methods=['DELETE'])
    def delete_cita(id):
        cita = session.query(Cita).filter_by(id=id).first()
        if cita is None:
            return jsonify({'error': 'Cita no encontrada'}), 404

        session.delete(cita)
        session.commit()

        return jsonify({'message': 'Cita eliminada correctamente'})
    

    @app.route('/')
    def index():
        pacientes = session.query(Paciente).all()
        medicos = session.query(Medico).all()
        return render_template('index.html', pacientes=pacientes, medicos=medicos)

