"""New model

Revision ID: 84b6aa4563b8
Revises: 
Create Date: 2025-06-27 03:53:45.622229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84b6aa4563b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grades',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter', sa.String(length=10), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('points')
    )
    with op.batch_alter_table('grades', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_grades_letter'), ['letter'], unique=True)

    op.create_table('sites',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('system', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('site_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('points_cap', sa.Integer(), nullable=True),
    sa.Column('format', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['site_id'], ['sites.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_events_site_id'), ['site_id'], unique=False)

    op.create_table('players',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('alias', sa.String(length=20), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('profile_picture', sa.String(length=200), nullable=True),
    sa.Column('playing_since', sa.Date(), nullable=True),
    sa.Column('bio', sa.String(length=140), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('roles', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_players_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_players_grade_id'), ['grade_id'], unique=False)

    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_teams_event_id'), ['event_id'], unique=False)

    op.create_table('registrations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('registrations', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_registrations_event_id'), ['event_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_registrations_player_id'), ['player_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_registrations_team_id'), ['team_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registrations', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_registrations_team_id'))
        batch_op.drop_index(batch_op.f('ix_registrations_player_id'))
        batch_op.drop_index(batch_op.f('ix_registrations_event_id'))

    op.drop_table('registrations')
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_teams_event_id'))

    op.drop_table('teams')
    op.drop_table('posts')
    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_players_grade_id'))
        batch_op.drop_index(batch_op.f('ix_players_email'))

    op.drop_table('players')
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_events_site_id'))

    op.drop_table('events')
    op.drop_table('sites')
    with op.batch_alter_table('grades', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_grades_letter'))

    op.drop_table('grades')
    # ### end Alembic commands ###
