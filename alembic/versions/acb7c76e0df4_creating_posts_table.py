"""creating posts table

Revision ID: acb7c76e0df4
Revises: 
Create Date: 2024-07-17 17:15:17.429035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acb7c76e0df4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",sa.Column("id",sa.Integer(),nullable=False))
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    op.drop_table("users")
    pass
