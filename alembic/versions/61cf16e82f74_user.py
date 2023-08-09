"""user

Revision ID: 61cf16e82f74
Revises: 
Create Date: 2023-08-09 09:43:05.619674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61cf16e82f74'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(20),nullable=False),
        sa.Column('phone',sa.String(10),nullable=False),
        sa.Column('password',sa.String(10),nullable=False),
        sa.PrimaryKeyConstraint('id'),

    )


def downgrade() -> None:
    op.drop_table('user')
