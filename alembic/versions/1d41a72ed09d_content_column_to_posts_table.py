"""content column to posts table

Revision ID: 1d41a72ed09d
Revises: d96958a889e1
Create Date: 2023-05-30 08:51:07.639115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d41a72ed09d'
down_revision = 'd96958a889e1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
