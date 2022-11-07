import random as rand
from flask import Blueprint, redirect, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,SubmitField,TextAreaField, HiddenField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, ValidationError,NumberRange

from better_profanity import profanity

import app.blueprints.services as services
import app.adapters.repository as repo

app_blueprint = Blueprint('app_blueprint', __name__)



@app_blueprint.route('/')
def home():
    start_index = 0
    end_index = 40
    # just gets all at the moment

    posts = services.get_posts(start_index, end_index)
    return render_template("home.html",posts)

@app_blueprint.route('/trading')
def trading():
    return render_template("trading.html")