
import os
import sys
import enum
import inspect
import datetime
import shutils
from datetime import timedelta, datetime, date

from sqlalchemy.orm import relationship, query, defer, deferred, column_property, mapper
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy import (Column, Integer, String, ForeignKey,
    Sequence, Float, Text, BigInteger, Date,
    DateTime, Time, Boolean, Index, CheckConstraint,
    UniqueConstraint, ForeignKeyConstraint, Numeric, LargeBinary , Table, func, Enum,
    text)

# IMPORT Postgresql Specific Types
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR, aggregate_order_by )

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin
from flask_appbuilder.filemanager import ImageManager

from flask_appbuilder.models.decorators import renders
from sqlalchemy_utils import aggregated, force_auto_coercion, observes
from sqlalchemy_utils.types import TSVectorType   #Searchability look at DocMixin
from sqlalchemy.ext.associationproxy import association_proxy

from flask_appbuilder.security.sqla.models import User
from geoalchemy2 import Geometry

# To create GraphSQL API
# import graphene
# from graphene_sqlalchemy import SQLAlchemyObjectType

# Versioning Mixin
# from sqlalchemy_continuum import make_versioned
#Add __versioned__ = {}


# from sqlalchemy_searchable import make_searchable
# from flask_graphql import GraphQLView

# ActiveRecord Model Features
# from sqlalchemy_mixins import AllFeaturesMixin, ActiveRecordMixin


from .mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')

# UTILITY CLASSES
# import arrow,


# Initialize sqlalchemy_utils
#force_auto_coercion()
# Keep versions of all data
# make_versioned()
# make_searchable()


class Status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'


class Agent_type(enum.Enum):
   INDIVIDUAL = 'Individual'
   BUSINESS_NAME = 'Business_Name'
   SOLE_PROPRIETORSHIP = 'Sole_Proprietorship'
   PRIVATE_LIMITED_COMPANY = 'Private_Limited_Company'
   PUBLIC_LIMITED_COMPANY = 'Public_Limited_Company'
   PUBLIC_COMPANY_LIMITED_BY_GUARANTEE = 'Public_Company_Limited_by_Guarantee'
   PRIVATE_UNLIMITED_COMPANY = 'Private_Unlimited_Company'
   PUBLIC_UNLIMITED_COMPANY = 'Public_Unlimited_Company'


class Agent_role(enum.Enum):
   AGENT = 'agent'
   SUPER_AGENT = 'super_agent'
   AGGREGATOR = 'aggregator'


class Kyc_verification_status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'


class Verification_status(enum.Enum):
   PENDING = 'pending'
   KYC_SUBMITTED = 'kyc_submitted'
   KYC_APPROVED = 'kyc_approved'
   KYC_REJECTED = 'kyc_rejected'
   ESCALATED = 'escalated'
   CONTRACTED = 'contracted'
   ACTIVE = 'active'
   SUSPENDED = 'suspended'
   INACTIVE = 'inactive'
   CONTRACT_TERMINATED = 'contract_terminated'
   DOCS_EXPIRED = 'docs_expired'
   UNDER_REVIEW = 'under_review'
   LOCKED = 'locked'
   AWAITING_RENEWAL = 'awaiting_renewal'
   RENEWAL_REJECTED = 'renewal_rejected'
   VERIFICATION_FAILED = 'verification_failed'


class Person_role(enum.Enum):
   NEXT_OF_KIN = 'next_of_kin'
   COMPANY_DIRECTOR = 'company_director'
   POS_OPERATOR = 'pos_operator'
   FIELD_SUPPORT = 'field_support'
   CUSTOMER = 'customer'
   REFEREE = 'referee'
   SUPERVISOR = 'supervisor'


class Gender(enum.Enum):
   MALE = 'Male'
   FEMALE = 'Female'
   NON_BINARY = 'Non_Binary'
   PREFER_NOT_TO_SAY = 'Prefer_Not_to_Say'
   OTHER = 'Other'






class Transaction_type(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'


class Card_trans_type(enum.Enum):
   PURCHASE = 'purchase'
   BALANCE = 'balance'
   REFUND = 'refund'
   CASH_ADVANCE = 'cash_advance'
   CASH_BACK = 'cash_back'
   PRE_AUTHORIZATION = 'pre_authorization'
   PRE_AUTHORIZATION_COMPLETION = 'pre_authorization_completion'
   CARD_VERIFICATION = 'card_verification'
   TRANSACTION = 'transaction'
   SETTLEMENT = 'settlement'


class Trans_status(enum.Enum):
   PENDING = 'pending'
   AUTHORIZED = 'authorized'
   COMPLETED = 'completed'
   FAILED = 'failed'
   CANCELLED = 'cancelled'
   REFUNDED = 'refunded'
   REVERSED = 'reversed'
   HOLD = 'hold'
   SUSPENDED = 'suspended'
   DISPUTED = 'disputed'
   DELIVERED = 'delivered'
   SETTLEMENT_PENDING = 'settlement_pending'
   SETTLED = 'settled'
   REJECTED = 'rejected'
   EXPIRED = 'expired'
   PENDING_VERIFICATION = 'pending_verification'
   HOLD_FOR_REVIEW = 'hold_for_review'
   PARTIALLY_COMPLETED = 'partially_completed'
   PARTIALLY_REFUNDED = 'partially_refunded'
   PARTIALLY_REVERSED = 'partially_reversed'
   COMPLETED_WITH_ERRORS = 'completed_with_errors'
   BATCH_PROCESSING = 'batch_processing'
   DEFERRED = 'deferred'
   WAITING_FOR_AUTHORIZATION = 'waiting_for_authorization'
   PROCESSING = 'processing'
   PENDING_FUNDS_AVAILABILITY = 'pending_funds_availability'
   PENDING_REVIEW = 'pending_review'
   PENDING_CONFIRMATION = 'pending_confirmation'
   WAITING_FOR_SETTLEMENT = 'waiting_for_settlement'
   PENDING_RECONCILIATION = 'pending_reconciliation'
   PENDING_DISBURSEMENT = 'pending_disbursement'
   CHARGEBACK_INITIATED = 'chargeback_initiated'
   CHARGEBACK_RESOLVED = 'chargeback_resolved'
   PENDING_CAPTURE = 'pending_capture'
   CAPTURED = 'captured'
   VOIDED = 'voided'
   IN_QUEUE = 'in_queue'
   MANUAL_INTERVENTION_REQUIRED = 'manual_intervention_required'
   GATEWAY_TIMEOUT = 'gateway_timeout'
   FRAUD_ALERT = 'fraud_alert'
   UNDER_AUDIT = 'under_audit'
   AUDIT_COMPLETED = 'audit_completed'
   CURRENCY_CONVERSION = 'currency_conversion'
   CURRENCY_CONVERSION_COMPLETED = 'currency_conversion_completed'
   ESCALATED = 'escalated'
   DE_ESCALATED = 'de_escalated'
   PENDING_APPROVAL = 'pending_approval'
   APPROVED = 'approved'
   DECLINED = 'declined'
   RE_ATTEMPTED = 're_attempted'
   RE_SCHEDULED = 're_scheduled'
   INSUFFICIENT_FUNDS = 'insufficient_funds'
   VERIFICATION_FAILED = 'verification_failed'
   VERIFICATION_SUCCESSFUL = 'verification_successful'
   PENDING_CLEARANCE = 'pending_clearance'
   CLEARED = 'cleared'
   RE_INITIATED = 're_initiated'
   SPLIT_TRANSACTION = 'split_transaction'
   CONSOLIDATED = 'consolidated'


class Origin_source(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'


class Trans_dest(enum.Enum):
   CASH = 'cash'
   CREDIT_CARD = 'credit_card'
   DEBIT_CARD = 'debit_card'
   PREPAID_CARD = 'prepaid_card'
   COMMERCIAL_CARD = 'commercial_card'
   DEBT = 'debt'
   BANK = 'bank'
   MOBILE = 'mobile'
   COUPON = 'coupon'
   ORDER = 'order'
   WITHDRAWAL = 'withdrawal'
   FUND_WALLET = 'fund_wallet'
   CHEQUE = 'cheque'
   BANK_TRANSFER = 'bank_transfer'
   CRYPTO = 'crypto'
   BARTER = 'barter'
   WIRE_TRANSFER = 'wire_transfer'
   CONTACTLESS = 'contactless'
   GIFT_CARD = 'gift_card'
   LOYALTY_POINTS = 'loyalty_points'
   MONEY_ORDER = 'money_order'
   ESCROW = 'escrow'
   INSTALLMENT = 'installment'
   INVOICE = 'invoice'
   PREPAID = 'prepaid'
   QR_CODE = 'qr_code'
   DIGITAL_WALLET = 'digital_wallet'
   AUTOMATIC_DEBIT = 'automatic_debit'
   CASH_ON_DELIVERY = 'cash_on_delivery'
   POSTPAID = 'postpaid'
   THIRD_PARTY = 'third_party'
   TRADE_CREDIT = 'trade_credit'


class Country(Model):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String)
    country_code = Column(String)
    country_phone_code = Column(Integer)

    def __repr__(self):
       return self.country_name

 ### 

class State(Model):
    __tablename__ = "state"

    country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    state_id = Column(Integer, primary_key=True, autoincrement=True)
    state_code = Column(String)
    state_name = Column(String)
    state_desc = Column(Text)
    state_country = relationship(Country, backref='states_state_country', primaryjoin='State.country_id_fk == Country.country_id')

    def __repr__(self):
       return self.state_name

 ### 

class Lga(Model):
    __tablename__ = "lga"

    state_id_fk = Column(Integer, ForeignKey('state.state_id'))
    lga_id = Column(Integer, primary_key=True, autoincrement=True)
    lga_code = Column(String)
    lga_name = Column(String)
    lga_state = relationship(State, backref='lgas_lga_state', primaryjoin='Lga.state_id_fk == State.state_id')

    def __repr__(self):
       return self.lga_name

 ### 

class DocType(Model):
    __tablename__ = "doc_type"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Unique identifier for the document type.")
    name = Column(String, comment="Name or title of the document type e.g. Passport, Driver"s License.")
    notes = Column(Text, comment="Any additional remarks or details about the document type.")
    required_information = Column(Text, comment="List or description of required fields/information for this document type.")
    is_serialized = Column(Boolean, default = False)
    serial_length = Column(Integer)
    expires = Column(Boolean, default = False)
    category = Column(String, comment="Category or classification of the document, e.g., Identification, Certification, Financial.")
    validity_period = Column(Integer, comment="Standard validity duration of this type of document in days.")
    renewal_frequency = Column(Integer, comment="Frequency at which this document typically needs renewal, in days. Useful for setting reminders.")
    is_government_issued = Column(Boolean, default = False, comment="Indicates if this document is typically issued by a government authority.")
    is_digital = Column(Boolean, default = False, comment="Indicates if the document is typically in digital format.")
    template_url = Column(String, comment="URL or link to a template or sample of this document type, if available.")
    example_image_url = Column(String, comment="URL or link to an example image of this document type.")
    created_at = Column(DateTime, server_default=text('NOW())', default = '2024-01-09 17, comment="Timestamp when the document type was added to the system.")
    updated_at = Column(DateTime, server_default=text('NOW())', default = '2024-01-09 17, comment="Timestamp when the document type was last updated.")

    def __repr__(self):
       return self.name

 ### 

class Bank(Model):
    __tablename__ = "bank"

    bank_id = Column(Integer, primary_key=True, autoincrement=True)
    bank_code = Column(String, comment="NIBSS institutionCode")
    bank_name = Column(String)
    bank_category = Column(Integer, default = 2, comment="category")
    swift_code = Column(String)
    sort_code = Column(String)
    iban = Column(String)
    cust_care_phone = Column(String)
    cust_care_email = Column(String)
    escalation_contact = Column(Text)
    created_on = Column(DateTime, server_default=text('NOW())', default = func.now())
    updated_on = Column(DateTime, server_default=text('NOW())', default = func.now())

    def __repr__(self):
       return self.bank_name

 ### 

class UserExt(Model):
    __tablename__ = "user_ext"

    user_ext_id = Column(Integer, primary_key=True, autoincrement=True)
    manager_id_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    user_first_name = Column(String)
    user_middle_name = Column(String)
    user_surname = Column(String)
    user_employee_number = Column(String)
    user_job_title = Column(String)
    user_phone_number = Column(String)
    user_email = Column(String)
    user_data = Column(Text)
    user_ext_manager = relationship('UserExt', backref='user_exts_user_ext_manager', primaryjoin='UserExt.manager_id_fk == UserExt.user_ext_id', remote_side=[user_ext_id])

    def __repr__(self):
       return self.user_first_name

 ### 

class AgentTier(Model):
    __tablename__ = "agent_tier"

    tier_id = Column(Integer, primary_key=True, autoincrement=True)
    tier_name = Column(String)
    tier_notes = Column(Text)

    def __repr__(self):
       return self.tier_name

 ### 

class Agent(Model):
    __tablename__ = "agent"

    agent_id = Column(Integer, primary_key=True, autoincrement=True)
    aggregator_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    is_aggregator = Column(Boolean, default = False)
    became_aggregator_date = Column(DateTime, server_default=text('NOW())')
    assigned_pos_count = Column(Integer, default = 0)
    aggregator_pos_threshold = Column(Integer, default = 20)
    status = Column(Enum(Status), name='t_status', nullable=False)
    agent_type = Column(Enum(Agent_type), name='t_agent_type', nullable=False)
    agent_role = Column(Enum(Agent_role), name='t_agent_role', nullable=False)
    agent_tier_id_fk = Column(Integer, ForeignKey('agent_tier.tier_id'))
    account_manager_id_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    agent_name = Column(String)
    alias = Column(String, comment="Use this for reports if available")
    phone_country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    phone = Column(String)
    phone_ext = Column(String)
    alt_phone_country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    alt_phone = Column(String)
    alt_phone_ext = Column(String)
    email = Column(String)
    alt_email = Column(String)
    bvn = Column(String)
    bvn_verified = Column(Boolean, default = False)
    bvn_verification_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    bvn_verification_code = Column(Text)
    tax_id = Column(String)
    bank_id_fk = Column(Integer, ForeignKey('bank.bank_id'))
    bank_acc_no = Column(String, comment="Transactions to this bank are free?")
    biz_name = Column(String)
    biz_state_id_fk = Column(Integer, ForeignKey('state.state_id'))
    biz_lga_id_fk = Column(Integer, ForeignKey('lga.lga_id'))
    biz_city = Column(String)
    biz_city_area = Column(String)
    biz_street = Column(String)
    biz_building = Column(String)
    biz_address = Column(Text)
    biz_poa_img = Column(String)
    biz_poa_desc = Column(String)
    biz_poa_valid = Column(Boolean, default = False)
    biz_lat = Column(Numeric)
    biz_lon = Column(Numeric)
    biz_loc = Column(Text)
    biz_ggl_code = Column(String)
    company_name = Column(String)
    cac_number = Column(String)
    cac_reg_date = Column(Date)
    cac_cert_img = Column(String)
    cac_cert_no = Column(String)
    ref_code = Column(String)
    access_pin = Column(String)
    registered_by_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    registration_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    reviewed_by_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    review_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    approved_by_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    approval_date = Column(DateTime, server_default=text('NOW())')
    approval_narrative = Column(Text)
    kyc_submit_date = Column(DateTime, server_default=text('NOW())')
    kyc_verification_status = Column(Enum(Kyc_verification_status), name='t_kyc_verification_status', nullable=False)
    kyc_approval_date = Column(DateTime, server_default=text('NOW())')
    kyc_ref_code = Column(String)
    kyc_rejection_narrative = Column(Text)
    kyc_rejection_by_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    rejection_date = Column(DateTime, server_default=text('NOW())')
    rejection_narrative = Column(Text)
    rejected_by_fk = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    face_matrix = Column(Text)
    finger_print_img = Column(Text)
    agent_public_key = Column(Text)
    agent_pj_expiry = Column(DateTime, server_default=text('NOW())')
    agent_history = Column(Text)
    agent_account_manager = relationship(UserExt, backref='agents_agent_account_manager', primaryjoin='Agent.account_manager_id_fk == UserExt.user_ext_id')
    agent_agent_tier = relationship(AgentTier, backref='agents_agent_agent_tier', primaryjoin='Agent.agent_tier_id_fk == AgentTier.tier_id')
    agent_aggregator = relationship('Agent', backref='agents_agent_aggregator', primaryjoin='Agent.aggregator_id_fk == Agent.agent_id', remote_side=[agent_id])
    agent_alt_phone_country = relationship(Country, backref='agents_agent_alt_phone_country', primaryjoin='Agent.alt_phone_country_id_fk == Country.country_id')
    agent_approved_by_fk_fkey = relationship(UserExt, backref='agents_agent_approved_by_fk_fkey', primaryjoin='Agent.approved_by_fk == UserExt.user_ext_id')
    agent_bank = relationship(Bank, backref='agents_agent_bank', primaryjoin='Agent.bank_id_fk == Bank.bank_id')
    agent_biz_lga = relationship(Lga, backref='agents_agent_biz_lga', primaryjoin='Agent.biz_lga_id_fk == Lga.lga_id')
    agent_biz_state = relationship(State, backref='agents_agent_biz_state', primaryjoin='Agent.biz_state_id_fk == State.state_id')
    agent_kyc_rejection_by_fk_fkey = relationship(UserExt, backref='agents_agent_kyc_rejection_by_fk_fkey', primaryjoin='Agent.kyc_rejection_by_fk == UserExt.user_ext_id')
    agent_phone_country = relationship(Country, backref='agents_agent_phone_country', primaryjoin='Agent.phone_country_id_fk == Country.country_id')
    agent_registered_by_fk_fkey = relationship(UserExt, backref='agents_agent_registered_by_fk_fkey', primaryjoin='Agent.registered_by_fk == UserExt.user_ext_id')
    agent_rejected_by_fk_fkey = relationship(UserExt, backref='agents_agent_rejected_by_fk_fkey', primaryjoin='Agent.rejected_by_fk == UserExt.user_ext_id')
    agent_reviewed_by_fk_fkey = relationship(UserExt, backref='agents_agent_reviewed_by_fk_fkey', primaryjoin='Agent.reviewed_by_fk == UserExt.user_ext_id')

    def __repr__(self):
       return self.alias

 ### 

class Doc(Model):
    __tablename__ = "doc"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Unique identifier for the document.")
    doc_type_id_fk = Column(Integer, ForeignKey('doc_type.id'), comment="References the type of document e.g. passport, license.")
    doc_name = Column(String, comment="Name or title of the document.")
    doc_content_type = Column(String, comment="MIME type of the document content e.g. application/pdf, image/jpeg.")
    identification_number = Column(String, comment="Unique identification number, e.g., passport number.")
    serial_number = Column(String, comment="Serial number of the document if applicable.")
    description = Column(Text, comment="Detailed description or remarks about the document.")
    file_name = Column(String, comment="Name of the file if stored digitally.")
    page_count = Column(Integer, comment="Number of pages in the document, if applicable.")
    doc_url = Column(Text, comment="Actual doc in pdf or other format")
    doc_length = Column(Integer, comment="Size of the document in bytes or another measure.")
    doc_text = Column(Text, comment="Text content extracted from the document. Useful for search and analytics. May be stored in another database for scalability.")
    issued_on = Column(Date, comment="The date when the document was issued.")
    issued_by_authority = Column(String, comment="Authority or organization that issued the document.")
    issued_at = Column(String, comment="Place or location where the document was issued.")
    expires_on = Column(Date, comment="Expiration date of the document.")
    expired = Column(Boolean, default = False, comment="Flag to indicate if the document has expired.")
    verified = Column(Boolean, default = False)
    verification_date = Column(DateTime, server_default=text('NOW())', default = func.now(), comment="The date when the document was verified.")
    verification_code = Column(Text)
    uploaded_on = Column(DateTime, server_default=text('NOW())', comment="Timestamp when the document was uploaded into the system.")
    updated_on = Column(DateTime, server_default=text('NOW())', default = '2024-01-09 17, comment="Timestamp when the document record was last updated.")
    doc_doc_type = relationship(DocType, backref='docs_doc_doc_type', primaryjoin='Doc.doc_type_id_fk == DocType.id')

    def __repr__(self):
       return self.doc_name

 ### 

class AgentDocLink(Model):
    __tablename__ = "agent_doc_link"

    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    doc_id_fk = Column(Integer, ForeignKey('doc.id'))
    verification_status = Column(Enum(Verification_status), name='t_verification_status', nullable=False)
    submit_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    agent_doc_link_agent = relationship(Agent, backref='agent_doc_links_agent_doc_link_agent', primaryjoin='AgentDocLink.agent_id_fk == Agent.agent_id')
    agent_doc_link_doc = relationship(Doc, backref='agent_doc_links_agent_doc_link_doc', primaryjoin='AgentDocLink.doc_id_fk == Doc.id')

    def __repr__(self):
       return self.agent_id_fk

 ### 

class Person(Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    next_of_kin_id_fk = Column(Integer, ForeignKey('person.id'))
    person_role = Column(Enum(Person_role), name='t_person_role', nullable=False)
    first_name = Column(String)
    middle_name = Column(String)
    surname = Column(String)
    nick_name = Column(String)
    gender = Column(Enum(Gender), name='t_gender', nullable=False)
    photo_img = Column(String)
    signature_img = Column(String)
    bvn_no = Column(String)
    bvn_verified = Column(Boolean, default = False)
    bvn_verification_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    bvn_verification_code = Column(Text)
    tax_id = Column(String)
    phone_country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    phone = Column(String)
    phone_ext = Column(String)
    email = Column(String)
    alt_phone_country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    alt_phone = Column(String)
    alt_phone_ext = Column(String)
    alt_email = Column(String)
    home_address = Column(Text)
    home_country_id_fk = Column(Integer, ForeignKey('country.country_id'))
    home_state_id_fk = Column(Integer, ForeignKey('state.state_id'))
    home_lga_id_fk = Column(Integer, ForeignKey('lga.lga_id'))
    home_city = Column(String)
    home_area = Column(String)
    home_street_address = Column(String)
    home_building_name = Column(String)
    nearby_landmark = Column(String)
    home_poa_img = Column(String)
    home_poa_desc = Column(String)
    home_poa_valid = Column(Boolean, default = False)
    home_lat = Column(Numeric)
    home_lon = Column(Numeric)
    home_loc = Column(Text)
    home_ggl_code = Column(String)
    person_agent = relationship(Agent, backref='persons_person_agent', primaryjoin='Person.agent_id_fk == Agent.agent_id')
    person_alt_phone_country = relationship(Country, backref='persons_person_alt_phone_country', primaryjoin='Person.alt_phone_country_id_fk == Country.country_id')
    person_home_country = relationship(Country, backref='persons_person_home_country', primaryjoin='Person.home_country_id_fk == Country.country_id')
    person_home_lga = relationship(Lga, backref='persons_person_home_lga', primaryjoin='Person.home_lga_id_fk == Lga.lga_id')
    person_home_state = relationship(State, backref='persons_person_home_state', primaryjoin='Person.home_state_id_fk == State.state_id')
    person_next_of_kin = relationship('Person', backref='persons_person_next_of_kin', primaryjoin='Person.next_of_kin_id_fk == Person.id', remote_side=[id])
    person_phone_country = relationship(Country, backref='persons_person_phone_country', primaryjoin='Person.phone_country_id_fk == Country.country_id')

    def __repr__(self):
       return self.first_name

 ### 

class PersonDocLink(Model):
    __tablename__ = "person_doc_link"

    person_id_fk = Column(Integer, ForeignKey('person.id'))
    doc_id_fk = Column(Integer, ForeignKey('doc.id'))
    verification_status = Column(Enum(Verification_status), name='t_verification_status', nullable=False)
    submit_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    person_doc_link_doc = relationship(Doc, backref='person_doc_links_person_doc_link_doc', primaryjoin='PersonDocLink.doc_id_fk == Doc.id')
    person_doc_link_person = relationship(Person, backref='person_doc_links_person_doc_link_person', primaryjoin='PersonDocLink.person_id_fk == Person.id')

    def __repr__(self):
       return self.person_id_fk

 ### 

class Pos(Model):
    __tablename__ = "pos"

    pos_id = Column(Integer, primary_key=True, autoincrement=True)
    serial_no = Column(String)
    imei = Column(String)
    mac_addr = Column(String)
    device_model = Column(String)
    device_make = Column(String)
    device_mfg = Column(String)
    os_version = Column(String)
    device_color = Column(String)
    device_condition = Column(String, comment="working, irreparrable, repaired")
    status = Column(String)
    owner_type = Column(String)
    registration_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    assigned = Column(Boolean, default = False)
    assigned_date = Column(DateTime, server_default=text('NOW())')
    assigned_narrative = Column(Text)
    active = Column(Boolean, default = False)
    activation_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    last_active = Column(DateTime, server_default=text('NOW())')
    deployed = Column(Boolean, default = False)
    deploy_date = Column(DateTime, server_default=text('NOW())')
    deploy_narrative = Column(Text)
    returned = Column(Boolean, default = False)
    return_date = Column(DateTime, server_default=text('NOW())')
    return_narrative = Column(Text)
    return_received_date = Column(DateTime, server_default=text('NOW())')
    return_received_by = Column(Integer, ForeignKey('user_ext.user_ext_id'))
    state_id = Column(Integer, ForeignKey('state.state_id'))
    lga_id = Column(Integer, ForeignKey('lga.lga_id'))
    street_address = Column(String)
    building_name = Column(String)
    contact_phone_num = Column(String)
    pos_user = Column(String)
    crypt_priv_key = Column(Text)
    crypt_pub_key = Column(Text)
    crypt_password = Column(Text)
    override_key = Column(Text)
    pos_lga = relationship(Lga, backref='poss_pos_lga', primaryjoin='Pos.lga_id == Lga.lga_id')
    pos_return_received_by_fkey = relationship(UserExt, backref='poss_pos_return_received_by_fkey', primaryjoin='Pos.return_received_by == UserExt.user_ext_id')
    pos_state = relationship(State, backref='poss_pos_state', primaryjoin='Pos.state_id == State.state_id')

    def __repr__(self):
       return self.device_model

 ### 

class PosAgentLink(Model):
    __tablename__ = "pos_agent_link"

    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'), primary_key=True)
    pos_id_fk = Column(Integer, ForeignKey('pos.pos_id'), primary_key=True)
    assigned_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    assigned_by = Column(String, comment="user")
    received_by = Column(String)
    received_date = Column(DateTime, server_default=text('NOW())')
    received_location = Column(String)
    delivery_note = Column(Text)
    delivery_note_printed = Column(Boolean, default = False)
    activated = Column(Boolean, default = False)
    activation_date = Column(DateTime, server_default=text('NOW())')
    activation_otp = Column(String)
    otp_sent = Column(Boolean, default = False)
    otp_sent_time = Column(DateTime, server_default=text('NOW())')
    otp_used = Column(Boolean, default = False)
    history = Column(Text)
    pos_agent_link_agent = relationship(Agent, backref='pos_agent_links_pos_agent_link_agent', primaryjoin='PosAgentLink.agent_id_fk == Agent.agent_id')
    pos_agent_link_pos = relationship(Pos, backref='pos_agent_links_pos_agent_link_pos', primaryjoin='PosAgentLink.pos_id_fk == Pos.pos_id')

    def __repr__(self):
       return self.agent_id_fk

 ### 

class TokenProvider(Model):
    __tablename__ = "token_provider"

    token_provider_id = Column(Integer, primary_key=True, autoincrement=True)
    token_provider_name = Column(String)
    token_provioder_notes = Column(Text)
    token_provider_priv_key = Column(Text)
    token_provider_pub_key = Column(Text)
    token_provider_endpoint = Column(Text)
    token_provider_protocol = Column(Text)
    token_provider_ssl = Column(Text)
    token_provider_ip_whitelist = Column(Text)
    token_provider_password = Column(String)

    def __repr__(self):
       return self.token_provider_name

 ### 

class BillerCategory(Model):
    __tablename__ = "biller_category"

    biller_cat_id = Column(Integer, primary_key=True, autoincrement=True)
    biller_cat_name = Column(String)
    biller_cat_notes = Column(Text)

    def __repr__(self):
       return self.biller_cat_name

 ### 

class Biller(Model):
    __tablename__ = "biller"

    biller_id = Column(Integer, primary_key=True, autoincrement=True)
    biller_cat_id_fk = Column(Integer, ForeignKey('biller_category.biller_cat_id'))
    biller_code = Column(String)
    biller_name = Column(String)
    biller_url = Column(String)
    biller_note = Column(Text)
    biller_biller_cat = relationship(BillerCategory, backref='billers_biller_biller_cat', primaryjoin='Biller.biller_cat_id_fk == BillerCategory.biller_cat_id')

    def __repr__(self):
       return self.biller_name

 ### 

class BillerOffering(Model):
    __tablename__ = "biller_offering"

    biller_id_fk = Column(Integer, ForeignKey('biller.biller_id'))
    biller_offering_id = Column(Integer, primary_key=True, autoincrement=True)
    offering_name = Column(String)
    offering_description = Column(Text)
    offering_price = Column(numeric(10, 2))
    biller_offering_biller = relationship(Biller, backref='biller_offerings_biller_offering_biller', primaryjoin='BillerOffering.biller_id_fk == Biller.biller_id')

    def __repr__(self):
       return self.offering_name

 ### 

class Promotion(Model):
    __tablename__ = "promotion"

    promo_id = Column(Integer, primary_key=True, autoincrement=True)
    promo_name = Column(String)
    promo_notes = Column(Text)
    promo_start_date = Column(DateTime, server_default=text('NOW())')
    promo_end_date = Column(DateTime, server_default=text('NOW())')

    def __repr__(self):
       return self.promo_name

 ### 

class TransType(Model):
    __tablename__ = "trans_type"

    tt_id = Column(Integer, primary_key=True, autoincrement=True)
    tt_name = Column(String, comment="Deposit, Withdrawal, Transfer, Bill Payment, etc")
    tt_notes = Column(Text)

    def __repr__(self):
       return self.tt_name

 ### 

class CustomerSegment(Model):
    __tablename__ = "customer_segment"

    cs_id = Column(Integer, primary_key=True, autoincrement=True)
    cs_name = Column(String)
    cs_notes = Column(Text)

    def __repr__(self):
       return self.cs_name

 ### 

class CommRef(Model):
    __tablename__ = "comm_ref"

    cr_id = Column(Integer, primary_key=True, autoincrement=True)
    agent_type = Column(Enum(Agent_type), name='t_agent_type', nullable=False)
    agent_tier_level = Column(Integer, ForeignKey('agent_tier.tier_id'))
    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    state_id_fk = Column(Integer, ForeignKey('state.state_id'))
    lga_id_fk = Column(Integer, ForeignKey('lga.lga_id'))
    biller_id_fk = Column(Integer, ForeignKey('biller.biller_id'))
    biller_offering_id_fk = Column(Integer, ForeignKey('biller_offering.biller_offering_id'))
    transaction_type_id_fk = Column(Integer, ForeignKey('trans_type.tt_id'))
    customer_segment_id_fk = Column(Integer, ForeignKey('customer_segment.cs_id'), comment="Customer Segment")
    special_promotion_id_fk = Column(Integer, ForeignKey('promotion.promo_id'))
    min_trans_amount = Column(numeric(10, 2), default = 0)
    max_trans_amount = Column(numeric(10, 2))
    min_max_step = Column(Integer)
    min_comm_amount = Column(numeric(10, 2), default = 0)
    max_comm_amount = Column(numeric(10, 2))
    commission_rate = Column(numeric(10, 5))
    start_time = Column(Time, comment="Start Time of Commission Rate Validity")
    end_time = Column(Time, comment="End Time of Commission Rate Validity")
    start_date = Column(Date, comment="In case this commission rate is only valid for a period")
    end_date = Column(Date)
    comm_ref_agent = relationship(Agent, backref='comm_refs_comm_ref_agent', primaryjoin='CommRef.agent_id_fk == Agent.agent_id')
    comm_ref_agent_tier_level_fkey = relationship(AgentTier, backref='comm_refs_comm_ref_agent_tier_level_fkey', primaryjoin='CommRef.agent_tier_level == AgentTier.tier_id')
    comm_ref_biller = relationship(Biller, backref='comm_refs_comm_ref_biller', primaryjoin='CommRef.biller_id_fk == Biller.biller_id')
    comm_ref_biller_offering = relationship(BillerOffering, backref='comm_refs_comm_ref_biller_offering', primaryjoin='CommRef.biller_offering_id_fk == BillerOffering.biller_offering_id')
    comm_ref_customer_segment = relationship(CustomerSegment, backref='comm_refs_comm_ref_customer_segment', primaryjoin='CommRef.customer_segment_id_fk == CustomerSegment.cs_id')
    comm_ref_lga = relationship(Lga, backref='comm_refs_comm_ref_lga', primaryjoin='CommRef.lga_id_fk == Lga.lga_id')
    comm_ref_special_promotion = relationship(Promotion, backref='comm_refs_comm_ref_special_promotion', primaryjoin='CommRef.special_promotion_id_fk == Promotion.promo_id')
    comm_ref_state = relationship(State, backref='comm_refs_comm_ref_state', primaryjoin='CommRef.state_id_fk == State.state_id')
    comm_ref_transaction_type = relationship(TransType, backref='comm_refs_comm_ref_transaction_type', primaryjoin='CommRef.transaction_type_id_fk == TransType.tt_id')

    def __repr__(self):
       return self.cr_id

 ### 

class TokenLists(Model):
    __tablename__ = "token_lists"

    token_id = Column(Integer, primary_key=True, autoincrement=True)
    token_provider_id = Column(Integer, ForeignKey('token_provider.token_provider_id'))
    token_validity = Column(Integer)
    token_expired = Column(Boolean, default = False)
    token_expiry_date = Column(DateTime, server_default=text('NOW())')
    token_name = Column(String)
    token_value = Column(String)
    token_password = Column(String)
    token_notes = Column(Text)
    token_client_secret = Column(Text)
    token_lists_token_provider = relationship(TokenProvider, backref='token_listss_token_lists_token_provider', primaryjoin='TokenLists.token_provider_id == TokenProvider.token_provider_id')

    def __repr__(self):
       return self.token_name

 ### 

class TransRoutingThresholds(Model):
    __tablename__ = "trans_routing_thresholds"

    trans_route_id = Column(Integer, primary_key=True, autoincrement=True)
    trans_route_name = Column(String)
    trans_route_min = Column(numeric(10, 2))
    trans_route_max = Column(numeric(10, 2))
    trans_route_priority = Column(Integer, default = 1)

    def __repr__(self):
       return self.trans_route_name

 ### 

class PaymentCard(Model):
    __tablename__ = "payment_card"

    __doc__ = "We want to store as little data as possible about peoples cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bin = Column(String)
    pan = Column(String)
    credit_card_expired = Column(Boolean)
    card_token = Column(String)
    issue_number = Column(String)
    bill_to_city = Column(String)
    masked_number = Column(String)
    name = Column(String)
    company_name = Column(String)
    card_holder_name = Column(String)
    number_last_digits = Column(String)
    payment_card_type = Column(String)
    derived_card_type_code = Column(String)
    bill_to_first_name = Column(String)
    bill_to_street = Column(String)
    expiration_year = Column(String)
    bill_to_street2 = Column(String)
    expiration_month = Column(String)
    bill_to_last_name = Column(String)
    payment_method_status = Column(String)
    card_number = Column(String, comment="Mask this number")
    cardholder_name = Column(String)
    card_expiration = Column(String)
    service_code = Column(String)
    cvv = Column(String, comment="mask or hash the cvv")

    def __repr__(self):
       return self.name

 ### 

class Coupon(Model):
    __tablename__ = "coupon"

    __doc__ = " A coupon can be shared electronically and redeemed at any agent"
    coupon_id = Column(Integer, primary_key=True, autoincrement=True)
    coupon_value = Column(numeric(10, 2))
    active = Column(Boolean)
    used = Column(Boolean, default = False)
    used_date = Column(DateTime, server_default=text('NOW())')
    primary_scan_code_label = Column(String)
    is_return_coupon = Column(Boolean)
    expiration_date = Column(Date)
    generation_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    activation_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    secondary_scan_code_label = Column(String)
    scan_code_img = Column(String)
    coupon_code = Column(String)
    return_coupon_reason = Column(String)
    is_valid = Column(Boolean, default = True)
    coupon_status = Column(String)
    discount_percentage = Column(Integer)
    coupon_count = Column(Integer)
    payment_method_status = Column(String)

    def __repr__(self):
       return self.coupon_id

 ### 

class Wallet(Model):
    __tablename__ = "wallet"

    __doc__ = " Each Pos has an individual wallet"
    wallet_id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    pos_id_fk = Column(Integer, ForeignKey('pos.pos_id'))
    wallet_name = Column(String)
    wallet_balance = Column(numeric(10, 3))
    wallet_locked = Column(Boolean, default = False)
    wallet_active = Column(Boolean, default = True)
    wallet_code = Column(String)
    wallet_crypt = Column(Text)
    wallet_narrative = Column(Text)
    wallet_agent = relationship(Agent, backref='wallets_wallet_agent', primaryjoin='Wallet.agent_id_fk == Agent.agent_id')
    wallet_pos = relationship(Pos, backref='wallets_wallet_pos', primaryjoin='Wallet.pos_id_fk == Pos.pos_id')

    def __repr__(self):
       return self.wallet_name

 ### 

class Trans(Model):
    __tablename__ = "trans"

    trans_id = Column(Integer, primary_key=True, autoincrement=True)
    coupon_id_fk = Column(Integer, ForeignKey('coupon.coupon_id'))
    customer_name = Column(String)
    trans_purpose = Column(Text)
    customer_id = Column(String)
    transaction_type = Column(Enum(Transaction_type), name='t_transaction_type', nullable=False)
    card_trans_type = Column(Enum(Card_trans_type), name='t_card_trans_type', nullable=False)
    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    payment_card_id_fk = Column(Integer, ForeignKey('payment_card.id'))
    pos_id_fk = Column(Integer, ForeignKey('pos.pos_id'))
    wallet_id_fk = Column(Integer, ForeignKey('wallet.wallet_id'))
    biller_id_fk = Column(Integer, ForeignKey('biller.biller_id'))
    biller_offering_id_fk = Column(Integer, ForeignKey('biller_offering.biller_offering_id'))
    trans_time = Column(DateTime, server_default=text('NOW())', default = func.now())
    trans_status = Column(Enum(Trans_status), name='t_trans_status', nullable=False)
    trans_route_id_fk = Column(Integer, ForeignKey('trans_routing_thresholds.trans_route_id'))
    origin_source = Column(Enum(Origin_source), name='t_origin_source', nullable=False)
    origin_ref_code = Column(String)
    origin_trans_notes = Column(Text)
    origin_bank_id_fk = Column(Integer, ForeignKey('bank.bank_id'))
    origin_institution_code = Column(String)
    origin_account_num = Column(String)
    origin_account_name = Column(String)
    origin_KYC_Level = Column(Integer)
    origin_Bank_Verification_Number = Column(String)
    origin_bvn = Column(String, comment="used for check balance")
    session_ref = Column(String)
    transaction_ref = Column(String)
    channelCode = Column(Integer)
    name_enquiry_ref = Column(String)
    api_transactionid = Column(String)
    receipt_no = Column(String)
    pin_based = Column(Boolean, default = False)
    pin_code = Column(String)
    pin_option = Column(String)
    authorization_code = Column(String)
    acquirer_name = Column(String)
    currency = Column(String)
    transaction_location = Column(String)
    payment_reference = Column(String)
    response_code = Column(String)
    trans_dest = Column(Enum(Trans_dest), name='t_trans_dest', nullable=False)
    bene_ref_code = Column(String)
    bene_trans_notes = Column(Text)
    bene_bank_id_fk = Column(Integer, ForeignKey('bank.bank_id'))
    bene_account_num = Column(String)
    bene_institution_code = Column(String)
    bene_bank_verification_number = Column(String)
    bene_KYC_Level = Column(Integer)
    bene_account_name = Column(String)
    bene_phone_number = Column(String)
    bene_phone_denom = Column(String)
    bene_phone_product = Column(String)
    transaction_amount = Column(numeric(10, 2), comment="topup_amount or bank transfer amount")
    available_balance = Column(numeric(10, 2))
    svc_fees = Column(numeric(10, 2), default = 0, comment="service fees")
    comm_total = Column(numeric(10, 2))
    comm_agent = Column(numeric(10, 2))
    comm_aggr = Column(numeric(10, 2))
    comm_ours = Column(numeric(10, 2))
    comm_other = Column(numeric(10, 2), default = 0, comment="payments to others")
    comm_net_pct = Column(Numeric)
    tax = Column(numeric(10, 2))
    excise_duty = Column(numeric(10, 2))
    vat = Column(numeric(10, 2))
    transmit_amount = Column(numeric(10, 2))
    comm_narration = Column(Text, comment="how the commision was calculated")
    trans_currency = Column(String, default = 'NGN')
    trans_convert_currency = Column(String)
    trans_currency_exchange_rate = Column(numeric(10, 2), default = 1)
    trans_date = Column(DateTime, server_default=text('NOW())', default = func.now())
    customer_segment_id_fk = Column(Integer, ForeignKey('customer_segment.cs_id'))
    agent_tier_level_id_fk = Column(Integer, ForeignKey('agent_tier.tier_id'))
    special_promotions_id_fk = Column(Integer, ForeignKey('promotion.promo_id'))
    fraud_marker = Column(Boolean, default = False, comment="fraudulent transaction")
    fraud_eval_outcome = Column(String, comment="returned by as Fraud, Not Fraud, Unknown")
    fraud_risk_score = Column(Numeric, default = 0, comment="values 1-1000")
    fraud_prediction_explanations = Column(Text, comment=" list of explanations for how each event variable impacted the fraud prediction score.")
    fraud_rule_evaluations = Column(Text, comment="evaluations of the rules that were included in the detector version")
    fraud_event_num = Column(String, comment=" returned by AWS Fraud Detector")
    trans_narration = Column(Text, comment="we track and store very event that happens")
    trans_agent = relationship(Agent, backref='transs_trans_agent', primaryjoin='Trans.agent_id_fk == Agent.agent_id')
    trans_agent_tier_level = relationship(AgentTier, backref='transs_trans_agent_tier_level', primaryjoin='Trans.agent_tier_level_id_fk == AgentTier.tier_id')
    trans_bene_bank = relationship(Bank, backref='transs_trans_bene_bank', primaryjoin='Trans.bene_bank_id_fk == Bank.bank_id')
    trans_biller = relationship(Biller, backref='transs_trans_biller', primaryjoin='Trans.biller_id_fk == Biller.biller_id')
    trans_biller_offering = relationship(BillerOffering, backref='transs_trans_biller_offering', primaryjoin='Trans.biller_offering_id_fk == BillerOffering.biller_offering_id')
    trans_coupon = relationship(Coupon, backref='transs_trans_coupon', primaryjoin='Trans.coupon_id_fk == Coupon.coupon_id')
    trans_customer_segment = relationship(CustomerSegment, backref='transs_trans_customer_segment', primaryjoin='Trans.customer_segment_id_fk == CustomerSegment.cs_id')
    trans_origin_bank = relationship(Bank, backref='transs_trans_origin_bank', primaryjoin='Trans.origin_bank_id_fk == Bank.bank_id')
    trans_payment_card = relationship(PaymentCard, backref='transs_trans_payment_card', primaryjoin='Trans.payment_card_id_fk == PaymentCard.id')
    trans_pos = relationship(Pos, backref='transs_trans_pos', primaryjoin='Trans.pos_id_fk == Pos.pos_id')
    trans_special_promotions = relationship(Promotion, backref='transs_trans_special_promotions', primaryjoin='Trans.special_promotions_id_fk == Promotion.promo_id')
    trans_trans_route = relationship(TransRoutingThresholds, backref='transs_trans_trans_route', primaryjoin='Trans.trans_route_id_fk == TransRoutingThresholds.trans_route_id')
    trans_wallet = relationship(Wallet, backref='transs_trans_wallet', primaryjoin='Trans.wallet_id_fk == Wallet.wallet_id')

    def __repr__(self):
       return self.customer_name

 ### 

class AgentPerson(Model):
    __tablename__ = "agent_person"

    person_id_fk = Column(Integer, ForeignKey('person.id'))
    agent_id_fk = Column(Integer, ForeignKey('agent.agent_id'))
    agent_person_agent = relationship(Agent, backref='agent_persons_agent_person_agent', primaryjoin='AgentPerson.agent_id_fk == Agent.agent_id')
    agent_person_person = relationship(Person, backref='agent_persons_agent_person_person', primaryjoin='AgentPerson.person_id_fk == Person.id')

    def __repr__(self):
       return self.person_id_fk

 ### 

