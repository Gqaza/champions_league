from app import db


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(128)
    )
    league = db.Column(
        db.String
    )

    # Relationships
    group = db.relationship(
        'Group', backref='team', lazy=True, uselist=False
    )
