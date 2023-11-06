from cricbuzz.model.models import Team
from cricbuzz.model.db import db

import logging
import logging.config

log = logging.getLogger(__name__)

class TeamDAO:
    @staticmethod
    def get_all_teams():
        log.info('Retrieving all teams')
        return Team.query.all()

    def add_team(team_data):
        try:
            new_team = Team(**team_data)
            db.session.add(new_team)
            db.session.commit()
            return new_team
        except Exception as e:
            db.session.rollback()
            log.error(f"Error adding team: {e}")
            return None
