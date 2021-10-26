"""Initial migration

Revision ID: 3a6eafc98acd
Revises: 
Create Date: 2021-10-24 01:44:35.031721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a6eafc98acd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('match_played', sa.Integer(), nullable=True),
    sa.Column('win', sa.Integer(), nullable=True),
    sa.Column('draw', sa.Integer(), nullable=True),
    sa.Column('loss', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('goal_diff', sa.Integer(), nullable=True),
    sa.Column('league_position', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('jersey_no', sa.Integer(), nullable=True),
    sa.Column('player_name', sa.String(), nullable=True),
    sa.Column('player_surname', sa.String(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    op.drop_table('group')
    op.drop_table('team')
    # ### end Alembic commands ###
