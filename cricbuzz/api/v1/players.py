from flask import Flask, request, jsonify
from flask_restx import Namespace, Resource, reqparse, fields

from cricbuzz.services.players_service import PlayerService

import logging.config

log = logging.getLogger(__name__)

api = Namespace('players', description='Player related operations')

player_service = PlayerService()  # Initializing your player service

# Model required by flask_restx for input and output validation Player has the name, country, age and role
player_model = api.model('Players', {
    'player_name': fields.String(required=True, description='Player Name'),
    'player_country': fields.String(required=True, description='Player Country'),
    'player_age': fields.Integer(required=True, description='Player Age'),
    'player_role': fields.String(required=True, description='Player Role')
})


# Endpoint to create a new player

# Need to write the following endpoints for the player resource:
# GET /players,
# GET /players/{player_id}, GET /teams/{team_id}/players, POST /players, PUT /players/{player_id}, or DELETE /players/{player_id}

@api.route('')
class Players(Resource):
    @api.expect(player_model)
    def post(self):
        data = request.get_json()  # Extract the data from the request body
        new_player = player_service.create_player(data)
        if new_player:
            return new_player.serialize(), 201  # Assuming 'serialize' method in the Player model
        else:
            return jsonify({'error': 'Failed to create player'}), 400

    def get(self):
        players = player_service.get_all_players()
        return players


@api.route('/<int:player_id>')
class GetPlayer(Resource):
    def get(self, player_id):
        player = player_service.get_player_by_id(player_id)
        if player:
            return player.serialize(), 200
        else:
            return jsonify({'error': 'Player not found'}), 404

    @api.expect(player_model)
    def put(self, player_id):
        data = request.get_json()  # Extract the data from the request body
        updated_player = player_service.update_player(player_id, data)
        if updated_player:
            return updated_player.serialize(), 200  # Assuming 'serialize' method in the Player model
        else:
            return jsonify({'error': 'Failed to update player'}), 400

    def delete(self, player_id):
        deleted_player = player_service.delete_player(player_id)
        if deleted_player:
            return deleted_player.serialize(), 200  # Assuming 'serialize' method in the Player model
        else:
            return jsonify({'error': 'Failed to delete player'}), 400

@api.route('/team/<int:team_id>')
class GetTeamPlayers(Resource):
    def get(self, team_id):
        players = player_service.get_players_by_team_id(team_id)
        return players, 200

