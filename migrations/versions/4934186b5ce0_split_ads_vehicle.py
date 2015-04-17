"""Split ADS/Vehicle

Revision ID: 4934186b5ce0
Revises: 3c69c378bdb9
Create Date: 2015-04-17 15:09:20.976565

"""

# revision identifiers, used by Alembic.
revision = '4934186b5ce0'
down_revision = '3c69c378bdb9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.Column('added_via', sa.Enum('form', 'api', name='sources_enum'), nullable=False),
    sa.Column('source', sa.String(length=255), nullable=False),
    sa.Column('last_update_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('immatriculation', sa.String(length=80), nullable=False),
    sa.Column('modele', sa.String(length=255), nullable=True),
    sa.Column('annee', sa.Integer(), nullable=True),
    sa.Column('motorisation', sa.String(length=80), nullable=True),
    sa.Column('puissance', sa.Float(), nullable=True),
    sa.Column('type_', sa.Enum('sedan', 'mpv', 'station_wagon', 'normal', name="vehicle_type_enum"), nullable=True),
    sa.Column('relais', sa.Boolean(), nullable=True),
    sa.Column('pmr', sa.Boolean(), nullable=True),
    sa.Column('marque', sa.String(length=255), nullable=True),
    sa.Column('horodateur', sa.String(length=255), nullable=True),
    sa.Column('taximetre', sa.String(length=255), nullable=True),
    sa.Column('date_dernier_ct', sa.Date(), nullable=True),
    sa.Column('date_validite_ct', sa.Date(), nullable=True),
    sa.Column('luxary', sa.Boolean(), nullable=True),
    sa.Column('credit_card_accepted', sa.Boolean(), nullable=True),
    sa.Column('nfc_cc_accepted', sa.Boolean(), nullable=True),
    sa.Column('amex_accepted', sa.Boolean(), nullable=True),
    sa.Column('bank_check_accepted', sa.Boolean(), nullable=True),
    sa.Column('fresh_drink', sa.Boolean(), nullable=True),
    sa.Column('dvd_player', sa.Boolean(), nullable=True),
    sa.Column('wifi', sa.Boolean(), nullable=True),
    sa.Column('baby_seat', sa.Boolean(), nullable=True),
    sa.Column('bike_accepted', sa.Boolean(), nullable=True),
    sa.Column('pet_accepted', sa.Boolean(), nullable=True),
    sa.Column('AC_vehicle', sa.Boolean(), nullable=True),
    sa.Column('telepeage', sa.Boolean(), nullable=True),
    sa.Column('gps', sa.Boolean(), nullable=True),
    sa.Column('conventionne', sa.Boolean(), nullable=True),
    sa.Column('every_destination', sa.Boolean(), nullable=True),
    sa.Column('color', sa.String(length=255), nullable=True),
    sa.Column('snv', sa.Boolean(), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'ADS', sa.Column('insee', sa.Integer(), nullable=True))
    op.add_column(u'ADS', sa.Column('vehicle_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'ADS_ZUPC_id_fkey', 'ADS', type_='foreignkey')
    op.create_foreign_key(None, 'ADS', 'vehicle', ['vehicle_id'], ['id'])
    op.drop_column(u'ADS', 'horodateur')
    op.drop_column(u'ADS', 'pmr')
    op.drop_column(u'ADS', 'color')
    op.drop_column(u'ADS', 'marque')
    op.drop_column(u'ADS', 'date_dernier_ct')
    op.drop_column(u'ADS', 'date_validite_ct')
    op.drop_column(u'ADS', 'credit_card_accepted')
    op.drop_column(u'ADS', 'fresh_drink')
    op.drop_column(u'ADS', 'immatriculation')
    op.drop_column(u'ADS', 'dvd_player')
    op.drop_column(u'ADS', 'telepeage')
    op.drop_column(u'ADS', 'taximetre')
    op.drop_column(u'ADS', 'every_destination')
    op.drop_column(u'ADS', 'puissance')
    op.drop_column(u'ADS', 'nfc_cc_accepted')
    op.drop_column(u'ADS', 'baby_seat')
    op.drop_column(u'ADS', 'amex_accepted')
    op.drop_column(u'ADS', 'gps')
    op.drop_column(u'ADS', 'pet_accepted')
    op.drop_column(u'ADS', 'luxary')
    op.drop_column(u'ADS', 'relais')
    op.drop_column(u'ADS', 'snv')
    op.drop_column(u'ADS', 'bank_check_accepted')
    op.drop_column(u'ADS', 'annee')
    op.drop_column(u'ADS', 'modele')
    op.drop_column(u'ADS', 'conventionne')
    op.drop_column(u'ADS', 'wifi')
    op.drop_column(u'ADS', 'type_')
    op.drop_column(u'ADS', 'AC_vehicle')
    op.drop_column(u'ADS', 'bike_accepted')
    op.drop_column(u'ADS', 'motorisation')
    op.drop_column(u'ADS', 'ZUPC_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'ADS', sa.Column('ZUPC_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('motorisation', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('bike_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('AC_vehicle', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('type_', postgresql.ENUM(u'sedan', u'mpv', u'station_wagon', u'normal', name='vehicle_type'), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('wifi', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('conventionne', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('modele', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('annee', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('bank_check_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('snv', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('relais', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('luxary', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('pet_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('gps', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('amex_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('baby_seat', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('nfc_cc_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('puissance', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('every_destination', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('taximetre', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('telepeage', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('dvd_player', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('immatriculation', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column(u'ADS', sa.Column('fresh_drink', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('credit_card_accepted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('date_validite_ct', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('date_dernier_ct', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('marque', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('color', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('pmr', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'ADS', sa.Column('horodateur', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'ADS', type_='foreignkey')
    op.create_foreign_key(u'ADS_ZUPC_id_fkey', 'ADS', 'ZUPC', ['ZUPC_id'], ['id'])
    op.drop_column(u'ADS', 'vehicle_id')
    op.drop_column(u'ADS', 'insee')
    op.drop_table('vehicle')
    ### end Alembic commands ###
