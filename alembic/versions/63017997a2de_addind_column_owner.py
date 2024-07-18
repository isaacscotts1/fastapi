"""addind column owner

Revision ID: 63017997a2de
Revises: acb7c76e0df4
Create Date: 2024-07-17 17:26:05.000947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63017997a2de'
down_revision: Union[str, None] = 'acb7c76e0df4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("email",sa.Integer(),nullable=False))
    op.create_unique_constraint("uniu","posts",["email"])
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name="uniu",table_name="posts",type_="unique")
    pass
