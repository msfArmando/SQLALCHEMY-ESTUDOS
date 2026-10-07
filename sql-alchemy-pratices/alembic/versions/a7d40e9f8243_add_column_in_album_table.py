"""add_column_in_album_table

Revision ID: a7d40e9f8243
Revises: 
Create Date: 2026-10-07 00:58:40.261381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7d40e9f8243'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('albums', sa.Column('year', sa.Integer, nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('albums', 'year')
    pass
