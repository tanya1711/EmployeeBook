# instance/config.py
import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'happy_people'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
