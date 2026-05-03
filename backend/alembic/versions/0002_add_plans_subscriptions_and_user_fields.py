"""add plans, subscriptions and user fields

Revision ID: 0002_add_plans_subs
Revises: 0001_initial
Create Date: 2026-05-03
"""
from alembic import op
import sqlalchemy as sa

revision = '0002_add_plans_subs'
down_revision = '0001_initial'
branch_labels = None
depends_on = None


def upgrade():
    # add new columns to users
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=False, server_default=sa.text('0')))
    op.add_column('users', sa.Column('verification_token', sa.String(length=255), nullable=True, index=True))
    op.add_column('users', sa.Column('reset_token', sa.String(length=255), nullable=True, index=True))
    op.add_column('users', sa.Column('reset_expires_at', sa.DateTime(), nullable=True))

    # create plans table
    op.create_table(
        'plans',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False, unique=True),
        sa.Column('price_cents', sa.Integer(), nullable=False, server_default=sa.text('0')),
        sa.Column('currency', sa.String(length=10), nullable=False, server_default=sa.text("'INR'")),
        sa.Column('monthly', sa.Boolean(), nullable=False, server_default=sa.text('1')),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # create subscriptions table
    op.create_table(
        'subscriptions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('plan_id', sa.Integer, sa.ForeignKey('plans.id', ondelete='SET NULL'), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False, server_default=sa.text('0')),
        sa.Column('provider', sa.String(length=255), nullable=True),
        sa.Column('provider_id', sa.String(length=255), nullable=True),
        sa.Column('started_at', sa.DateTime(), nullable=True),
        sa.Column('expires_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table('subscriptions')
    op.drop_table('plans')
    op.drop_column('users', 'reset_expires_at')
    op.drop_column('users', 'reset_token')
    op.drop_column('users', 'verification_token')
    op.drop_column('users', 'is_verified')
