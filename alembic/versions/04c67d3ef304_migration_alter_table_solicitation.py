"""migration: alter table solicitation

Revision ID: 04c67d3ef304
Revises: f74f9e69110e
Create Date: 2023-04-24 19:52:35.184218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04c67d3ef304'
down_revision = 'f74f9e69110e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('FUNCTIONALITIES_application_id_fkey', 'FUNCTIONALITIES', type_='foreignkey')
    op.create_foreign_key(None, 'FUNCTIONALITIES', 'APPLICATIONS', ['application_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('LOGS_functionality_id_fkey', 'LOGS', type_='foreignkey')
    op.create_foreign_key(None, 'LOGS', 'FUNCTIONALITIES', ['functionality_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('SOLICITATIONS_user_id_fkey', 'SOLICITATIONS', type_='foreignkey')
    op.create_foreign_key(None, 'SOLICITATIONS', 'USERS', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'SOLICITATIONS', schema='public', type_='foreignkey')
    op.create_foreign_key('SOLICITATIONS_user_id_fkey', 'SOLICITATIONS', 'USERS', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'LOGS', schema='public', type_='foreignkey')
    op.create_foreign_key('LOGS_functionality_id_fkey', 'LOGS', 'FUNCTIONALITIES', ['functionality_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'FUNCTIONALITIES', schema='public', type_='foreignkey')
    op.create_foreign_key('FUNCTIONALITIES_application_id_fkey', 'FUNCTIONALITIES', 'APPLICATIONS', ['application_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
