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

    def get_team_by_id(team_id):
        team = db.session.query(Team).filter(Team.team_id == team_id).first()
        return team.serialize()

    def update_team_by_id(team_id, data):
        team = db.session.query(Team).filter(Team.team_id == team_id).first()

        if team:
            for key, value in data.items():
                setattr(team, key, value)

            db.session.commit()  # Commit the changes to the database
            return team.serialize()  # Return the updated team object
        else:
            db.session.rollback()
            return None

    def delete_team_by_id(team_id):
        team = db.session.query(Team).filter(Team.team_id == team_id).first()
        if team:
            db.session.delete(team)
            db.session.commit()
            return True
        else:
            db.session.rollback()
            return None
