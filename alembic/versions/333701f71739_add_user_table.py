"""add user table

Revision ID: 333701f71739
Revises: 1d41a72ed09d
Create Date: 2023-05-30 09:01:50.869980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333701f71739'
down_revision = '1d41a72ed09d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
