"""Create runs table

Revision ID: f3b9ef95fa9d
Revises: 
Create Date: 2024-11-26 15:57:42.381636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b9ef95fa9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('runs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strava_id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.Column('moving_time', sa.Integer(), nullable=False),
    sa.Column('elapsed_time', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('average_speed', sa.Float(), nullable=True),
    sa.Column('max_speed', sa.Float(), nullable=True),
    sa.Column('total_elevation_gain', sa.Float(), nullable=True),
    sa.Column('average_cadence', sa.Float(), nullable=True),
    sa.Column('elevation_high', sa.Float(), nullable=True),
    sa.Column('elevation_low', sa.Float(), nullable=True),
    sa.Column('start_latitude', sa.Float(), nullable=True),
    sa.Column('start_longitude', sa.Float(), nullable=True),
    sa.Column('end_latitude', sa.Float(), nullable=True),
    sa.Column('end_longitude', sa.Float(), nullable=True),
    sa.Column('average_temp', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('strava_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('runs')
    # ### end Alembic commands ###
