from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from app.models import Activity, db
from datetime import datetime
from ..controllers.admin_s3 import connectionS3,save_file,upload_file_s3

activity_bp = Blueprint('activity_bp', __name__)

# Ruta para listar todas las actividades
@activity_bp.route('/activities', methods=['GET'])
def get_activities():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    activity_id = request.args.get('id') 
    query = Activity.query

    # Filtrar por nombre
    if first_name:
        query = query.filter(Activity.first_name.ilike(f'%{first_name}%'))
    
    # Filtrar por apellido
    if last_name:
        query = query.filter(Activity.last_name.ilike(f'%{last_name}%'))
    
    # Filtrar por ID
    if activity_id:
        query = query.filter(Activity.id == activity_id)
    
    activities = query.all()
    return render_template('activities.html', activities=activities)

# Ruta para mostrar el formulario de agregar actividad
@activity_bp.route('/activities/new', methods=['GET'])
def new_activity():
    return render_template('add_activity.html')

# Ruta para agregar una nueva actividad
def add_activity():
    data = request.form
    file = request.files
    photo = file.get("photo")  # Usar get para evitar KeyError
    try:
        if not photo:
            # Manejar el caso en el que no se proporciona una foto
            flash("Se requiere una foto para agregar una actividad.", "error")
            return redirect(url_for('activity_bp.new_activity'))

        new_activity = Activity(
            description=data['description'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            start_time=datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M'),  # Convertir a datetime
            end_time=datetime.strptime(data['end_time'], '%Y-%m-%dT%H:%M') if data['end_time'] else None  # Usar el formato correcto
        )
        
        db.session.add(new_activity)
        db.session.commit()

        session_s3 = connectionS3()
        photo_path, photo_name = save_file(new_activity.id, photo)  # Asegúrate de usar el ID correcto aquí
        upload_file_s3(session_s3, photo_path, photo_name)

        flash("Actividad agregada exitosamente.", "success")
        return redirect(url_for('activity_bp.get_activities'))
    except Exception as e:
        db.session.rollback()  # Revertir la sesión en caso de error
        flash(f"Ocurrió un error al agregar la actividad: {str(e)}", "error")
        return redirect(url_for('activity_bp.new_activity'))

# Ruta para marcar el final de una actividad
@activity_bp.route('/activities/<int:id>/end', methods=['POST'])
def end_activity(id):
    activity = Activity.query.get_or_404(id)
    activity.end_time = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('activity_bp.get_activities'))
