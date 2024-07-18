"""i do

Revision ID: 4adafffea5d3
Revises: 684e14f3e6c0
Create Date: 2024-07-17 18:14:13.312095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4adafffea5d3'
down_revision: Union[str, None] = '684e14f3e6c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key("fku","posts","users",["owner_id"],["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name="fku",table_name="posts",type_="foreign_key")
    pass
