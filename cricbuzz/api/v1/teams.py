from flask import Flask, jsonify, request
from flask_restx import Namespace, Resource, reqparse, fields

# parser = reqparse.RequestParser()
# parser.add_argument('team_name', type=str, required=True, help="Team Name is required")
# parser.add_argument('team_country', type=str, required=True, help="Team Country is required")
# parser.add_argument('team_captain', type=str, required=True, help="Team Captain is required")
# parser.add_argument('team_coach', type=str, required=True, help="Team Coach is required")



from cricbuzz.services import team_service

import logging
import logging.config

log = logging.getLogger(__name__)


api = Namespace('teams', description='scroe card')

team_model = api.model('Team', {
    'team_name': fields.String(required=True, description='Team Name'),
    'team_country': fields.String(required=True, description='Team Country'),
    'team_captain': fields.String(required=True, description='Team Captain'),
    'team_coach': fields.String(required=True, description='Team Coach')
})


@api.route('')
class Teams(Resource):
    def get(self):
        teams = team_service.get_all_teams()
        return teams

    @api.expect(team_model)
    def post(self):
        data = request.get_json()

        team_data = {
            'team_name': data.get('team_name'),
            'team_country': data.get('team_country'),
            'team_captain': data.get('team_captain'),
            'team_coach': data.get('team_coach')
        }

        new_team = team_service.add_team(team_data)

        if new_team:
            return {'message': 'Team added successfully'}, 201
        else:
            return {'message': 'Failed to add new team'}, 500

