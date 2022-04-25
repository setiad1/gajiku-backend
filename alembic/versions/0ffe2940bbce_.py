"""empty message

Revision ID: 0ffe2940bbce
Revises: b31074b6992e
Create Date: 2022-04-25 11:52:14.430379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffe2940bbce'
down_revision = 'b31074b6992e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('set_gaji_pangkat', sa.Column('keterangan', sa.String(length=500), nullable=True))
    op.create_index(op.f('ix_set_gaji_pangkat_keterangan'), 'set_gaji_pangkat', ['keterangan'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_set_gaji_pangkat_keterangan'), table_name='set_gaji_pangkat')
    op.drop_column('set_gaji_pangkat', 'keterangan')
    # ### end Alembic commands ###
