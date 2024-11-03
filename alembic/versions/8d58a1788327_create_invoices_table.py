"""create invoices table

Revision ID: 8d58a1788327
Revises: 
Create Date: 2024-11-03 17:52:50.711018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d58a1788327'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'invoices',
        sa.Column('task_id', sa.String, primary_key=True),
        sa.Column('task', sa.String, nullable=False),
        sa.Column('hours', sa.Integer, nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('discount', sa.Integer, nullable=False),
        sa.Column('unit_price', sa.Integer, nullable=False),
    )

def downgrade():
    op.drop_table('invoices')
