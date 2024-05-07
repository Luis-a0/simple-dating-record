from flask import Flask
from routes import configure_routes
from models import engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Configuración de la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Registrar las rutas
configure_routes(app, session)


if __name__ == '__main__':
    app.run(debug=True)
