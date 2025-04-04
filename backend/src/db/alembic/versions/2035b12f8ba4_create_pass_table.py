"""create_pass_table

Revision ID: 2035b12f8ba4
Revises: 73248d775db5
Create Date: 2025-03-30 16:02:31.153001

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "2035b12f8ba4"
down_revision: Union[str, None] = "73248d775db5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "passwords_table",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_password_user_id", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("passwords_table")
    # ### end Alembic commands ###
