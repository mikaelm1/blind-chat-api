"""empty message

Revision ID: 52a2cb489f82
Revises: a50c11b4a56f
Create Date: 2016-10-18 19:44:26.662080

"""

# revision identifiers, used by Alembic.
revision = '52a2cb489f82'
down_revision = 'a50c11b4a56f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'created')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('created', mysql.DATETIME(), nullable=True))
    ### end Alembic commands ###
