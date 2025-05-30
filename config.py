import os
basedir = os.path.abspath(os.path.dirname(__file__))


def get_database_uri():
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "ROGERNYVA")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "54320")
    dbname = os.getenv("DB_NAME", "photosnyva")
    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

class Config:
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_EXTENSIONS = [".jpg", ".png"]
    UPLOAD_FOLDER = os.path.join(basedir, "static/uploads")