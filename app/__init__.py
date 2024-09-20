from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.config import Config  # Asegúrate de que esta ruta sea correcta

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    try:
        from app.routes.activity_routes import activity_bp
        app.register_blueprint(activity_bp)
    except ImportError as e:
        print(f"Error al importar los blueprints: {e}")

    return app

