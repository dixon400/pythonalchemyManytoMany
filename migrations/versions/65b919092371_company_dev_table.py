"""company_dev_table

Revision ID: 65b919092371
Revises: c6e5abf57016
Create Date: 2023-05-29 19:58:47.782248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b919092371'
down_revision = 'c6e5abf57016'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('founding_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_devs',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    op.create_table('freebies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('devs_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['devs_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('freebies')
    op.drop_table('company_devs')
    op.drop_table('devs')
    op.drop_table('companies')
    # ### end Alembic commands ###
