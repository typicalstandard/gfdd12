from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from flask_migrate import Migrate
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost/db_name'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)


