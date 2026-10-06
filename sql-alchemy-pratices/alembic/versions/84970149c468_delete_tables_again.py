"""delete_tables_again

Revision ID: 84970149c468
Revises: 53787ecc6266
Create Date: 2026-10-06 17:28:55.871157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84970149c468'
down_revision: Union[str, Sequence[str], None] = '53787ecc6266'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    tables = ['membersnewnain', 'membersnewname', 'membersnewnana']
    for tablename in tables: op.drop_table(f'{tablename}') 
    pass
