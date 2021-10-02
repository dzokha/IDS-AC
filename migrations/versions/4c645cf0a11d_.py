"""empty message

Revision ID: 4c645cf0a11d
Revises: 
Create Date: 2021-09-18 01:31:25.437555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c645cf0a11d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abnormals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('timestamp', sa.String(length=60), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('loc', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('src_ip', sa.String(length=100), nullable=True),
    sa.Column('src_port', sa.Integer(), nullable=True),
    sa.Column('dst_ip', sa.String(length=100), nullable=True),
    sa.Column('dst_port', sa.Integer(), nullable=True),
    sa.Column('protocol', sa.String(length=50), nullable=True),
    sa.Column('service', sa.String(length=50), nullable=True),
    sa.Column('flag', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gid_sid_rev', sa.String(length=20), nullable=True),
    sa.Column('msg', sa.String(length=200), nullable=True),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.String(length=60), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('loc', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('src_ip', sa.String(length=100), nullable=True),
    sa.Column('src_port', sa.Integer(), nullable=True),
    sa.Column('dst_ip', sa.String(length=100), nullable=True),
    sa.Column('dst_port', sa.Integer(), nullable=True),
    sa.Column('meta_data', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alerts')
    op.drop_table('abnormals')
    # ### end Alembic commands ###
