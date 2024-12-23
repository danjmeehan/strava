"""Add comments field to runs table

Revision ID: d69e461f5af6
Revises: 0b6aae9d1046
Create Date: 2024-12-02 22:34:48.558299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69e461f5af6'
down_revision = '0b6aae9d1046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('runs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comments', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('runs', schema=None) as batch_op:
        batch_op.drop_column('comments')

    # ### end Alembic commands ###
