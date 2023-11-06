from cricbuzz.model.db import db


class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)
    team_country = db.Column(db.String)
    team_captain = db.Column(db.String)
    team_coach = db.Column(db.String)

    # Serialize method
    def serialize(self):
        return {
            'team_id': self.team_id,
            'team_name': self.team_name,
            'team_country': self.team_country,
            'team_captain': self.team_captain,
            'team_coach': self.team_coach
        }


class Player(db.Model):
    __tablename__ = 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String)
    player_country = db.Column(db.String)
    player_age = db.Column(db.Integer)
    player_role = db.Column(db.String)


class Match(db.Model):
    __tablename__ = 'match'
    match_id = db.Column(db.Integer, primary_key=True)
    team1_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    team2_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    venue = db.Column(db.String)
    start_time = db.Column(db.String)
    end_time = db.Column(db.String)
    result = db.Column(db.String)
    winning_team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    status = db.Column(db.String)


class Innings(db.Model):
    __tablename__ = 'innings'
    innings_id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.match_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    total_runs = db.Column(db.Integer)
    wickets_lost = db.Column(db.Integer)
    total_overs = db.Column(db.Integer)
    current_batsmen_ids = db.Column(db.String)  # Comma-separated player IDs
    current_bowler_id = db.Column(db.Integer)
    live_commentary = db.Column(db.String)
    # ... other relevant inning information


class PlayerStats(db.Model):
    __tablename__ = 'player_stats'
    player_stats_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    innings_id = db.Column(db.Integer, db.ForeignKey('innings.innings_id'))
    runs_scored = db.Column(db.Integer)
    balls_faced = db.Column(db.Integer)
    wickets_taken = db.Column(db.Integer)
    bowling_economy = db.Column(db.Float)
    batting_strike_rate = db.Column(db.Float)


class MatchCommentary(db.Model):
    __tablename__ = 'match_commentary'
    commentary_id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.match_id'))
    commentary = db.Column(db.String)  # Field to store real-time commentary for a match

