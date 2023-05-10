from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

from .user_controller  import foo, bar;

user_blueprint.add_url_rule('/foo', None, foo, methods=['GET'])
user_blueprint.add_url_rule('/bar', None, bar, methods=['GET'])

