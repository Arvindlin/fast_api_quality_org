"""org_level_2

Revision ID: 095223ac0938
Revises: 78bb6c7ea26c
Create Date: 2023-07-10 14:59:25.866754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '095223ac0938'
down_revision = '78bb6c7ea26c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organizations_level2', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_md_wqms_mock_organizations_level2_organization_id'), 'organizations_level2', ['organization_id'], unique=False, schema='md_wqms_mock')
    op.drop_constraint('organizations_level2_ibfk_1', 'organizations_level2', type_='foreignkey')
    op.create_foreign_key(None, 'organizations_level2', 'organizations', ['organization_id'], ['id'], source_schema='md_wqms_mock', referent_schema='md_wqms_mock')
    op.create_foreign_key(None, 'organizations_level2', 'organizations', ['level1_id'], ['id'], source_schema='md_wqms_mock', referent_schema='md_wqms_mock')
    op.drop_constraint('permissions_ibfk_1', 'permissions', type_='foreignkey')
    op.create_foreign_key(None, 'permissions', 'roles', ['role_id'], ['id'], source_schema='md_wqms_mock', referent_schema='md_wqms_mock')
    op.drop_constraint('roles_ibfk_1', 'roles', type_='foreignkey')
    op.create_foreign_key(None, 'roles', 'organizations', ['organization_id'], ['id'], source_schema='md_wqms_mock', referent_schema='md_wqms_mock')
    op.add_column('users', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_password_reset', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('password_reset_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'password_reset_date')
    op.drop_column('users', 'is_password_reset')
    op.drop_column('users', 'status')
    op.drop_constraint(None, 'roles', schema='md_wqms_mock', type_='foreignkey')
    op.create_foreign_key('roles_ibfk_1', 'roles', 'organizations', ['organization_id'], ['id'])
    op.drop_constraint(None, 'permissions', schema='md_wqms_mock', type_='foreignkey')
    op.create_foreign_key('permissions_ibfk_1', 'permissions', 'roles', ['role_id'], ['id'])
    op.drop_constraint(None, 'organizations_level2', schema='md_wqms_mock', type_='foreignkey')
    op.drop_constraint(None, 'organizations_level2', schema='md_wqms_mock', type_='foreignkey')
    op.create_foreign_key('organizations_level2_ibfk_1', 'organizations_level2', 'organizations', ['level1_id'], ['id'])
    op.drop_index(op.f('ix_md_wqms_mock_organizations_level2_organization_id'), table_name='organizations_level2', schema='md_wqms_mock')
    op.drop_column('organizations_level2', 'organization_id')
    # ### end Alembic commands ###
