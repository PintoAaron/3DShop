"""empty message

Revision ID: e66453f9e8cd
Revises: 
Create Date: 2024-04-05 12:25:04.364646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e66453f9e8cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.String(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    op.drop_table('products')
    op.drop_table('customers')
    # ### end Alembic commands ###
