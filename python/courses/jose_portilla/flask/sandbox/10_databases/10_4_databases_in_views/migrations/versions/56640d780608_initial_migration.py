"""Initial migration

Revision ID: 56640d780608
Revises: 
Create Date: 2020-09-23 11:57:38.913624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56640d780608'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
