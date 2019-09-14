from flask import render_template
from . import auth
from app.models import User

@auth.route('/')
def index():
    return "Welcome"
