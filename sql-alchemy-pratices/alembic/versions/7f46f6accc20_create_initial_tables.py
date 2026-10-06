"""create_initial_tables

Revision ID: 7f46f6accc20
Revises: 
Create Date: 2026-10-06 16:31:36.504627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision: str = '7f46f6accc20'
down_revision: Union[str, Sequence[str], None] = None
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
    tables = ['membersnewnain', 'membersnewname', 'membersnewnana']
    for tablename in tables: op.drop_table(f'{tablename}') 
    pass