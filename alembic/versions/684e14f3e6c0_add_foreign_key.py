"""add foreign key

Revision ID: 684e14f3e6c0
Revises: 63017997a2de
Create Date: 2024-07-17 17:46:59.326089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '684e14f3e6c0'
down_revision: Union[str, None] = '63017997a2de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts","owner_id")
    pass
