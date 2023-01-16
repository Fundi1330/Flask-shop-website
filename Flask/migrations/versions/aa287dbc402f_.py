"""empty message

Revision ID: aa287dbc402f
Revises: 8b20e39b123c
Create Date: 2023-01-16 17:15:41.881325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa287dbc402f'
down_revision = '8b20e39b123c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Food_Goods', schema=None) as batch_op:
        batch_op.drop_column('fruit')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Food_Goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fruit', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
