import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'super-secret-key'
    )

    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///store.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = \
        'static/uploads'

    QR_FOLDER = \
        'static/qrcodes'