from app import db


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    team_id = db.Column(
        db.Integer,
        db.ForeignKey('team.id'),
        nullable=False
    )
    match_played = db.Column(
        db.Integer
    )
    win = db.Column(
        db.Integer
    )
    draw = db.Column(
        db.Integer
    )
    loss = db.Column(
        db.Integer
    )
    goals_for = db.Column(
        db.Integer
    )
    goals_against = db.Column(
        db.Integer
    )
    goal_diff = db.Column(
        db.Integer
    )
    league_position = db.Column(
        db.Integer
    )
