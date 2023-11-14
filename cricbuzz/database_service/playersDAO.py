from cricbuzz.model.db import db
from cricbuzz.model.models import Player


# add error handling for all the methods

class PlayerDAO:
    # add error handling for all the methods and catch sqlalchemy exceptions

    def create_player(self, data):
        try:
            new_player = Player(**data)  # Assuming data keys match Player model attributes
            db.session.add(new_player)  # Add the new player object
            db.session.commit()  # Commit the changes to the database
            return new_player
        except Exception as e:
            print(e)
            return None

    def get_all_players(self):
        return Player.query.all()

    def get_player_by_id(self, player_id):
        return Player.query.get(player_id)

    def get_players_by_team_id(self, team_id):
        return Player.query.filter_by(team_id=team_id).all()

    def update_player(self, player_id, data):
        player = Player.query.get(player_id)
        if player:
            for key, value in data.items():
                setattr(player, key, value)
            db.session.commit()
            return player
        else:
            return None

    def delete_player(self, player_id):
        player = Player.query.get(player_id)
        if player:
            db.session.delete(player)
            db.session.commit()
            return player
        else:
            return None
