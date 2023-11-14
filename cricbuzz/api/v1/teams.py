from flask import Flask, jsonify, request
from flask_restx import Namespace, Resource, reqparse, fields

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


@api.route('/<int:team_id>')
class GetTeam(Resource):
    def get(self, team_id):
        team = team_service.get_team_by_id(team_id)
        if team:
            return team, 200
        else:
            return jsonify({'error': 'Team not found'}), 404

    @api.expect(team_model)
    def put(self, team_id):
        data = request.get_json()

        updated_team = team_service.update_team_by_id(team_id, data)
        if updated_team:
            return updated_team, 200
        else:
            return jsonify({'error': 'Team not found'}), 404


    def delete(self, team_id):
        team = team_service.delete_team_by_id(team_id)
        if team:
            return jsonify({'message': 'Team deleted successfully'}), 200
        else:
            return jsonify({'error': 'Team not found'}), 404



