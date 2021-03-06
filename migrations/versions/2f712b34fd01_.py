"""empty message

Revision ID: 2f712b34fd01
Revises: 
Create Date: 2019-12-01 20:53:46.727506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f712b34fd01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('host',
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('ph_number', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('email', 'ph_number')
    )
    op.create_table('visitor',
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('ph_number', sa.Integer(), nullable=False),
    sa.Column('check_in_time', sa.DateTime(), nullable=False),
    sa.Column('check_out_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('email', 'check_in_time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitor')
    op.drop_table('host')
    # ### end Alembic commands ###
