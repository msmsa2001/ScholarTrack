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

gender_type=sa.Enum('M','F',name="GenderType")

def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(20),nullable=False),
        sa.Column('phone',sa.String(10),nullable=False),
        sa.Column('password',sa.String(10),nullable=False),
        sa.Column('isAdmin',sa.Boolean(),nullable=False, default=False),
        sa.Column('created_on',
                  sa.DateTime(),
                  nullable=False, 
                  server_default=sa.text("now()")),
        sa.Column('created_by',sa.Integer(),nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'basic_details',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('first_name',sa.String(20),nullable=False),
        sa.Column('last_name',sa.String(20),nullable=False),
        sa.Column('gender',gender_type),
        sa.Column('dob',sa.Date(),nullable=False),
        sa.Column('photo',sa.String(100),nullable=True),
        sa.Column('ssc_mark',sa.Integer(),nullable=True),
        sa.Column('ssc_year',sa.Date,nullable=True),
        sa.Column('hsc',sa.Integer(),nullable=True),
        sa.Column('hsc_year',sa.Date,nullable=True),
        sa.Column('graduaction_mark',sa.Integer(),nullable=True),
        sa.Column('graduaction_year',sa.Date,nullable=True),
        sa.Column('joinning_date',sa.Date(),nullable=True),
        sa.Column('user_id',sa.Integer(),nullable=False),
        sa.ForeignKeyConstraint(['user_id'],['user.id']),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('user')
    op.drop_table('basic_details')
    gender_type.drop(op.get_bind(),checkfirst=False)
