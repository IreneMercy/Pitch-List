import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY='sjjimo'
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME='ijanemercy@gmail.com'
    MAIL_PASSWORD='@janeMercy700'
