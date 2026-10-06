"""create_tables

Revision ID: 66d297e64d7e
Revises: 2f2e5457bfc1
Create Date: 2026-10-06 17:21:12.097643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66d297e64d7e'
down_revision: Union[str, Sequence[str], None] = '2f2e5457bfc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'membersnewnain',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('artist_id', sa.Integer, nullable=True),
        sa.ForeignKeyConstraint(('artist_id',), ['artists.artist_id'])
    )
    pass



def downgrade() -> None:
    op.drop_table('membersnewnain')
    pass
