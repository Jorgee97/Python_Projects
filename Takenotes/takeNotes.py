import click
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('./credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://takenotes-637c5.firebaseio.com"
})

db.Reference()

print(default_app.project_id)
