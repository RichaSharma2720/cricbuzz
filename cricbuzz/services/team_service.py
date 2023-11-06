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