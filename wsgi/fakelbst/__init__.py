#!/usr/bin/env python
import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {"DB" : "yourDB"}
app.config['SECRET_KEY'] = 'random'

db = MongoEngine(app)

from views.views import projects
app.register_blueprint(projects)
