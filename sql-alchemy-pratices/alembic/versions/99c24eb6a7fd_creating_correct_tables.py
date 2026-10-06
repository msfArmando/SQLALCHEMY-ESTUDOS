"""creating_correct_tables

Revision ID: 99c24eb6a7fd
Revises: 84970149c468
Create Date: 2026-10-06 17:30:49.604986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99c24eb6a7fd'
down_revision: Union[str, Sequence[str], None] = '84970149c468'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'members',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('artist_id', sa.Integer, nullable=True),
        sa.ForeignKeyConstraint(('artist_id',), ['artists.artist_id'])
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
