import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://joozao:sjjimo@localhost:5432/pitchlist'
    SECRET_KEY='sjjimo'
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME='ijanemercy@gmail.com'
    MAIL_PASSWORD='@janeMercy700'

    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
