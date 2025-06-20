"""Added super_name to Hero

Revision ID: db428af072da
Revises: b869e4aaefc9
Create Date: 2025-06-15 23:59:19.064043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db428af072da'
down_revision = 'b869e4aaefc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('super_name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.drop_column('super_name')

    # ### end Alembic commands ###
