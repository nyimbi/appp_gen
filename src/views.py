
import calendar
from flask import redirect, flash, url_for, Markup, g
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin
from flask_appbuilder import ModelView, ModelRestApi, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access
from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.widgets import ListThumbnail, ListWidget
from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction as FA
from flask_appbuilder.api import ModelRestApi
from flask import g

# If you want to enable search
# from elasticsearch import Elasticsearch

from . import appbuilder, db

from .models import *
from .view_mixins import *
from .apis import *

##########
# Various Utilities
hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on']

#To pretty Print from PersonMixin
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)


def pretty_year(value):
    return str(value.year)


# def fill_gender():
#   try:
#       db.session.add(Gender(name='Male'))
#       db.session.add(Gender(name='Female'))
#       db.session.commit()
#   except:
#       db.session.rollback()
#############

def get_user():
    return g.user


class AgentTierModelView(ModelView):
    datamodel = SQLAInterface(AgentTier)
#    list_columns = ['name', 'notes']

appbuilder.add_view(AgentTierModelView, "AgentTiers", icon="fa-folder-open-o", category="Setup")

class BankModelView(ModelView):
    datamodel = SQLAInterface(Bank)
#    list_columns = ['code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']

appbuilder.add_view(BankModelView, "Banks", icon="fa-folder-open-o", category="Setup")

class BillerCategoryModelView(ModelView):
    datamodel = SQLAInterface(BillerCategory)
#    list_columns = ['name', 'notes']

appbuilder.add_view(BillerCategoryModelView, "BillerCategorys", icon="fa-folder-open-o", category="Setup")

class ContactTypeModelView(ModelView):
    datamodel = SQLAInterface(ContactType)
#    list_columns = ['name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']

appbuilder.add_view(ContactTypeModelView, "ContactTypes", icon="fa-folder-open-o", category="Setup")

class CountryModelView(ModelView):
    datamodel = SQLAInterface(Country)
#    list_columns = ['name', 'code', 'phone_code']

appbuilder.add_view(CountryModelView, "Countrys", icon="fa-folder-open-o", category="Setup")

class CouponModelView(ModelView):
    datamodel = SQLAInterface(Coupon)
#    list_columns = ['coupon_id', 'coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']

appbuilder.add_view(CouponModelView, "Coupons", icon="fa-folder-open-o", category="Setup")

class CurrencyModelView(ModelView):
    datamodel = SQLAInterface(Currency)
#    list_columns = ['name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']

appbuilder.add_view(CurrencyModelView, "Currencys", icon="fa-folder-open-o", category="Setup")

class CustomerSegmentModelView(ModelView):
    datamodel = SQLAInterface(CustomerSegment)
#    list_columns = ['cs_id', 'cs_name', 'cs_notes']

appbuilder.add_view(CustomerSegmentModelView, "CustomerSegments", icon="fa-folder-open-o", category="Setup")

class DocTypeModelView(ModelView):
    datamodel = SQLAInterface(DocType)
#    list_columns = ['name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']

appbuilder.add_view(DocTypeModelView, "DocTypes", icon="fa-folder-open-o", category="Setup")

class MimeTypeModelView(ModelView):
    datamodel = SQLAInterface(MimeType)
#    list_columns = ['label', 'mime_type', 'file_extension']

appbuilder.add_view(MimeTypeModelView, "MimeTypes", icon="fa-folder-open-o", category="Setup")

class MimeTypeMapModelView(ModelView):
    datamodel = SQLAInterface(MimeTypeMap)
#    list_columns = ['extension', 'mime_type']

appbuilder.add_view(MimeTypeMapModelView, "MimeTypeMaps", icon="fa-folder-open-o", category="Setup")

class PaymentCardModelView(ModelView):
    datamodel = SQLAInterface(PaymentCard)
#    list_columns = ['bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']

appbuilder.add_view(PaymentCardModelView, "PaymentCards", icon="fa-folder-open-o", category="Setup")

class PromotionModelView(ModelView):
    datamodel = SQLAInterface(Promotion)
#    list_columns = ['promo_id', 'promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']

appbuilder.add_view(PromotionModelView, "Promotions", icon="fa-folder-open-o", category="Setup")

class TechparamsModelView(ModelView):
    datamodel = SQLAInterface(Techparams)
#    list_columns = ['tp_key', 'tp_value', 'enabled', 'notes']

appbuilder.add_view(TechparamsModelView, "Techparamss", icon="fa-folder-open-o", category="Setup")

class TokenProviderModelView(ModelView):
    datamodel = SQLAInterface(TokenProvider)
#    list_columns = ['token_provider_id', 'token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']

appbuilder.add_view(TokenProviderModelView, "TokenProviders", icon="fa-folder-open-o", category="Setup")

class TransRoutingThresholdsModelView(ModelView):
    datamodel = SQLAInterface(TransRoutingThresholds)
#    list_columns = ['name', 'min_amount', 'max_amount', 'priority']

appbuilder.add_view(TransRoutingThresholdsModelView, "TransRoutingThresholdss", icon="fa-folder-open-o", category="Setup")

class TransTypeModelView(ModelView):
    datamodel = SQLAInterface(TransType)
#    list_columns = ['tt_id', 'tt_name', 'tt_notes']

appbuilder.add_view(TransTypeModelView, "TransTypes", icon="fa-folder-open-o", category="Setup")

class UserExtModelView(ModelView):
    datamodel = SQLAInterface(UserExt)
#    list_columns = ['col.name[:-6]', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data']

appbuilder.add_view(UserExtModelView, "UserExts", icon="fa-folder-open-o", category="Setup")

class BillerModelView(ModelView):
    datamodel = SQLAInterface(Biller)
#    list_columns = ['col.name[:-6]', 'code', 'name', 'url', 'note']

appbuilder.add_view(BillerModelView, "Billers", icon="fa-folder-open-o", category="Setup")

class StateModelView(ModelView):
    datamodel = SQLAInterface(State)
#    list_columns = ['col.name[:-6]', 'code', 'name', 'desc']

appbuilder.add_view(StateModelView, "States", icon="fa-folder-open-o", category="Setup")

class TokenModelView(ModelView):
    datamodel = SQLAInterface(Token)
#    list_columns = ['token_id', 'col.name[:-6]', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled']

appbuilder.add_view(TokenModelView, "Tokens", icon="fa-folder-open-o", category="Setup")

class BillerOfferingModelView(ModelView):
    datamodel = SQLAInterface(BillerOffering)
#    list_columns = ['col.name[:-6]', 'offering_id', 'offering_name', 'offering_description', 'offering_price']

appbuilder.add_view(BillerOfferingModelView, "BillerOfferings", icon="fa-folder-open-o", category="Setup")

class LgaModelView(ModelView):
    datamodel = SQLAInterface(Lga)
#    list_columns = ['col.name[:-6]', 'code', 'lga_name']

appbuilder.add_view(LgaModelView, "Lgas", icon="fa-folder-open-o", category="Setup")

class AgentModelView(ModelView):
    datamodel = SQLAInterface(Agent)
#    list_columns = ['col.name[:-6]', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'col.name[:-6]', 'col.name[:-6]', 'agent_name', 'alias', 'col.name[:-6]', 'phone', 'phone_ext', 'col.name[:-6]', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'tax_id', 'col.name[:-6]', 'bank_acc_no', 'biz_name', 'col.name[:-6]', 'col.name[:-6]', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history']

appbuilder.add_view(AgentModelView, "Agents", icon="fa-folder-open-o", category="Setup")

class PosModelView(ModelView):
    datamodel = SQLAInterface(Pos)
#    list_columns = ['serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'state_id', 'lga_id', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key']

appbuilder.add_view(PosModelView, "Poss", icon="fa-folder-open-o", category="Setup")

class AgentPosLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentPosLink)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history']

appbuilder.add_view(AgentPosLinkModelView, "AgentPosLinks", icon="fa-folder-open-o", category="Setup")

class CommRefModelView(ModelView):
    datamodel = SQLAInterface(CommRef)
#    list_columns = ['cr_id', 'agent_type', 'agent_tier_level', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date']

appbuilder.add_view(CommRefModelView, "CommRefs", icon="fa-folder-open-o", category="Setup")

class PersonModelView(ModelView):
    datamodel = SQLAInterface(Person)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'tax_id', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code']

appbuilder.add_view(PersonModelView, "People", icon="fa-folder-open-o", category="Setup")

class WalletModelView(ModelView):
    datamodel = SQLAInterface(Wallet)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative']

appbuilder.add_view(WalletModelView, "Wallets", icon="fa-folder-open-o", category="Setup")

class AgentPersonLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentPersonLink)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]']

appbuilder.add_view(AgentPersonLinkModelView, "AgentPersonLinks", icon="fa-folder-open-o", category="Setup")

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes']

appbuilder.add_view(ContactModelView, "Contacts", icon="fa-folder-open-o", category="Setup")

class DocModelView(ModelView):
    datamodel = SQLAInterface(Doc)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on']

appbuilder.add_view(DocModelView, "Docs", icon="fa-folder-open-o", category="Setup")

class PersonAdditionalDataModelView(ModelView):
    datamodel = SQLAInterface(PersonAdditionalData)
#    list_columns = ['col.name[:-6]', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on']

appbuilder.add_view(PersonAdditionalDataModelView, "PersonAdditionalDatas", icon="fa-folder-open-o", category="Setup")

class PersonAdminDataModelView(ModelView):
    datamodel = SQLAInterface(PersonAdminData)
#    list_columns = ['col.name[:-6]', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating']

appbuilder.add_view(PersonAdminDataModelView, "PersonAdminDatas", icon="fa-folder-open-o", category="Setup")

class TransModelView(ModelView):
    datamodel = SQLAInterface(Trans)
#    list_columns = ['col.name[:-6]', 'customer_name', 'trans_purpose', 'customer_id', 'transaction_type', 'card_trans_type', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'trans_time', 'col.name[:-6]', 'trans_status', 'col.name[:-6]', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'col.name[:-6]', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'col.name[:-6]', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'col.name[:-6]', 'col.name[:-6]', 'col.name[:-6]', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration']

appbuilder.add_view(TransModelView, "Transs", icon="fa-folder-open-o", category="Setup")

class AgentDocLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentDocLink)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'verification_status', 'submit_date', 'notes']

appbuilder.add_view(AgentDocLinkModelView, "AgentDocLinks", icon="fa-folder-open-o", category="Setup")

class PersonDocLinkModelView(ModelView):
    datamodel = SQLAInterface(PersonDocLink)
#    list_columns = ['col.name[:-6]', 'col.name[:-6]', 'verification_status', 'submit_date']

appbuilder.add_view(PersonDocLinkModelView, "PersonDocLinks", icon="fa-folder-open-o", category="Setup")

class UserExt_UserExtMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [UserExtModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(UserExt_UserExtMasterDetailView, "UserExts", icon="fa-folder-open-o", category="Review")

class BillerCategory_BillerMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(BillerCategory)
    related_views = [BillerModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(BillerCategory_BillerMasterDetailView, "BillerCategorys", icon="fa-folder-open-o", category="Review")

class Country_StateMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [StateModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Country_StateMasterDetailView, "Countrys", icon="fa-folder-open-o", category="Review")

class TokenProvider_TokenMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(TokenProvider)
    related_views = [TokenModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(TokenProvider_TokenMasterDetailView, "TokenProviders", icon="fa-folder-open-o", category="Review")

class Biller_BillerOfferingMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [BillerOfferingModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Biller_BillerOfferingMasterDetailView, "Billers", icon="fa-folder-open-o", category="Review")

class State_LgaMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [LgaModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(State_LgaMasterDetailView, "States", icon="fa-folder-open-o", category="Review")

class UserExt_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(UserExt_AgentMasterDetailView, "UserExts", icon="fa-folder-open-o", category="Review")

class Lga_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Lga_AgentMasterDetailView, "Lgas", icon="fa-folder-open-o", category="Review")

class State_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(State_AgentMasterDetailView, "States", icon="fa-folder-open-o", category="Review")

class Country_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Country_AgentMasterDetailView, "Countrys", icon="fa-folder-open-o", category="Review")

class Bank_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Bank)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Bank_AgentMasterDetailView, "Banks", icon="fa-folder-open-o", category="Review")

class AgentTier_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(AgentTier_AgentMasterDetailView, "AgentTiers", icon="fa-folder-open-o", category="Review")

class Agent_AgentMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_AgentMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class UserExt_PosMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [PosModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(UserExt_PosMasterDetailView, "UserExts", icon="fa-folder-open-o", category="Review")

class State_PosMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [PosModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(State_PosMasterDetailView, "States", icon="fa-folder-open-o", category="Review")

class Lga_PosMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [PosModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Lga_PosMasterDetailView, "Lgas", icon="fa-folder-open-o", category="Review")

class Pos_AgentPosLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [AgentPosLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Pos_AgentPosLinkMasterDetailView, "Poss", icon="fa-folder-open-o", category="Review")

class Agent_AgentPosLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentPosLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_AgentPosLinkMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class CustomerSegment_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(CustomerSegment)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(CustomerSegment_CommRefMasterDetailView, "CustomerSegments", icon="fa-folder-open-o", category="Review")

class Agent_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_CommRefMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class BillerOffering_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(BillerOffering)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(BillerOffering_CommRefMasterDetailView, "BillerOfferings", icon="fa-folder-open-o", category="Review")

class Lga_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Lga_CommRefMasterDetailView, "Lgas", icon="fa-folder-open-o", category="Review")

class Biller_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Biller_CommRefMasterDetailView, "Billers", icon="fa-folder-open-o", category="Review")

class AgentTier_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(AgentTier_CommRefMasterDetailView, "AgentTiers", icon="fa-folder-open-o", category="Review")

class State_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(State_CommRefMasterDetailView, "States", icon="fa-folder-open-o", category="Review")

class TransType_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(TransType)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(TransType_CommRefMasterDetailView, "TransTypes", icon="fa-folder-open-o", category="Review")

class Promotion_CommRefMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Promotion)
    related_views = [CommRefModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Promotion_CommRefMasterDetailView, "Promotions", icon="fa-folder-open-o", category="Review")

class Person_PersonMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_PersonMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class Agent_PersonMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [PersonModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_PersonMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class Pos_WalletMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [WalletModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Pos_WalletMasterDetailView, "Poss", icon="fa-folder-open-o", category="Review")

class Agent_WalletMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [WalletModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_WalletMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class Agent_AgentPersonLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentPersonLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_AgentPersonLinkMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class Person_AgentPersonLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [AgentPersonLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_AgentPersonLinkMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class ContactType_ContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(ContactType)
    related_views = [ContactModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(ContactType_ContactMasterDetailView, "ContactTypes", icon="fa-folder-open-o", category="Review")

class Person_ContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ContactModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_ContactMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class Agent_ContactMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [ContactModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_ContactMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class DocType_DocMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(DocType)
    related_views = [DocModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(DocType_DocMasterDetailView, "DocTypes", icon="fa-folder-open-o", category="Review")

class Person_DocMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [DocModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_DocMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class Agent_DocMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [DocModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_DocMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class MimeType_DocMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(MimeType)
    related_views = [DocModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(MimeType_DocMasterDetailView, "MimeTypes", icon="fa-folder-open-o", category="Review")

class Person_PersonAdditionalDataMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonAdditionalDataModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_PersonAdditionalDataMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class Country_PersonAdditionalDataMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [PersonAdditionalDataModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Country_PersonAdditionalDataMasterDetailView, "Countrys", icon="fa-folder-open-o", category="Review")

class Person_PersonAdminDataMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonAdminDataModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_PersonAdminDataMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class Promotion_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Promotion)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Promotion_TransMasterDetailView, "Promotions", icon="fa-folder-open-o", category="Review")

class Agent_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_TransMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class Coupon_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Coupon)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Coupon_TransMasterDetailView, "Coupons", icon="fa-folder-open-o", category="Review")

class PaymentCard_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(PaymentCard)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(PaymentCard_TransMasterDetailView, "PaymentCards", icon="fa-folder-open-o", category="Review")

class BillerOffering_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(BillerOffering)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(BillerOffering_TransMasterDetailView, "BillerOfferings", icon="fa-folder-open-o", category="Review")

class Currency_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Currency)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Currency_TransMasterDetailView, "Currencys", icon="fa-folder-open-o", category="Review")

class Pos_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Pos_TransMasterDetailView, "Poss", icon="fa-folder-open-o", category="Review")

class Biller_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Biller_TransMasterDetailView, "Billers", icon="fa-folder-open-o", category="Review")

class CustomerSegment_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(CustomerSegment)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(CustomerSegment_TransMasterDetailView, "CustomerSegments", icon="fa-folder-open-o", category="Review")

class Bank_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Bank)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Bank_TransMasterDetailView, "Banks", icon="fa-folder-open-o", category="Review")

class AgentTier_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(AgentTier_TransMasterDetailView, "AgentTiers", icon="fa-folder-open-o", category="Review")

class Wallet_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Wallet)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Wallet_TransMasterDetailView, "Wallets", icon="fa-folder-open-o", category="Review")

class TransRoutingThresholds_TransMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(TransRoutingThresholds)
    related_views = [TransModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(TransRoutingThresholds_TransMasterDetailView, "TransRoutingThresholdss", icon="fa-folder-open-o", category="Review")

class Agent_AgentDocLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentDocLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Agent_AgentDocLinkMasterDetailView, "Agents", icon="fa-folder-open-o", category="Review")

class Doc_AgentDocLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Doc)
    related_views = [AgentDocLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Doc_AgentDocLinkMasterDetailView, "Docs", icon="fa-folder-open-o", category="Review")

class Doc_PersonDocLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Doc)
    related_views = [PersonDocLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Doc_PersonDocLinkMasterDetailView, "Docs", icon="fa-folder-open-o", category="Review")

class Person_PersonDocLinkMasterDetailView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonDocLinkModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'

appbuilder.add_view(Person_PersonDocLinkMasterDetailView, "People", icon="fa-folder-open-o", category="Review")

class AgentMultipleView(MultipleView):
    datamodel = SQLAInterface(Agent)
    views = [BankModelView, AgentModelView, AgentTierModelView, LgaModelView, StateModelView, CountryModelView, UserExtModelView]

appbuilder.add_view(AgentMultipleView, "Agents", icon="fa-folder-open-o", category="Inspect")

class LgaMultipleView(MultipleView):
    datamodel = SQLAInterface(Lga)
    views = [StateModelView, LgaModelView, UserExtModelView]

appbuilder.add_view(LgaMultipleView, "Lgas", icon="fa-folder-open-o", category="Inspect")

class PromotionMultipleView(MultipleView):
    datamodel = SQLAInterface(Promotion)
    views = [StateModelView, AgentModelView, BillerOfferingModelView, CustomerSegmentModelView, PromotionModelView, LgaModelView, BillerModelView, AgentTierModelView, TransTypeModelView]

appbuilder.add_view(PromotionMultipleView, "Promotions", icon="fa-folder-open-o", category="Inspect")

class PersonMultipleView(MultipleView):
    datamodel = SQLAInterface(Person)
    views = [AgentModelView, PersonModelView]

appbuilder.add_view(PersonMultipleView, "People", icon="fa-folder-open-o", category="Inspect")

class MimeTypeMultipleView(MultipleView):
    datamodel = SQLAInterface(MimeType)
    views = [DocTypeModelView, AgentModelView, PersonModelView, MimeTypeModelView]

appbuilder.add_view(MimeTypeMultipleView, "MimeTypes", icon="fa-folder-open-o", category="Inspect")

class CountryMultipleView(MultipleView):
    datamodel = SQLAInterface(Country)
    views = [CountryModelView, PersonModelView]

appbuilder.add_view(CountryMultipleView, "Countrys", icon="fa-folder-open-o", category="Inspect")

class TransRoutingThresholdsMultipleView(MultipleView):
    datamodel = SQLAInterface(TransRoutingThresholds)
    views = [BankModelView, AgentModelView, PaymentCardModelView, BillerOfferingModelView, CouponModelView, PromotionModelView, PosModelView, CustomerSegmentModelView, TransRoutingThresholdsModelView, CurrencyModelView, BillerModelView, AgentTierModelView, WalletModelView]

appbuilder.add_view(TransRoutingThresholdsMultipleView, "TransRoutingThresholdss", icon="fa-folder-open-o", category="Inspect")

class DocMultipleView(MultipleView):
    datamodel = SQLAInterface(Doc)
    views = [AgentModelView, DocModelView]

appbuilder.add_view(DocMultipleView, "Docs", icon="fa-folder-open-o", category="Inspect")


appbuilder.add_link("rest_api", href="/swagger/v1", icon="fa-sliders", label="REST Api", category="Utilities")
appbuilder.add_link("graphql", href="/graphql", icon="fa-wrench", label="GraphQL", category="Utilities")

#appbuilder.add_separator("Setup")
#appbuilder.add_separator("My Views")
#appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)

'''
     Application wide 404 error handler
'''

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
           "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
     )


db.create_all()
