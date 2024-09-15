from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from app.models import Activity, db
from datetime import datetime

activity_bp = Blueprint('activity_bp', __name__)

# Ruta para listar todas las actividades
@activity_bp.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return render_template('activities.html', activities=activities)

# Ruta para mostrar el formulario de agregar actividad
@activity_bp.route('/activities/new', methods=['GET'])
def new_activity():
    return render_template('add_activity.html')

# Ruta para agregar una nueva actividad
@activity_bp.route('/activities', methods=['POST'])
def add_activity():
    data = request.form
    new_activity = Activity(
        description=data['description'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        start_time=datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M'),  # Convertir a datetime
        end_time=datetime.strptime(data['end_time'], '%Y-%m-%dT%H:%M') if data['end_time'] else None  # Usar el formato correcto
    )
    db.session.add(new_activity)
    db.session.commit()
    return redirect(url_for('activity_bp.get_activities'))

# Ruta para marcar el final de una actividad
@activity_bp.route('/activities/<int:id>/end', methods=['POST'])
def end_activity(id):
    activity = Activity.query.get_or_404(id)
    activity.end_time = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('activity_bp.get_activities'))
