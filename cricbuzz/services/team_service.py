from cricbuzz.database_service.teamDAO import TeamDAO

import logging
import logging.config

log = logging.getLogger(__name__)

def get_all_teams():
    log.info("Getting all teams")
    teams = TeamDAO.get_all_teams()
    if not teams:
        return []
    return [team.serialize() for team in teams]


def add_team(team_data):
    team = TeamDAO.add_team(team_data)
    return team


def get_team_by_id(team_id):
    return TeamDAO.get_team_by_id(team_id)


def update_team_by_id(team_id, data):
    return TeamDAO.update_team_by_id(team_id, data)


def delete_team_by_id(team_id):
    return TeamDAO.delete_team_by_id(team_id)