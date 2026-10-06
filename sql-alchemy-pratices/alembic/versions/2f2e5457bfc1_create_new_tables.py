"""create_new_tables

Revision ID: 2f2e5457bfc1
Revises: 7f46f6accc20
Create Date: 2026-10-06 17:04:11.167598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision: str = '2f2e5457bfc1'
down_revision: Union[str, Sequence[str], None] = '7f46f6accc20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'membersnewnana',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('artist_id', sa.Integer, nullable=True),
        sa.ForeignKeyConstraint(('artist_id',), ['artists.artist_id'])
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
