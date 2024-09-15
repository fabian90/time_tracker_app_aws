class Config:
    DB_USER = "admin"
    DB_PASSWORD = "Prueba123456"
    DB_HOST = "timetrackerdb.cpwaky0y8bbr.us-east-2.rds.amazonaws.com"
    DB_NAME = "timetrackerdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"