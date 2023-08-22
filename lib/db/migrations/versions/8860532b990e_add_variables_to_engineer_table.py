"""add variables to engineer table

Revision ID: 8860532b990e
Revises: 7ef7afba919e
Create Date: 2023-08-21 21:56:59.731795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8860532b990e'
down_revision: Union[str, None] = '7ef7afba919e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('engineer', sa.Column('name', sa.String(), nullable=True))
    op.add_column('engineer', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('engineer', sa.Column('level', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('engineer', 'level')
    op.drop_column('engineer', 'last_name')
    op.drop_column('engineer', 'name')
    # ### end Alembic commands ###
