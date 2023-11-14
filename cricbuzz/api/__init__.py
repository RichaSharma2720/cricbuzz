from flask import Blueprint
from flask_restx import Api

from cricbuzz.api.v1.scroecard import api as v1_scorecard_api
from cricbuzz.api.v1.teams import api as v1_teams_api
from cricbuzz.api.v1.players import api as v1_players_api

api_v1 = Blueprint('api_v1', __name__, url_prefix='/cricbuzz/rest/v1')

api = Api(api_v1, version='1.0', title='Crickbuzz')

api.add_namespace(v1_scorecard_api)
api.add_namespace(v1_teams_api)
api.add_namespace(v1_players_api)