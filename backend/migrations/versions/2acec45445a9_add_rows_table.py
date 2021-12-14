"""Add rows table

Revision ID: 2acec45445a9
Revises: 
Create Date: 2021-05-14 22:15:11.527967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2acec45445a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rows_count'), 'rows', ['count'], unique=False)
    op.create_index(op.f('ix_rows_date'), 'rows', ['date'], unique=False)
    op.create_index(op.f('ix_rows_distance'), 'rows', ['distance'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rows_distance'), table_name='rows')
    op.drop_index(op.f('ix_rows_date'), table_name='rows')
    op.drop_index(op.f('ix_rows_count'), table_name='rows')
    op.drop_table('rows')
    # ### end Alembic commands ###
