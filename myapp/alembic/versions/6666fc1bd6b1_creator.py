"""creator

Revision ID: 6666fc1bd6b1
Revises: 728ba10f59c2
Create Date: 2024-07-15 22:40:47.684212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6666fc1bd6b1'
down_revision: Union[str, None] = '728ba10f59c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
