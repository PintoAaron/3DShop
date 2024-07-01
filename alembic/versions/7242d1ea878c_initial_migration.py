"""initial migration

Revision ID: 7242d1ea878c
Revises: 
Create Date: 2024-06-30 11:46:18.776497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7242d1ea878c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('staff', 'admin', name='roletype'), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('orders',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.UUID(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_image')
    op.drop_table('order_item')
    op.drop_table('cart_item')
    op.drop_table('product')
    op.drop_table('orders')
    op.drop_table('user')
    op.drop_table('category')
    op.drop_table('cart')
    # ### end Alembic commands ###