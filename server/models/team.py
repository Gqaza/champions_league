from app import db


class Team(db.Model):
    __tablename__ = 'team'
    __table_args__ = (
        db.UniqueConstraint(
            "name",
            "league",
            name='unique_name_league'
        ),
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(128),
        nullable=False,
    )
    league = db.Column(
        db.String,
        nullable=False
    )

    # Relationships
    group = db.relationship(
        'Group', backref='team', lazy=True, uselist=False
    )
