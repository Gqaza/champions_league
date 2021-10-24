from app import db


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    team_id = db.Column(
        db.Integer,
        db.ForeignKey('team.id'),
        nullable=False
    )
    jersey_no = db.Column(db.Integer)
    player_name = db.Column(db.String)
    player_surname = db.Column(db.String)
    position = db.Column(db.Integer)
    date_of_birth = db.Column(db.DateTime)

    team = db.relationship(
        'Team', backref='player', lazy=True, uselist=False
    )
