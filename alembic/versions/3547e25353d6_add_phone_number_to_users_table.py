"""add phone number to users table

Revision ID: 3547e25353d6
Revises: a2757619b230
Create Date: 2023-05-30 09:37:43.633127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3547e25353d6'
down_revision = 'a2757619b230'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###