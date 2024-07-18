#""create posts table

#Revision ID: 728ba10f59c2
#Revises: 
#Create Date: 2024-07-15 11:57:11.961104

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '728ba10f59c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("poster",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String(234),nullable=False))
    


def downgrade() -> None:
	op.drop_table("posts")
	
