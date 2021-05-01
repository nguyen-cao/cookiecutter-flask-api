from flask_restful import Api

from {{cookiecutter.app_name}}.handlers.base import BaseResource

restapi = Api()
restapi.add_resource(BaseResource, "/resource", endpoint="resource")