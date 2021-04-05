"""empty message

Revision ID: b32d31a2aa75
Revises: 762402052503
Create Date: 2021-04-05 05:01:37.213270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32d31a2aa75'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=200), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('to_do')
    # ### end Alembic commands ###
