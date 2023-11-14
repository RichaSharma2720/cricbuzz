from cricbuzz.database_service.playersDAO import PlayerDAO
class PlayerService:
    def __init__(self):
        self.player_dao = PlayerDAO()  # Assuming the PlayerDAO handles DB operations

    def create_player(self, data):
        return self.player_dao.create_player(data)

    def get_all_players(self):
        players = self.player_dao.get_all_players();
        if not players:
            return []
        return [player.serialize() for player in players]

    def get_player_by_id(self, player_id):
        return self.player_dao.get_player_by_id(player_id)

    def get_players_by_team_id(self, team_id):
        return self.player_dao.get_players_by_team_id(team_id)

    def update_player(self, player_id, data):
        return self.player_dao.update_player(player_id, data)

    def delete_player(self, player_id):
        return self.player_dao.delete_player(player_id)