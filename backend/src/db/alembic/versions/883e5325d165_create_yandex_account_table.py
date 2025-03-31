"""create_yandex_account_table

Revision ID: 883e5325d165
Revises: b66edaba9d78
Create Date: 2025-03-29 21:25:37.664072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '883e5325d165'
down_revision: Union[str, None] = 'b66edaba9d78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('yandex_account_table',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('default_email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('yandex_account_table')
    # ### end Alembic commands ###
