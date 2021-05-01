from flask import current_app, request
from flask_restful import Resource
from funcy import project
from sqlalchemy import text

from {{cookiecutter.app_name}}.extensions import db

class BaseResource(Resource):
    def get(self):
        return []

    def post(self):
        return None
