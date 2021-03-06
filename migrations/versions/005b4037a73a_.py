"""empty message

Revision ID: 005b4037a73a
Revises: 90e6d7684eef
Create Date: 2018-07-04 20:45:31.188552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '005b4037a73a'
down_revision = '90e6d7684eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_verified')
    # ### end Alembic commands ###
