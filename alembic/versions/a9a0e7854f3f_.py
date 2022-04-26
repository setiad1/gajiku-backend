"""empty message

Revision ID: a9a0e7854f3f
Revises: e175c7866e45
Create Date: 2022-04-26 08:15:47.818375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9a0e7854f3f'
down_revision = 'e175c7866e45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('set_gaji_kawin', sa.Column('ptkp', sa.Float(), nullable=True))
    op.drop_index('ix_set_gaji_kawin_besaran_ptkp', table_name='set_gaji_kawin')
    op.drop_index('ix_set_gaji_kawin_jenis_besaran_ptkp', table_name='set_gaji_kawin')
    op.create_index(op.f('ix_set_gaji_kawin_ptkp'), 'set_gaji_kawin', ['ptkp'], unique=False)
    op.drop_column('set_gaji_kawin', 'jenis_besaran_ptkp')
    op.drop_column('set_gaji_kawin', 'besaran_ptkp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('set_gaji_kawin', sa.Column('besaran_ptkp', mysql.FLOAT(), nullable=True))
    op.add_column('set_gaji_kawin', sa.Column('jenis_besaran_ptkp', mysql.ENUM('persentase', 'spesifik'), server_default=sa.text("'spesifik'"), nullable=False))
    op.drop_index(op.f('ix_set_gaji_kawin_ptkp'), table_name='set_gaji_kawin')
    op.create_index('ix_set_gaji_kawin_jenis_besaran_ptkp', 'set_gaji_kawin', ['jenis_besaran_ptkp'], unique=False)
    op.create_index('ix_set_gaji_kawin_besaran_ptkp', 'set_gaji_kawin', ['besaran_ptkp'], unique=False)
    op.drop_column('set_gaji_kawin', 'ptkp')
    # ### end Alembic commands ###
