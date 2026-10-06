"""delete_tables

Revision ID: 53787ecc6266
Revises: 66d297e64d7e
Create Date: 2026-10-06 17:24:33.171224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53787ecc6266'
down_revision: Union[str, Sequence[str], None] = '66d297e64d7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    tables = ['membersnewnain', 'membersnewname', 'membersnewnana']
    for tablename in tables: op.drop_table(f'{tablename}') 
    pass
