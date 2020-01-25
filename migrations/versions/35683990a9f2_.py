"""empty message

Revision ID: 35683990a9f2
Revises: 4f09a55c9d6a
Create Date: 2020-01-17 00:15:12.822903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35683990a9f2'
down_revision = '4f09a55c9d6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('address', sa.String(length=120), nullable=False))
    op.add_column('person', sa.Column('full_name', sa.String(length=120), nullable=False))
    op.add_column('person', sa.Column('phone', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'person', ['address'])
    op.create_unique_constraint(None, 'person', ['full_name'])
    op.create_unique_constraint(None, 'person', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'phone')
    op.drop_column('person', 'full_name')
    op.drop_column('person', 'address')
    # ### end Alembic commands ###