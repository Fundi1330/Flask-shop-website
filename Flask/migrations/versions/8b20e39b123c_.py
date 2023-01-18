"""empty message

Revision ID: 8b20e39b123c
Revises: 5a9e1401084b
Create Date: 2023-01-16 16:31:12.738016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b20e39b123c'
down_revision = '5a9e1401084b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Food_Goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.create_index(batch_op.f('ix_Food_Goods_price'), ['price'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Food_Goods', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Food_Goods_price'))
        batch_op.drop_column('price')

    # ### end Alembic commands ###
