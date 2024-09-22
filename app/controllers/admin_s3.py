import boto3
from config.keys import ACCESS_KEY, SECRET_KEY
from flask import Blueprint, request, render_template, redirect, url_for, jsonify, flash
bucket_name = "aws-bucket-cymetria-15"

def connectionS3():
    # Crea una sesión de AWS usando las claves
    session_aws = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_file(session_s3):    
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    keys = [obj.key for obj in bucket_objects]
    print(keys)  # Imprimir las claves de los objetos
    return keys 

def save_file(id, photo):
    extension = photo.filename.split(".")[-1]  # Obtén la extensión del archivo
    photo_name = f"{id}.{extension}"  # Usar f-string para la concatenación
    photo_path = f"/tmp/{photo_name}"  # Usar f-string para la ruta
    photo.save(photo_path)
    print("Photo saved")
    return photo_path, photo_name

def upload_file_s3(session_s3, photo_path, photo_name):
    path_photo_local = f"images/{photo_name}"
    try:
        session_s3.meta.client.upload_file(photo_path, bucket_name, path_photo_local)
        print("Photo uploaded")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")  # Loguear el error