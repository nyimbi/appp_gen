
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
from flask import g

# If you want to enable search
# from elasticsearch import Elasticsearch

from . import appbuilder, db

from .models import *
from .view_mixins import *

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



class AgentTierApi(ModelRestApi):
    datamodel = SQLAInterface(AgentTier)

appbuilder.add_api(AgentTierApi)

class AgentTierModelView(ModelView):
    datamodel = SQLAInterface(AgentTier)

    add_title = 'Add AgentTier'
    # add_columns = ['id', 'name', 'notes']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'AgentTier List'
    # list_columns = ['id', 'name', 'notes']
    # list_exclude_columns = [] # ['id', 'name', 'notes'] #

    edit_title = 'Edit AgentTier'
    # edit_columns = ['id', 'name', 'notes']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'notes']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'notes']
    # search_exclude_columns = [] # ['id', 'name', 'notes']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'notes': 'Notes'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'notes']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(AgentTierModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(AgentTierModelView, "Agent Tier", icon="fa-folder-open-o", category="Setup")


class BankApi(ModelRestApi):
    datamodel = SQLAInterface(Bank)

appbuilder.add_api(BankApi)

class BankModelView(ModelView):
    datamodel = SQLAInterface(Bank)

    add_title = 'Add Bank'
    # add_columns = ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Bank List'
    # list_columns = ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # list_exclude_columns = [] # ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on'] #

    edit_title = 'Edit Bank'
    # edit_columns = ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # search_exclude_columns = [] # ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'code': 'Code', 'name': 'Name', 'category': 'Category', 'swift_code': 'Swift Code', 'sort_code': 'Sort Code', 'iban': 'Iban', 'cust_care_phone': 'Cust Care Phone', 'cust_care_email': 'Cust Care Email', 'escalation_contact': 'Escalation Contact', 'created_on': 'Created On', 'updated_on': 'Updated On'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'code', 'name', 'category', 'swift_code', 'sort_code', 'iban', 'cust_care_phone', 'cust_care_email', 'escalation_contact', 'created_on', 'updated_on']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(BankModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(BankModelView, "Bank", icon="fa-folder-open-o", category="Setup")


class BillerCategoryApi(ModelRestApi):
    datamodel = SQLAInterface(BillerCategory)

appbuilder.add_api(BillerCategoryApi)

class BillerCategoryModelView(ModelView):
    datamodel = SQLAInterface(BillerCategory)

    add_title = 'Add BillerCategory'
    # add_columns = ['id', 'name', 'notes']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'BillerCategory List'
    # list_columns = ['id', 'name', 'notes']
    # list_exclude_columns = [] # ['id', 'name', 'notes'] #

    edit_title = 'Edit BillerCategory'
    # edit_columns = ['id', 'name', 'notes']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'notes']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'notes']
    # search_exclude_columns = [] # ['id', 'name', 'notes']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'notes': 'Notes'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'notes']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(BillerCategoryModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(BillerCategoryModelView, "Biller Category", icon="fa-folder-open-o", category="Setup")


class ContactTypeApi(ModelRestApi):
    datamodel = SQLAInterface(ContactType)

appbuilder.add_api(ContactTypeApi)

class ContactTypeModelView(ModelView):
    datamodel = SQLAInterface(ContactType)

    add_title = 'Add ContactType'
    # add_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'ContactType List'
    # list_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # list_exclude_columns = [] # ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at'] #

    edit_title = 'Edit ContactType'
    # edit_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # search_exclude_columns = [] # ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'description': 'Description', 'is_digital': 'Is Digital', 'requires_verification': 'Requires Verification', 'max_length': 'Max Length', 'icon_url': 'Icon Url', 'created_at': 'Created At', 'updated_at': 'Updated At'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'description', 'is_digital', 'requires_verification', 'max_length', 'icon_url', 'created_at', 'updated_at']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(ContactTypeModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(ContactTypeModelView, "Contact Type", icon="fa-folder-open-o", category="Setup")


class CountryApi(ModelRestApi):
    datamodel = SQLAInterface(Country)

appbuilder.add_api(CountryApi)

class CountryModelView(ModelView):
    datamodel = SQLAInterface(Country)

    add_title = 'Add Country'
    # add_columns = ['id', 'name', 'code', 'phone_code']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Country List'
    # list_columns = ['id', 'name', 'code', 'phone_code']
    # list_exclude_columns = [] # ['id', 'name', 'code', 'phone_code'] #

    edit_title = 'Edit Country'
    # edit_columns = ['id', 'name', 'code', 'phone_code']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'code', 'phone_code']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'code', 'phone_code']
    # search_exclude_columns = [] # ['id', 'name', 'code', 'phone_code']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'code': 'Code', 'phone_code': 'Phone Code'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'code', 'phone_code']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(CountryModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(CountryModelView, "Country", icon="fa-folder-open-o", category="Setup")


class CouponApi(ModelRestApi):
    datamodel = SQLAInterface(Coupon)

appbuilder.add_api(CouponApi)

class CouponModelView(ModelView):
    datamodel = SQLAInterface(Coupon)

    add_title = 'Add Coupon'
    # add_columns = ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Coupon List'
    # list_columns = ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # list_exclude_columns = [] # ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status'] #

    edit_title = 'Edit Coupon'
    # edit_columns = ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # search_exclude_columns = [] # ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'coupon_id': 'Coupon Id', 'coupon_value': 'Coupon Value', 'active': 'Active', 'used': 'Used', 'used_date': 'Used Date', 'primary_scan_code_label': 'Primary Scan Code Label', 'is_return_coupon': 'Is Return Coupon', 'expiration_date': 'Expiration Date', 'generation_date': 'Generation Date', 'activation_date': 'Activation Date', 'secondary_scan_code_label': 'Secondary Scan Code Label', 'scan_code_img': 'Scan Code Img', 'coupon_code': 'Coupon Code', 'return_coupon_reason': 'Return Coupon Reason', 'is_valid': 'Is Valid', 'coupon_status': 'Coupon Status', 'discount_percentage': 'Discount Percentage', 'coupon_count': 'Coupon Count', 'payment_method_status': 'Payment Method Status'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['coupon_value', 'active', 'used', 'used_date', 'primary_scan_code_label', 'is_return_coupon', 'expiration_date', 'generation_date', 'activation_date', 'secondary_scan_code_label', 'scan_code_img', 'coupon_code', 'return_coupon_reason', 'is_valid', 'coupon_status', 'discount_percentage', 'coupon_count', 'payment_method_status']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(CouponModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(CouponModelView, "Coupon", icon="fa-folder-open-o", category="Setup")


class CurrencyApi(ModelRestApi):
    datamodel = SQLAInterface(Currency)

appbuilder.add_api(CurrencyApi)

class CurrencyModelView(ModelView):
    datamodel = SQLAInterface(Currency)

    add_title = 'Add Currency'
    # add_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Currency List'
    # list_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # list_exclude_columns = [] # ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code'] #

    edit_title = 'Edit Currency'
    # edit_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # search_exclude_columns = [] # ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'symbol': 'Symbol', 'numeric_code': 'Numeric Code', 'full_name': 'Full Name', 'decimal_places': 'Decimal Places', 'internationalized_name_code': 'Internationalized Name Code'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'symbol', 'numeric_code', 'full_name', 'decimal_places', 'internationalized_name_code']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(CurrencyModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(CurrencyModelView, "Currency", icon="fa-folder-open-o", category="Setup")


class CustomerSegmentApi(ModelRestApi):
    datamodel = SQLAInterface(CustomerSegment)

appbuilder.add_api(CustomerSegmentApi)

class CustomerSegmentModelView(ModelView):
    datamodel = SQLAInterface(CustomerSegment)

    add_title = 'Add CustomerSegment'
    # add_columns = ['cs_name', 'cs_notes']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'CustomerSegment List'
    # list_columns = ['cs_name', 'cs_notes']
    # list_exclude_columns = [] # ['cs_name', 'cs_notes'] #

    edit_title = 'Edit CustomerSegment'
    # edit_columns = ['cs_name', 'cs_notes']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['cs_name', 'cs_notes']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['cs_name', 'cs_notes']
    # search_exclude_columns = [] # ['cs_name', 'cs_notes']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'cs_id': 'Cs Id', 'cs_name': 'Cs Name', 'cs_notes': 'Cs Notes'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['cs_name', 'cs_notes']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(CustomerSegmentModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(CustomerSegmentModelView, "Customer Segment", icon="fa-folder-open-o", category="Setup")


class DocTypeApi(ModelRestApi):
    datamodel = SQLAInterface(DocType)

appbuilder.add_api(DocTypeApi)

class DocTypeModelView(ModelView):
    datamodel = SQLAInterface(DocType)

    add_title = 'Add DocType'
    # add_columns = ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'DocType List'
    # list_columns = ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # list_exclude_columns = [] # ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at'] #

    edit_title = 'Edit DocType'
    # edit_columns = ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # search_exclude_columns = [] # ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'doc_category': 'Doc Category', 'notes': 'Notes', 'required_information': 'Required Information', 'is_serialized': 'Is Serialized', 'serial_length': 'Serial Length', 'expires': 'Expires', 'validity_period': 'Validity Period', 'renewal_frequency': 'Renewal Frequency', 'is_government_issued': 'Is Government Issued', 'is_digital': 'Is Digital', 'template_url': 'Template Url', 'example_image_url': 'Example Image Url', 'created_at': 'Created At', 'updated_at': 'Updated At'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'doc_category', 'notes', 'required_information', 'is_serialized', 'serial_length', 'expires', 'validity_period', 'renewal_frequency', 'is_government_issued', 'is_digital', 'template_url', 'example_image_url', 'created_at', 'updated_at']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(DocTypeModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(DocTypeModelView, "Doc Type", icon="fa-folder-open-o", category="Setup")


class MimeTypeApi(ModelRestApi):
    datamodel = SQLAInterface(MimeType)

appbuilder.add_api(MimeTypeApi)

class MimeTypeModelView(ModelView):
    datamodel = SQLAInterface(MimeType)

    add_title = 'Add MimeType'
    # add_columns = ['id', 'label', 'mime_type', 'file_extension']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'MimeType List'
    # list_columns = ['id', 'label', 'mime_type', 'file_extension']
    # list_exclude_columns = [] # ['id', 'label', 'mime_type', 'file_extension'] #

    edit_title = 'Edit MimeType'
    # edit_columns = ['id', 'label', 'mime_type', 'file_extension']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'label', 'mime_type', 'file_extension']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'label', 'mime_type', 'file_extension']
    # search_exclude_columns = [] # ['id', 'label', 'mime_type', 'file_extension']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'label': 'Label', 'mime_type': 'Mime Type', 'file_extension': 'File Extension'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'label', 'mime_type', 'file_extension']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(MimeTypeModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(MimeTypeModelView, "Mime Type", icon="fa-folder-open-o", category="Setup")


class MimeTypeMapApi(ModelRestApi):
    datamodel = SQLAInterface(MimeTypeMap)

appbuilder.add_api(MimeTypeMapApi)

class MimeTypeMapModelView(ModelView):
    datamodel = SQLAInterface(MimeTypeMap)

    add_title = 'Add MimeTypeMap'
    # add_columns = ['id', 'extension', 'mime_type']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'MimeTypeMap List'
    # list_columns = ['id', 'extension', 'mime_type']
    # list_exclude_columns = [] # ['id', 'extension', 'mime_type'] #

    edit_title = 'Edit MimeTypeMap'
    # edit_columns = ['id', 'extension', 'mime_type']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'extension', 'mime_type']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'extension', 'mime_type']
    # search_exclude_columns = [] # ['id', 'extension', 'mime_type']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'extension': 'Extension', 'mime_type': 'Mime Type'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'extension', 'mime_type']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(MimeTypeMapModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(MimeTypeMapModelView, "Mime Type Map", icon="fa-folder-open-o", category="Setup")


class PaymentCardApi(ModelRestApi):
    datamodel = SQLAInterface(PaymentCard)

appbuilder.add_api(PaymentCardApi)

class PaymentCardModelView(ModelView):
    datamodel = SQLAInterface(PaymentCard)

    add_title = 'Add PaymentCard'
    # add_columns = ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'PaymentCard List'
    # list_columns = ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # list_exclude_columns = [] # ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv'] #

    edit_title = 'Edit PaymentCard'
    # edit_columns = ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # search_exclude_columns = [] # ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'bin': 'Bin', 'pan': 'Pan', 'credit_card_expired': 'Credit Card Expired', 'card_token': 'Card Token', 'issue_number': 'Issue Number', 'bill_to_city': 'Bill To City', 'masked_number': 'Masked Number', 'name': 'Name', 'company_name': 'Company Name', 'card_holder_name': 'Card Holder Name', 'number_last_digits': 'Number Last Digits', 'payment_card_type': 'Payment Card Type', 'derived_card_type_code': 'Derived Card Type Code', 'expiration_year': 'Expiration Year', 'expiration_month': 'Expiration Month', 'bill_to_street': 'Bill To Street', 'bill_to_street2': 'Bill To Street2', 'bill_to_first_name': 'Bill To First Name', 'bill_to_last_name': 'Bill To Last Name', 'payment_method_status': 'Payment Method Status', 'card_number': 'Card Number', 'cardholder_name': 'Cardholder Name', 'card_expiration': 'Card Expiration', 'service_code': 'Service Code', 'cvv': 'Cvv'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'bin', 'pan', 'credit_card_expired', 'card_token', 'issue_number', 'bill_to_city', 'masked_number', 'name', 'company_name', 'card_holder_name', 'number_last_digits', 'payment_card_type', 'derived_card_type_code', 'expiration_year', 'expiration_month', 'bill_to_street', 'bill_to_street2', 'bill_to_first_name', 'bill_to_last_name', 'payment_method_status', 'card_number', 'cardholder_name', 'card_expiration', 'service_code', 'cvv']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PaymentCardModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PaymentCardModelView, "Payment Card", icon="fa-folder-open-o", category="Setup")


class PromotionApi(ModelRestApi):
    datamodel = SQLAInterface(Promotion)

appbuilder.add_api(PromotionApi)

class PromotionModelView(ModelView):
    datamodel = SQLAInterface(Promotion)

    add_title = 'Add Promotion'
    # add_columns = ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Promotion List'
    # list_columns = ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # list_exclude_columns = [] # ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date'] #

    edit_title = 'Edit Promotion'
    # edit_columns = ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # search_exclude_columns = [] # ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'promo_id': 'Promo Id', 'promo_name': 'Promo Name', 'promo_notes': 'Promo Notes', 'promo_start_date': 'Promo Start Date', 'promo_end_date': 'Promo End Date'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['promo_name', 'promo_notes', 'promo_start_date', 'promo_end_date']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PromotionModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PromotionModelView, "Promotion", icon="fa-folder-open-o", category="Setup")


class TechparamsApi(ModelRestApi):
    datamodel = SQLAInterface(Techparams)

appbuilder.add_api(TechparamsApi)

class TechparamsModelView(ModelView):
    datamodel = SQLAInterface(Techparams)

    add_title = 'Add Techparams'
    # add_columns = ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Techparams List'
    # list_columns = ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # list_exclude_columns = [] # ['id', 'tp_key', 'tp_value', 'enabled', 'notes'] #

    edit_title = 'Edit Techparams'
    # edit_columns = ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # search_exclude_columns = [] # ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'tp_key': 'Tp Key', 'tp_value': 'Tp Value', 'enabled': 'Enabled', 'notes': 'Notes'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'tp_key', 'tp_value', 'enabled', 'notes']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TechparamsModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TechparamsModelView, "Techparams", icon="fa-folder-open-o", category="Setup")


class TokenProviderApi(ModelRestApi):
    datamodel = SQLAInterface(TokenProvider)

appbuilder.add_api(TokenProviderApi)

class TokenProviderModelView(ModelView):
    datamodel = SQLAInterface(TokenProvider)

    add_title = 'Add TokenProvider'
    # add_columns = ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'TokenProvider List'
    # list_columns = ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # list_exclude_columns = [] # ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled'] #

    edit_title = 'Edit TokenProvider'
    # edit_columns = ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # search_exclude_columns = [] # ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'token_provider_id': 'Token Provider Id', 'token_provider_name': 'Token Provider Name', 'token_provioder_notes': 'Token Provioder Notes', 'token_provider_priv_key': 'Token Provider Priv Key', 'token_provider_pub_key': 'Token Provider Pub Key', 'token_provider_endpoint': 'Token Provider Endpoint', 'token_provider_protocol': 'Token Provider Protocol', 'token_provider_auth': 'Token Provider Auth', 'token_provider_ssl': 'Token Provider Ssl', 'token_provider_ip_whitelist': 'Token Provider Ip Whitelist', 'token_provider_password': 'Token Provider Password', 'enabled': 'Enabled'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['token_provider_name', 'token_provioder_notes', 'token_provider_priv_key', 'token_provider_pub_key', 'token_provider_endpoint', 'token_provider_protocol', 'token_provider_auth', 'token_provider_ssl', 'token_provider_ip_whitelist', 'token_provider_password', 'enabled']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TokenProviderModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TokenProviderModelView, "Token Provider", icon="fa-folder-open-o", category="Setup")


class TransRoutingThresholdsApi(ModelRestApi):
    datamodel = SQLAInterface(TransRoutingThresholds)

appbuilder.add_api(TransRoutingThresholdsApi)

class TransRoutingThresholdsModelView(ModelView):
    datamodel = SQLAInterface(TransRoutingThresholds)

    add_title = 'Add TransRoutingThresholds'
    # add_columns = ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'TransRoutingThresholds List'
    # list_columns = ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # list_exclude_columns = [] # ['id', 'name', 'min_amount', 'max_amount', 'priority'] #

    edit_title = 'Edit TransRoutingThresholds'
    # edit_columns = ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # search_exclude_columns = [] # ['id', 'name', 'min_amount', 'max_amount', 'priority']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'name': 'Name', 'min_amount': 'Min Amount', 'max_amount': 'Max Amount', 'priority': 'Priority'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'name', 'min_amount', 'max_amount', 'priority']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TransRoutingThresholdsModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TransRoutingThresholdsModelView, "Trans Routing Thresholds", icon="fa-folder-open-o", category="Setup")


class TransTypeApi(ModelRestApi):
    datamodel = SQLAInterface(TransType)

appbuilder.add_api(TransTypeApi)

class TransTypeModelView(ModelView):
    datamodel = SQLAInterface(TransType)

    add_title = 'Add TransType'
    # add_columns = ['tt_name', 'tt_notes']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'TransType List'
    # list_columns = ['tt_name', 'tt_notes']
    # list_exclude_columns = [] # ['tt_name', 'tt_notes'] #

    edit_title = 'Edit TransType'
    # edit_columns = ['tt_name', 'tt_notes']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['tt_name', 'tt_notes']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['tt_name', 'tt_notes']
    # search_exclude_columns = [] # ['tt_name', 'tt_notes']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'tt_id': 'Tt Id', 'tt_name': 'Tt Name', 'tt_notes': 'Tt Notes'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['tt_name', 'tt_notes']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TransTypeModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TransTypeModelView, "Trans Type", icon="fa-folder-open-o", category="Setup")


class UserExtApi(ModelRestApi):
    datamodel = SQLAInterface(UserExt)

appbuilder.add_api(UserExtApi)

class UserExtModelView(ModelView):
    datamodel = SQLAInterface(UserExt)

    add_title = 'Add UserExt'
    # add_columns = ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'UserExt List'
    # list_columns = ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey'] #

    edit_title = 'Edit UserExt'
    # edit_columns = ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'manager_id_fk': 'Manager Id Fk', 'first_name': 'First Name', 'middle_name': 'Middle Name', 'surname': 'Surname', 'employee_number': 'Employee Number', 'job_title': 'Job Title', 'phone_number': 'Phone Number', 'email': 'Email', 'user_data': 'User Data', 'user_ext_manager_id_fk_fkey': 'User Ext Manager Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'manager_id_fk', 'first_name', 'middle_name', 'surname', 'employee_number', 'job_title', 'phone_number', 'email', 'user_data', 'user_ext_manager_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(UserExtModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(UserExtModelView, "User Ext", icon="fa-folder-open-o", category="Setup")


class BillerApi(ModelRestApi):
    datamodel = SQLAInterface(Biller)

appbuilder.add_api(BillerApi)

class BillerModelView(ModelView):
    datamodel = SQLAInterface(Biller)

    add_title = 'Add Biller'
    # add_columns = ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Biller List'
    # list_columns = ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey'] #

    edit_title = 'Edit Biller'
    # edit_columns = ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'cat_id_fk': 'Cat Id Fk', 'code': 'Code', 'name': 'Name', 'url': 'Url', 'note': 'Note', 'biller_cat_id_fk_fkey': 'Biller Cat Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'cat_id_fk', 'code', 'name', 'url', 'note', 'biller_cat_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(BillerModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(BillerModelView, "Biller", icon="fa-folder-open-o", category="Setup")


class StateApi(ModelRestApi):
    datamodel = SQLAInterface(State)

appbuilder.add_api(StateApi)

class StateModelView(ModelView):
    datamodel = SQLAInterface(State)

    add_title = 'Add State'
    # add_columns = ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'State List'
    # list_columns = ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # list_exclude_columns = [] # ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey'] #

    edit_title = 'Edit State'
    # edit_columns = ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # search_exclude_columns = [] # ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'country_id_fk': 'Country Id Fk', 'id': 'Id', 'code': 'Code', 'name': 'Name', 'desc': 'Desc', 'state_country_id_fk_fkey': 'State Country Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['country_id_fk', 'id', 'code', 'name', 'desc', 'state_country_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(StateModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(StateModelView, "State", icon="fa-folder-open-o", category="Setup")


class TokenApi(ModelRestApi):
    datamodel = SQLAInterface(Token)

appbuilder.add_api(TokenApi)

class TokenModelView(ModelView):
    datamodel = SQLAInterface(Token)

    add_title = 'Add Token'
    # add_columns = ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Token List'
    # list_columns = ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # list_exclude_columns = [] # ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey'] #

    edit_title = 'Edit Token'
    # edit_columns = ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # search_exclude_columns = [] # ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'token_id': 'Token Id', 'token_provider_id_fk': 'Token Provider Id Fk', 'token_name': 'Token Name', 'token_issue_date': 'Token Issue Date', 'token_expiry_date': 'Token Expiry Date', 'token_validity': 'Token Validity', 'token_expired': 'Token Expired', 'token_value': 'Token Value', 'token_username': 'Token Username', 'token_password': 'Token Password', 'token_notes': 'Token Notes', 'token_client_secret': 'Token Client Secret', 'enabled': 'Enabled', 'token_token_provider_id_fk_fkey': 'Token Token Provider Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['token_provider_id_fk', 'token_name', 'token_issue_date', 'token_expiry_date', 'token_validity', 'token_expired', 'token_value', 'token_username', 'token_password', 'token_notes', 'token_client_secret', 'enabled', 'token_token_provider_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TokenModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TokenModelView, "Token", icon="fa-folder-open-o", category="Setup")


class BillerOfferingApi(ModelRestApi):
    datamodel = SQLAInterface(BillerOffering)

appbuilder.add_api(BillerOfferingApi)

class BillerOfferingModelView(ModelView):
    datamodel = SQLAInterface(BillerOffering)

    add_title = 'Add BillerOffering'
    # add_columns = ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'BillerOffering List'
    # list_columns = ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # list_exclude_columns = [] # ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey'] #

    edit_title = 'Edit BillerOffering'
    # edit_columns = ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # search_exclude_columns = [] # ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'biller_id_fk': 'Biller Id Fk', 'offering_id': 'Offering Id', 'offering_name': 'Offering Name', 'offering_description': 'Offering Description', 'offering_price': 'Offering Price', 'biller_offering_biller_id_fk_fkey': 'Biller Offering Biller Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['biller_id_fk', 'offering_name', 'offering_description', 'offering_price', 'biller_offering_biller_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(BillerOfferingModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(BillerOfferingModelView, "Biller Offering", icon="fa-folder-open-o", category="Setup")


class LgaApi(ModelRestApi):
    datamodel = SQLAInterface(Lga)

appbuilder.add_api(LgaApi)

class LgaModelView(ModelView):
    datamodel = SQLAInterface(Lga)

    add_title = 'Add Lga'
    # add_columns = ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Lga List'
    # list_columns = ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey'] #

    edit_title = 'Edit Lga'
    # edit_columns = ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'state_id_fk': 'State Id Fk', 'code': 'Code', 'lga_name': 'Lga Name', 'lga_state_id_fk_fkey': 'Lga State Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'state_id_fk', 'code', 'lga_name', 'lga_state_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(LgaModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(LgaModelView, "Lga", icon="fa-folder-open-o", category="Setup")


class AgentApi(ModelRestApi):
    datamodel = SQLAInterface(Agent)

appbuilder.add_api(AgentApi)

class AgentModelView(ModelView):
    datamodel = SQLAInterface(Agent)

    add_title = 'Add Agent'
    # add_columns = ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Agent List'
    # list_columns = ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # list_exclude_columns = [] # ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey'] #

    edit_title = 'Edit Agent'
    # edit_columns = ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # search_exclude_columns = [] # ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'aggregator_id_fk': 'Aggregator Id Fk', 'is_aggregator': 'Is Aggregator', 'became_aggregator_date': 'Became Aggregator Date', 'assigned_pos_count': 'Assigned Pos Count', 'aggregator_pos_threshold': 'Aggregator Pos Threshold', 'registration_status': 'Registration Status', 'registration_status_notes': 'Registration Status Notes', 'agent_type': 'Agent Type', 'agent_role': 'Agent Role', 'agent_tier_id_fk': 'Agent Tier Id Fk', 'account_manager_id_fk': 'Account Manager Id Fk', 'agent_name': 'Agent Name', 'alias': 'Alias', 'phone_country_id_fk': 'Phone Country Id Fk', 'phone': 'Phone', 'phone_ext': 'Phone Ext', 'alt_phone_country_id_fk': 'Alt Phone Country Id Fk', 'alt_phone': 'Alt Phone', 'alt_phone_ext': 'Alt Phone Ext', 'email': 'Email', 'alt_email': 'Alt Email', 'bvn': 'Bvn', 'bvn_verified': 'Bvn Verified', 'bvn_verification_date': 'Bvn Verification Date', 'bvn_verification_code': 'Bvn Verification Code', 'tax_id': 'Tax Id', 'bank_id_fk': 'Bank Id Fk', 'bank_acc_no': 'Bank Acc No', 'biz_name': 'Biz Name', 'biz_state_id_fk': 'Biz State Id Fk', 'biz_lga_id_fk': 'Biz Lga Id Fk', 'biz_city': 'Biz City', 'biz_city_area': 'Biz City Area', 'biz_street': 'Biz Street', 'biz_building': 'Biz Building', 'biz_address': 'Biz Address', 'biz_poa_img': 'Biz Poa Img', 'biz_poa_desc': 'Biz Poa Desc', 'biz_poa_valid': 'Biz Poa Valid', 'biz_lat': 'Biz Lat', 'biz_lon': 'Biz Lon', 'biz_loc': 'Biz Loc', 'biz_ggl_code': 'Biz Ggl Code', 'company_name': 'Company Name', 'cac_number': 'Cac Number', 'cac_reg_date': 'Cac Reg Date', 'cac_cert_img': 'Cac Cert Img', 'cac_cert_no': 'Cac Cert No', 'ref_code': 'Ref Code', 'access_pin': 'Access Pin', 'registered_by_fk': 'Registered By Fk', 'registration_date': 'Registration Date', 'reviewed_by_fk': 'Reviewed By Fk', 'review_date': 'Review Date', 'approved_by_fk': 'Approved By Fk', 'approval_date': 'Approval Date', 'approval_narrative': 'Approval Narrative', 'kyc_submit_date': 'Kyc Submit Date', 'kyc_verification_status': 'Kyc Verification Status', 'kyc_approval_date': 'Kyc Approval Date', 'kyc_ref_code': 'Kyc Ref Code', 'kyc_rejection_narrative': 'Kyc Rejection Narrative', 'kyc_rejection_by_fk': 'Kyc Rejection By Fk', 'rejection_date': 'Rejection Date', 'rejection_narrative': 'Rejection Narrative', 'rejected_by_fk': 'Rejected By Fk', 'face_matrix': 'Face Matrix', 'finger_print_img': 'Finger Print Img', 'agent_public_key': 'Agent Public Key', 'agent_pj_expiry': 'Agent Pj Expiry', 'agent_history': 'Agent History', 'agent_account_manager_id_fk_fkey': 'Agent Account Manager Id Fk Fkey', 'agent_agent_tier_id_fk_fkey': 'Agent Agent Tier Id Fk Fkey', 'agent_aggregator_id_fk_fkey': 'Agent Aggregator Id Fk Fkey', 'agent_alt_phone_country_id_fk_fkey': 'Agent Alt Phone Country Id Fk Fkey', 'agent_approved_by_fk_fkey': 'Agent Approved By Fk Fkey', 'agent_bank_id_fk_fkey': 'Agent Bank Id Fk Fkey', 'agent_biz_lga_id_fk_fkey': 'Agent Biz Lga Id Fk Fkey', 'agent_biz_state_id_fk_fkey': 'Agent Biz State Id Fk Fkey', 'agent_kyc_rejection_by_fk_fkey': 'Agent Kyc Rejection By Fk Fkey', 'agent_phone_country_id_fk_fkey': 'Agent Phone Country Id Fk Fkey', 'agent_registered_by_fk_fkey': 'Agent Registered By Fk Fkey', 'agent_rejected_by_fk_fkey': 'Agent Rejected By Fk Fkey', 'agent_reviewed_by_fk_fkey': 'Agent Reviewed By Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'aggregator_id_fk', 'is_aggregator', 'became_aggregator_date', 'assigned_pos_count', 'aggregator_pos_threshold', 'registration_status', 'registration_status_notes', 'agent_type', 'agent_role', 'agent_tier_id_fk', 'account_manager_id_fk', 'agent_name', 'alias', 'phone_country_id_fk', 'phone', 'phone_ext', 'alt_phone_country_id_fk', 'alt_phone', 'alt_phone_ext', 'email', 'alt_email', 'bvn', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'bank_id_fk', 'bank_acc_no', 'biz_name', 'biz_state_id_fk', 'biz_lga_id_fk', 'biz_city', 'biz_city_area', 'biz_street', 'biz_building', 'biz_address', 'biz_poa_img', 'biz_poa_desc', 'biz_poa_valid', 'biz_lat', 'biz_lon', 'biz_loc', 'biz_ggl_code', 'company_name', 'cac_number', 'cac_reg_date', 'cac_cert_img', 'cac_cert_no', 'ref_code', 'access_pin', 'registered_by_fk', 'registration_date', 'reviewed_by_fk', 'review_date', 'approved_by_fk', 'approval_date', 'approval_narrative', 'kyc_submit_date', 'kyc_verification_status', 'kyc_approval_date', 'kyc_ref_code', 'kyc_rejection_narrative', 'kyc_rejection_by_fk', 'rejection_date', 'rejection_narrative', 'rejected_by_fk', 'face_matrix', 'finger_print_img', 'agent_public_key', 'agent_pj_expiry', 'agent_history', 'agent_account_manager_id_fk_fkey', 'agent_agent_tier_id_fk_fkey', 'agent_aggregator_id_fk_fkey', 'agent_alt_phone_country_id_fk_fkey', 'agent_approved_by_fk_fkey', 'agent_bank_id_fk_fkey', 'agent_biz_lga_id_fk_fkey', 'agent_biz_state_id_fk_fkey', 'agent_kyc_rejection_by_fk_fkey', 'agent_phone_country_id_fk_fkey', 'agent_registered_by_fk_fkey', 'agent_rejected_by_fk_fkey', 'agent_reviewed_by_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(AgentModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(AgentModelView, "Agent", icon="fa-folder-open-o", category="Setup")


class PosApi(ModelRestApi):
    datamodel = SQLAInterface(Pos)

appbuilder.add_api(PosApi)

class PosModelView(ModelView):
    datamodel = SQLAInterface(Pos)

    add_title = 'Add Pos'
    # add_columns = ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Pos List'
    # list_columns = ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # list_exclude_columns = [] # ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state'] #

    edit_title = 'Edit Pos'
    # edit_columns = ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # search_exclude_columns = [] # ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'serial_no': 'Serial No', 'imei': 'Imei', 'mac_addr': 'Mac Addr', 'device_model': 'Device Model', 'device_make': 'Device Make', 'device_mfg': 'Device Mfg', 'os_version': 'Os Version', 'device_color': 'Device Color', 'device_condition': 'Device Condition', 'status': 'Status', 'owner_type': 'Owner Type', 'registration_date': 'Registration Date', 'assigned': 'Assigned', 'assigned_date': 'Assigned Date', 'assigned_narrative': 'Assigned Narrative', 'active': 'Active', 'activation_date': 'Activation Date', 'last_active': 'Last Active', 'deployed': 'Deployed', 'deploy_date': 'Deploy Date', 'deploy_narrative': 'Deploy Narrative', 'returned': 'Returned', 'return_date': 'Return Date', 'return_narrative': 'Return Narrative', 'return_received_date': 'Return Received Date', 'return_received_by': 'Return Received By', 'state_id': 'State Id', 'lga_id': 'Lga Id', 'street_address': 'Street Address', 'building_name': 'Building Name', 'contact_phone_num': 'Contact Phone Num', 'pos_user': 'Pos User', 'crypt_priv_key': 'Crypt Priv Key', 'crypt_pub_key': 'Crypt Pub Key', 'crypt_password': 'Crypt Password', 'override_key': 'Override Key', 'pos_lga': 'Pos Lga', 'pos_return_received_by_fkey': 'Pos Return Received By Fkey', 'pos_state': 'Pos State'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'serial_no', 'imei', 'mac_addr', 'device_model', 'device_make', 'device_mfg', 'os_version', 'device_color', 'device_condition', 'status', 'owner_type', 'registration_date', 'assigned', 'assigned_date', 'assigned_narrative', 'active', 'activation_date', 'last_active', 'deployed', 'deploy_date', 'deploy_narrative', 'returned', 'return_date', 'return_narrative', 'return_received_date', 'return_received_by', 'street_address', 'building_name', 'contact_phone_num', 'pos_user', 'crypt_priv_key', 'crypt_pub_key', 'crypt_password', 'override_key', 'pos_lga', 'pos_return_received_by_fkey', 'pos_state']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PosModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PosModelView, "Pos", icon="fa-folder-open-o", category="Setup")


class AgentPosLinkApi(ModelRestApi):
    datamodel = SQLAInterface(AgentPosLink)

appbuilder.add_api(AgentPosLinkApi)

class AgentPosLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentPosLink)

    add_title = 'Add AgentPosLink'
    # add_columns = ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'AgentPosLink List'
    # list_columns = ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # list_exclude_columns = [] # ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey'] #

    edit_title = 'Edit AgentPosLink'
    # edit_columns = ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # search_exclude_columns = [] # ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'agent_id_fk': 'Agent Id Fk', 'pos_id_fk': 'Pos Id Fk', 'assigned_date': 'Assigned Date', 'assigned_by': 'Assigned By', 'received_by': 'Received By', 'received_date': 'Received Date', 'received_location': 'Received Location', 'delivery_note': 'Delivery Note', 'delivery_note_printed': 'Delivery Note Printed', 'activated': 'Activated', 'activation_date': 'Activation Date', 'activation_otp': 'Activation Otp', 'otp_sent': 'Otp Sent', 'otp_sent_time': 'Otp Sent Time', 'otp_used': 'Otp Used', 'history': 'History', 'agent_pos_link_agent_id_fk_fkey': 'Agent Pos Link Agent Id Fk Fkey', 'agent_pos_link_pos_id_fk_fkey': 'Agent Pos Link Pos Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['agent_id_fk', 'pos_id_fk', 'assigned_date', 'assigned_by', 'received_by', 'received_date', 'received_location', 'delivery_note', 'delivery_note_printed', 'activated', 'activation_date', 'activation_otp', 'otp_sent', 'otp_sent_time', 'otp_used', 'history', 'agent_pos_link_agent_id_fk_fkey', 'agent_pos_link_pos_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(AgentPosLinkModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(AgentPosLinkModelView, "Agent Pos Link", icon="fa-folder-open-o", category="Setup")


class CommRefApi(ModelRestApi):
    datamodel = SQLAInterface(CommRef)

appbuilder.add_api(CommRefApi)

class CommRefModelView(ModelView):
    datamodel = SQLAInterface(CommRef)

    add_title = 'Add CommRef'
    # add_columns = ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'CommRef List'
    # list_columns = ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # list_exclude_columns = [] # ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey'] #

    edit_title = 'Edit CommRef'
    # edit_columns = ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # search_exclude_columns = [] # ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'cr_id': 'Cr Id', 'agent_type': 'Agent Type', 'agent_tier_level': 'Agent Tier Level', 'agent_id_fk': 'Agent Id Fk', 'state_id_fk': 'State Id Fk', 'lga_id_fk': 'Lga Id Fk', 'biller_id_fk': 'Biller Id Fk', 'biller_offering_id_fk': 'Biller Offering Id Fk', 'transaction_type_id_fk': 'Transaction Type Id Fk', 'customer_segment_id_fk': 'Customer Segment Id Fk', 'special_promotion_id_fk': 'Special Promotion Id Fk', 'min_trans_amount': 'Min Trans Amount', 'max_trans_amount': 'Max Trans Amount', 'min_max_step': 'Min Max Step', 'min_comm_amount': 'Min Comm Amount', 'max_comm_amount': 'Max Comm Amount', 'commission_rate': 'Commission Rate', 'start_time': 'Start Time', 'end_time': 'End Time', 'start_date': 'Start Date', 'end_date': 'End Date', 'comm_ref_agent_id_fk_fkey': 'Comm Ref Agent Id Fk Fkey', 'comm_ref_agent_tier_level_fkey': 'Comm Ref Agent Tier Level Fkey', 'comm_ref_biller_id_fk_fkey': 'Comm Ref Biller Id Fk Fkey', 'comm_ref_biller_offering_id_fk_fkey': 'Comm Ref Biller Offering Id Fk Fkey', 'comm_ref_customer_segment_id_fk_fkey': 'Comm Ref Customer Segment Id Fk Fkey', 'comm_ref_lga_id_fk_fkey': 'Comm Ref Lga Id Fk Fkey', 'comm_ref_special_promotion_id_fk_fkey': 'Comm Ref Special Promotion Id Fk Fkey', 'comm_ref_state_id_fk_fkey': 'Comm Ref State Id Fk Fkey', 'comm_ref_transaction_type_id_fk_fkey': 'Comm Ref Transaction Type Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['agent_type', 'agent_tier_level', 'agent_id_fk', 'state_id_fk', 'lga_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'transaction_type_id_fk', 'customer_segment_id_fk', 'special_promotion_id_fk', 'min_trans_amount', 'max_trans_amount', 'min_max_step', 'min_comm_amount', 'max_comm_amount', 'commission_rate', 'start_time', 'end_time', 'start_date', 'end_date', 'comm_ref_agent_id_fk_fkey', 'comm_ref_agent_tier_level_fkey', 'comm_ref_biller_id_fk_fkey', 'comm_ref_biller_offering_id_fk_fkey', 'comm_ref_customer_segment_id_fk_fkey', 'comm_ref_lga_id_fk_fkey', 'comm_ref_special_promotion_id_fk_fkey', 'comm_ref_state_id_fk_fkey', 'comm_ref_transaction_type_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(CommRefModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(CommRefModelView, "Comm Ref", icon="fa-folder-open-o", category="Setup")


class PersonApi(ModelRestApi):
    datamodel = SQLAInterface(Person)

appbuilder.add_api(PersonApi)

class PersonModelView(ModelView):
    datamodel = SQLAInterface(Person)

    add_title = 'Add Person'
    # add_columns = ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Person List'
    # list_columns = ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey'] #

    edit_title = 'Edit Person'
    # edit_columns = ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'agent_id_fk': 'Agent Id Fk', 'next_of_kin_id_fk': 'Next Of Kin Id Fk', 'person_role': 'Person Role', 'first_name': 'First Name', 'middle_name': 'Middle Name', 'surname': 'Surname', 'nick_name': 'Nick Name', 'gender': 'Gender', 'photo_img': 'Photo Img', 'signature_img': 'Signature Img', 'bvn_no': 'Bvn No', 'bvn_verified': 'Bvn Verified', 'bvn_verification_date': 'Bvn Verification Date', 'bvn_verification_code': 'Bvn Verification Code', 'tax_id': 'Tax Id', 'home_poa_img': 'Home Poa Img', 'home_poa_desc': 'Home Poa Desc', 'home_poa_valid': 'Home Poa Valid', 'home_lat': 'Home Lat', 'home_lon': 'Home Lon', 'home_loc': 'Home Loc', 'home_ggl_code': 'Home Ggl Code', 'person_agent_id_fk_fkey': 'Person Agent Id Fk Fkey', 'person_next_of_kin_id_fk_fkey': 'Person Next Of Kin Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'agent_id_fk', 'next_of_kin_id_fk', 'person_role', 'first_name', 'middle_name', 'surname', 'nick_name', 'gender', 'photo_img', 'signature_img', 'bvn_no', 'bvn_verified', 'bvn_verification_date', 'bvn_verification_code', 'home_poa_img', 'home_poa_desc', 'home_poa_valid', 'home_lat', 'home_lon', 'home_loc', 'home_ggl_code', 'person_agent_id_fk_fkey', 'person_next_of_kin_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PersonModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PersonModelView, "Person", icon="fa-folder-open-o", category="Setup")


class WalletApi(ModelRestApi):
    datamodel = SQLAInterface(Wallet)

appbuilder.add_api(WalletApi)

class WalletModelView(ModelView):
    datamodel = SQLAInterface(Wallet)

    add_title = 'Add Wallet'
    # add_columns = ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Wallet List'
    # list_columns = ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey'] #

    edit_title = 'Edit Wallet'
    # edit_columns = ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'agent_id_fk': 'Agent Id Fk', 'pos_id_fk': 'Pos Id Fk', 'wallet_name': 'Wallet Name', 'wallet_balance': 'Wallet Balance', 'wallet_locked': 'Wallet Locked', 'wallet_active': 'Wallet Active', 'wallet_code': 'Wallet Code', 'wallet_crypt': 'Wallet Crypt', 'wallet_narrative': 'Wallet Narrative', 'wallet_agent_id_fk_fkey': 'Wallet Agent Id Fk Fkey', 'wallet_pos_id_fk_fkey': 'Wallet Pos Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'agent_id_fk', 'pos_id_fk', 'wallet_name', 'wallet_balance', 'wallet_locked', 'wallet_active', 'wallet_code', 'wallet_crypt', 'wallet_narrative', 'wallet_agent_id_fk_fkey', 'wallet_pos_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(WalletModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(WalletModelView, "Wallet", icon="fa-folder-open-o", category="Setup")


class AgentPersonLinkApi(ModelRestApi):
    datamodel = SQLAInterface(AgentPersonLink)

appbuilder.add_api(AgentPersonLinkApi)

class AgentPersonLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentPersonLink)

    add_title = 'Add AgentPersonLink'
    # add_columns = ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'AgentPersonLink List'
    # list_columns = ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # list_exclude_columns = [] # ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey'] #

    edit_title = 'Edit AgentPersonLink'
    # edit_columns = ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # search_exclude_columns = [] # ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'person_id_fk': 'Person Id Fk', 'agent_id_fk': 'Agent Id Fk', 'agent_person_link_agent_id_fk_fkey': 'Agent Person Link Agent Id Fk Fkey', 'agent_person_link_person_id_fk_fkey': 'Agent Person Link Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['person_id_fk', 'agent_id_fk', 'agent_person_link_agent_id_fk_fkey', 'agent_person_link_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(AgentPersonLinkModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(AgentPersonLinkModelView, "Agent Person Link", icon="fa-folder-open-o", category="Setup")


class ContactApi(ModelRestApi):
    datamodel = SQLAInterface(Contact)

appbuilder.add_api(ContactApi)

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    add_title = 'Add Contact'
    # add_columns = ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Contact List'
    # list_columns = ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey'] #

    edit_title = 'Edit Contact'
    # edit_columns = ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'person_id_fk': 'Person Id Fk', 'agent_id_fk': 'Agent Id Fk', 'contact_type_id_fk': 'Contact Type Id Fk', 'contact': 'Contact', 'priority': 'Priority', 'best_time_to_contact_start': 'Best Time To Contact Start', 'best_time_to_contact_end': 'Best Time To Contact End', 'active_from_date': 'Active From Date', 'active_to_date': 'Active To Date', 'for_business_use': 'For Business Use', 'for_personal_use': 'For Personal Use', 'do_not_use': 'Do Not Use', 'is_active': 'Is Active', 'is_blocked': 'Is Blocked', 'is_verified': 'Is Verified', 'notes': 'Notes', 'contact_agent_id_fk_fkey': 'Contact Agent Id Fk Fkey', 'contact_contact_type_id_fk_fkey': 'Contact Contact Type Id Fk Fkey', 'contact_person_id_fk_fkey': 'Contact Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'person_id_fk', 'agent_id_fk', 'contact_type_id_fk', 'contact', 'priority', 'best_time_to_contact_start', 'best_time_to_contact_end', 'active_from_date', 'active_to_date', 'for_business_use', 'for_personal_use', 'do_not_use', 'is_active', 'is_blocked', 'is_verified', 'notes', 'contact_agent_id_fk_fkey', 'contact_contact_type_id_fk_fkey', 'contact_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(ContactModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(ContactModelView, "Contact", icon="fa-folder-open-o", category="Setup")


class DocApi(ModelRestApi):
    datamodel = SQLAInterface(Doc)

appbuilder.add_api(DocApi)

class DocModelView(ModelView):
    datamodel = SQLAInterface(Doc)

    add_title = 'Add Doc'
    # add_columns = ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Doc List'
    # list_columns = ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey'] #

    edit_title = 'Edit Doc'
    # edit_columns = ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'doc_type_id_fk': 'Doc Type Id Fk', 'person_id_fk': 'Person Id Fk', 'agent_id_fk': 'Agent Id Fk', 'doc_name': 'Doc Name', 'doc_content_type': 'Doc Content Type', 'doc_binaary': 'Doc Binaary', 'doc_url': 'Doc Url', 'doc_length': 'Doc Length', 'doc_text': 'Doc Text', 'identification_number': 'Identification Number', 'serial_number': 'Serial Number', 'description': 'Description', 'file_name': 'File Name', 'page_count': 'Page Count', 'issued_on': 'Issued On', 'issued_by_authority': 'Issued By Authority', 'issued_at': 'Issued At', 'expires_on': 'Expires On', 'expired': 'Expired', 'verified': 'Verified', 'verification_date': 'Verification Date', 'verification_code': 'Verification Code', 'uploaded_on': 'Uploaded On', 'updated_on': 'Updated On', 'doc_agent_id_fk_fkey': 'Doc Agent Id Fk Fkey', 'doc_doc_content_type_fkey': 'Doc Doc Content Type Fkey', 'doc_doc_type_id_fk_fkey': 'Doc Doc Type Id Fk Fkey', 'doc_person_id_fk_fkey': 'Doc Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'doc_type_id_fk', 'person_id_fk', 'agent_id_fk', 'doc_name', 'doc_content_type', 'doc_binaary', 'doc_url', 'doc_length', 'doc_text', 'identification_number', 'serial_number', 'description', 'file_name', 'page_count', 'issued_on', 'issued_by_authority', 'issued_at', 'expires_on', 'expired', 'verified', 'verification_date', 'verification_code', 'uploaded_on', 'updated_on', 'doc_agent_id_fk_fkey', 'doc_doc_content_type_fkey', 'doc_doc_type_id_fk_fkey', 'doc_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(DocModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(DocModelView, "Doc", icon="fa-folder-open-o", category="Setup")


class PersonAdditionalDataApi(ModelRestApi):
    datamodel = SQLAInterface(PersonAdditionalData)

appbuilder.add_api(PersonAdditionalDataApi)

class PersonAdditionalDataModelView(ModelView):
    datamodel = SQLAInterface(PersonAdditionalData)

    add_title = 'Add PersonAdditionalData'
    # add_columns = ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'PersonAdditionalData List'
    # list_columns = ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # list_exclude_columns = [] # ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey'] #

    edit_title = 'Edit PersonAdditionalData'
    # edit_columns = ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # search_exclude_columns = [] # ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'person_id_fk': 'Person Id Fk', 'gender': 'Gender', 'religion': 'Religion', 'ethnicity': 'Ethnicity', 'consumer_credit_score': 'Consumer Credit Score', 'is_home_owner': 'Is Home Owner', 'person_height': 'Person Height', 'person_weight': 'Person Weight', 'person_height_unit_of_measure': 'Person Height Unit Of Measure', 'person_weight_unit_of_measure': 'Person Weight Unit Of Measure', 'highest_education_level': 'Highest Education Level', 'person_life_stage': 'Person Life Stage', 'mothers_maiden_name': 'Mothers Maiden Name', 'Marital_Status_cd': 'Marital Status Cd', 'citizenship_fk': 'Citizenship Fk', 'From_whom': 'From Whom', 'Amount': 'Amount', 'Interest_rate_pa': 'Interest Rate Pa', 'Number_of_people_depending_on_overal_income': 'Number Of People Depending On Overal Income', 'YesNo_cd_Bank_account': 'Yesno Cd Bank Account', 'YesNo_cd_Business_plan_provided': 'Yesno Cd Business Plan Provided', 'YesNo_cd_Access_to_internet': 'Yesno Cd Access To Internet', 'Introduced_by': 'Introduced By', 'Known_to_introducer_since': 'Known To Introducer Since', 'Last_visited_by': 'Last Visited By', 'Last_visited_on': 'Last Visited On', 'person_additional_data_citizenship_fk_fkey': 'Person Additional Data Citizenship Fk Fkey', 'person_additional_data_person_id_fk_fkey': 'Person Additional Data Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['person_id_fk', 'gender', 'religion', 'ethnicity', 'consumer_credit_score', 'is_home_owner', 'person_height', 'person_weight', 'person_height_unit_of_measure', 'person_weight_unit_of_measure', 'highest_education_level', 'person_life_stage', 'mothers_maiden_name', 'Marital_Status_cd', 'citizenship_fk', 'From_whom', 'Amount', 'Interest_rate_pa', 'Number_of_people_depending_on_overal_income', 'YesNo_cd_Bank_account', 'YesNo_cd_Business_plan_provided', 'YesNo_cd_Access_to_internet', 'Introduced_by', 'Known_to_introducer_since', 'Last_visited_by', 'Last_visited_on', 'person_additional_data_citizenship_fk_fkey', 'person_additional_data_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PersonAdditionalDataModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PersonAdditionalDataModelView, "Person Additional Data", icon="fa-folder-open-o", category="Setup")


class PersonAdminDataApi(ModelRestApi):
    datamodel = SQLAInterface(PersonAdminData)

appbuilder.add_api(PersonAdminDataApi)

class PersonAdminDataModelView(ModelView):
    datamodel = SQLAInterface(PersonAdminData)

    add_title = 'Add PersonAdminData'
    # add_columns = ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'PersonAdminData List'
    # list_columns = ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # list_exclude_columns = [] # ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey'] #

    edit_title = 'Edit PersonAdminData'
    # edit_columns = ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # search_exclude_columns = [] # ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'person_id_fk': 'Person Id Fk', 'creation_time': 'Creation Time', 'failed_login_count': 'Failed Login Count', 'failed_login_timestamp': 'Failed Login Timestamp', 'password_last_set_time': 'Password Last Set Time', 'profile_picture': 'Profile Picture', 'awatar': 'Awatar', 'screen_name': 'Screen Name', 'user_priv_cert': 'User Priv Cert', 'user_pub_cert': 'User Pub Cert', 'alt_security_identities': 'Alt Security Identities', 'generated_UID': 'Generated Uid', 'do_not_email': 'Do Not Email', 'do_not_phone': 'Do Not Phone', 'do_not_mail': 'Do Not Mail', 'do_not_sms': 'Do Not Sms', 'do_not_trade': 'Do Not Trade', 'opted_out': 'Opted Out', 'do_not_track_update_date': 'Do Not Track Update Date', 'do_not_process_from_update_date': 'Do Not Process From Update Date', 'do_not_market_from_update_date': 'Do Not Market From Update Date', 'do_not_track_location_update_date': 'Do Not Track Location Update Date', 'do_not_profile_from_update_date': 'Do Not Profile From Update Date', 'do_forget_me_from_update_date': 'Do Forget Me From Update Date', 'do_not_process_reason': 'Do Not Process Reason', 'no_merge_reason': 'No Merge Reason', 'do_extract_my_data_update_date': 'Do Extract My Data Update Date', 'should_forget': 'Should Forget', 'consumer_credit_score_provider_name': 'Consumer Credit Score Provider Name', 'web_site_url': 'Web Site Url', 'ordering_name': 'Ordering Name', 'hospitalizations_last5_years_count': 'Hospitalizations Last5 Years Count', 'surgeries_last5_years_count': 'Surgeries Last5 Years Count', 'dependent_count': 'Dependent Count', 'account_locked': 'Account Locked', 'send_individual_data': 'Send Individual Data', 'influencer_rating': 'Influencer Rating', 'person_admin_data_person_id_fk_fkey': 'Person Admin Data Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['person_id_fk', 'creation_time', 'failed_login_count', 'failed_login_timestamp', 'password_last_set_time', 'profile_picture', 'awatar', 'screen_name', 'user_priv_cert', 'user_pub_cert', 'alt_security_identities', 'generated_UID', 'do_not_email', 'do_not_phone', 'do_not_mail', 'do_not_sms', 'do_not_trade', 'opted_out', 'do_not_track_update_date', 'do_not_process_from_update_date', 'do_not_market_from_update_date', 'do_not_track_location_update_date', 'do_not_profile_from_update_date', 'do_forget_me_from_update_date', 'do_not_process_reason', 'no_merge_reason', 'do_extract_my_data_update_date', 'should_forget', 'consumer_credit_score_provider_name', 'web_site_url', 'ordering_name', 'hospitalizations_last5_years_count', 'surgeries_last5_years_count', 'dependent_count', 'account_locked', 'send_individual_data', 'influencer_rating', 'person_admin_data_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PersonAdminDataModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PersonAdminDataModelView, "Person Admin Data", icon="fa-folder-open-o", category="Setup")


class TransApi(ModelRestApi):
    datamodel = SQLAInterface(Trans)

appbuilder.add_api(TransApi)

class TransModelView(ModelView):
    datamodel = SQLAInterface(Trans)

    add_title = 'Add Trans'
    # add_columns = ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'Trans List'
    # list_columns = ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # list_exclude_columns = [] # ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey'] #

    edit_title = 'Edit Trans'
    # edit_columns = ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # search_exclude_columns = [] # ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'id': 'Id', 'coupon_id_fk': 'Coupon Id Fk', 'customer_name': 'Customer Name', 'trans_purpose': 'Trans Purpose', 'customer_id': 'Customer Id', 'transaction_type': 'Transaction Type', 'card_trans_type': 'Card Trans Type', 'agent_id_fk': 'Agent Id Fk', 'payment_card_id_fk': 'Payment Card Id Fk', 'pos_id_fk': 'Pos Id Fk', 'wallet_id_fk': 'Wallet Id Fk', 'biller_id_fk': 'Biller Id Fk', 'biller_offering_id_fk': 'Biller Offering Id Fk', 'trans_time': 'Trans Time', 'currency_id_fk': 'Currency Id Fk', 'trans_status': 'Trans Status', 'trans_route_id_fk': 'Trans Route Id Fk', 'origin_source': 'Origin Source', 'origin_ref_code': 'Origin Ref Code', 'origin_trans_notes': 'Origin Trans Notes', 'origin_bank_id_fk': 'Origin Bank Id Fk', 'origin_institution_code': 'Origin Institution Code', 'origin_account_num': 'Origin Account Num', 'origin_account_name': 'Origin Account Name', 'origin_KYC_Level': 'Origin Kyc Level', 'origin_Bank_Verification_Number': 'Origin Bank Verification Number', 'origin_bvn': 'Origin Bvn', 'session_ref': 'Session Ref', 'transaction_ref': 'Transaction Ref', 'channelCode': 'Channelcode', 'name_enquiry_ref': 'Name Enquiry Ref', 'api_transactionid': 'Api Transactionid', 'receipt_no': 'Receipt No', 'pin_based': 'Pin Based', 'pin_code': 'Pin Code', 'pin_option': 'Pin Option', 'authorization_code': 'Authorization Code', 'acquirer_name': 'Acquirer Name', 'currency': 'Currency', 'transaction_location': 'Transaction Location', 'payment_reference': 'Payment Reference', 'response_code': 'Response Code', 'trans_dest': 'Trans Dest', 'bene_ref_code': 'Bene Ref Code', 'bene_trans_notes': 'Bene Trans Notes', 'bene_bank_id_fk': 'Bene Bank Id Fk', 'bene_account_num': 'Bene Account Num', 'bene_institution_code': 'Bene Institution Code', 'bene_bank_verification_number': 'Bene Bank Verification Number', 'bene_KYC_Level': 'Bene Kyc Level', 'bene_account_name': 'Bene Account Name', 'bene_phone_number': 'Bene Phone Number', 'bene_phone_denom': 'Bene Phone Denom', 'bene_phone_product': 'Bene Phone Product', 'transaction_amount': 'Transaction Amount', 'available_balance': 'Available Balance', 'svc_fees': 'Svc Fees', 'comm_total': 'Comm Total', 'comm_agent': 'Comm Agent', 'comm_aggr': 'Comm Aggr', 'comm_ours': 'Comm Ours', 'comm_other': 'Comm Other', 'comm_net_pct': 'Comm Net Pct', 'tax': 'Tax', 'excise_duty': 'Excise Duty', 'vat': 'Vat', 'transmit_amount': 'Transmit Amount', 'comm_narration': 'Comm Narration', 'trans_currency': 'Trans Currency', 'trans_convert_currency': 'Trans Convert Currency', 'trans_currency_exchange_rate': 'Trans Currency Exchange Rate', 'trans_date': 'Trans Date', 'customer_segment_id_fk': 'Customer Segment Id Fk', 'agent_tier_level_id_fk': 'Agent Tier Level Id Fk', 'special_promotions_id_fk': 'Special Promotions Id Fk', 'fraud_marker': 'Fraud Marker', 'fraud_eval_outcome': 'Fraud Eval Outcome', 'fraud_risk_score': 'Fraud Risk Score', 'fraud_prediction_explanations': 'Fraud Prediction Explanations', 'fraud_rule_evaluations': 'Fraud Rule Evaluations', 'fraud_event_num': 'Fraud Event Num', 'trans_narration': 'Trans Narration', 'trans_agent_id_fk_fkey': 'Trans Agent Id Fk Fkey', 'trans_agent_tier_level_id_fk_fkey': 'Trans Agent Tier Level Id Fk Fkey', 'trans_bene_bank_id_fk_fkey': 'Trans Bene Bank Id Fk Fkey', 'trans_biller_id_fk_fkey': 'Trans Biller Id Fk Fkey', 'trans_biller_offering_id_fk_fkey': 'Trans Biller Offering Id Fk Fkey', 'trans_coupon_id_fk_fkey': 'Trans Coupon Id Fk Fkey', 'trans_currency_id_fk_fkey': 'Trans Currency Id Fk Fkey', 'trans_customer_segment_id_fk_fkey': 'Trans Customer Segment Id Fk Fkey', 'trans_origin_bank_id_fk_fkey': 'Trans Origin Bank Id Fk Fkey', 'trans_payment_card_id_fk_fkey': 'Trans Payment Card Id Fk Fkey', 'trans_pos_id_fk_fkey': 'Trans Pos Id Fk Fkey', 'trans_special_promotions_id_fk_fkey': 'Trans Special Promotions Id Fk Fkey', 'trans_trans_route_id_fk_fkey': 'Trans Trans Route Id Fk Fkey', 'trans_wallet_id_fk_fkey': 'Trans Wallet Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['id', 'coupon_id_fk', 'customer_name', 'trans_purpose', 'transaction_type', 'card_trans_type', 'agent_id_fk', 'payment_card_id_fk', 'pos_id_fk', 'wallet_id_fk', 'biller_id_fk', 'biller_offering_id_fk', 'trans_time', 'currency_id_fk', 'trans_status', 'trans_route_id_fk', 'origin_source', 'origin_ref_code', 'origin_trans_notes', 'origin_bank_id_fk', 'origin_institution_code', 'origin_account_num', 'origin_account_name', 'origin_KYC_Level', 'origin_Bank_Verification_Number', 'origin_bvn', 'session_ref', 'transaction_ref', 'channelCode', 'name_enquiry_ref', 'api_transactionid', 'receipt_no', 'pin_based', 'pin_code', 'pin_option', 'authorization_code', 'acquirer_name', 'currency', 'transaction_location', 'payment_reference', 'response_code', 'trans_dest', 'bene_ref_code', 'bene_trans_notes', 'bene_bank_id_fk', 'bene_account_num', 'bene_institution_code', 'bene_bank_verification_number', 'bene_KYC_Level', 'bene_account_name', 'bene_phone_number', 'bene_phone_denom', 'bene_phone_product', 'transaction_amount', 'available_balance', 'svc_fees', 'comm_total', 'comm_agent', 'comm_aggr', 'comm_ours', 'comm_other', 'comm_net_pct', 'tax', 'excise_duty', 'vat', 'transmit_amount', 'comm_narration', 'trans_currency', 'trans_convert_currency', 'trans_currency_exchange_rate', 'trans_date', 'customer_segment_id_fk', 'agent_tier_level_id_fk', 'special_promotions_id_fk', 'fraud_marker', 'fraud_eval_outcome', 'fraud_risk_score', 'fraud_prediction_explanations', 'fraud_rule_evaluations', 'fraud_event_num', 'trans_narration', 'trans_agent_id_fk_fkey', 'trans_agent_tier_level_id_fk_fkey', 'trans_bene_bank_id_fk_fkey', 'trans_biller_id_fk_fkey', 'trans_biller_offering_id_fk_fkey', 'trans_coupon_id_fk_fkey', 'trans_currency_id_fk_fkey', 'trans_customer_segment_id_fk_fkey', 'trans_origin_bank_id_fk_fkey', 'trans_payment_card_id_fk_fkey', 'trans_pos_id_fk_fkey', 'trans_special_promotions_id_fk_fkey', 'trans_trans_route_id_fk_fkey', 'trans_wallet_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(TransModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(TransModelView, "Trans", icon="fa-folder-open-o", category="Setup")


class AgentDocLinkApi(ModelRestApi):
    datamodel = SQLAInterface(AgentDocLink)

appbuilder.add_api(AgentDocLinkApi)

class AgentDocLinkModelView(ModelView):
    datamodel = SQLAInterface(AgentDocLink)

    add_title = 'Add AgentDocLink'
    # add_columns = ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'AgentDocLink List'
    # list_columns = ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # list_exclude_columns = [] # ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey'] #

    edit_title = 'Edit AgentDocLink'
    # edit_columns = ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # search_exclude_columns = [] # ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'agent_id_fk': 'Agent Id Fk', 'doc_id_fk': 'Doc Id Fk', 'verification_status': 'Verification Status', 'submit_date': 'Submit Date', 'notes': 'Notes', 'agent_doc_link_agent_id_fk_fkey': 'Agent Doc Link Agent Id Fk Fkey', 'agent_doc_link_doc_id_fk_fkey': 'Agent Doc Link Doc Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['agent_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'notes', 'agent_doc_link_agent_id_fk_fkey', 'agent_doc_link_doc_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(AgentDocLinkModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(AgentDocLinkModelView, "Agent Doc Link", icon="fa-folder-open-o", category="Setup")


class PersonDocLinkApi(ModelRestApi):
    datamodel = SQLAInterface(PersonDocLink)

appbuilder.add_api(PersonDocLinkApi)

class PersonDocLinkModelView(ModelView):
    datamodel = SQLAInterface(PersonDocLink)

    add_title = 'Add PersonDocLink'
    # add_columns = ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # add_exclude_columns = hide_list
    # add_fieldset =  []

    list_title= 'PersonDocLink List'
    # list_columns = ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # list_exclude_columns = [] # ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey'] #

    edit_title = 'Edit PersonDocLink'
    # edit_columns = ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # edit_fieldset =  []
    # edit_exclude_columns = hide_list #

    # show_columns = ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # show_fieldset =  []
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = [] + ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # search_exclude_columns = [] # ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {'person_id_fk': 'Person Id Fk', 'doc_id_fk': 'Doc Id Fk', 'verification_status': 'Verification Status', 'submit_date': 'Submit Date', 'person_doc_link_doc_id_fk_fkey': 'Person Doc Link Doc Id Fk Fkey', 'person_doc_link_person_id_fk_fkey': 'Person Doc Link Person Id Fk Fkey'}
#   # label_columns=   [{column.name: column.name for column in table.columns} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {
#      "basic_info": {
#           "title": "Basic Information",
#           "fields": []
#            },
#      "advanced_settings": {
#           "title": "Advanced Settings",
#           "fields": ['person_id_fk', 'doc_id_fk', 'verification_status', 'submit_date', 'person_doc_link_doc_id_fk_fkey', 'person_doc_link_person_id_fk_fkey']
#            }
#      }

#     def prefill_form(self, form, pk):
#        form = super(PersonDocLinkModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {"search_vector": item.search_vector}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {"query": {"match": {"search_vector": q}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )


appbuilder.add_view(PersonDocLinkModelView, "Person Doc Link", icon="fa-folder-open-o", category="Setup")



# Based on FK between: UserExt.manager_id_fk == user_ext.id
class UserExtUserExtView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [UserExtModelView]

appbuilder.add_view(UserExtUserExtView(), "UserExt_UserExt Review", icon="fa-folder-open-o", category="UserExt")



# Based on FK between: Biller.cat_id_fk == biller_category.id
class BillerCategoryBillerView(MasterDetailView):
    datamodel = SQLAInterface(BillerCategory)
    related_views = [BillerModelView]

appbuilder.add_view(BillerCategoryBillerView(), "BillerCategory_Biller Review", icon="fa-folder-open-o", category="BillerCategory")



# Based on FK between: State.country_id_fk == country.id
class CountryStateView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [StateModelView]

appbuilder.add_view(CountryStateView(), "Country_State Review", icon="fa-folder-open-o", category="Country")



# Based on FK between: Token.token_provider_id_fk == token_provider.token_provider_id
class TokenProviderTokenView(MasterDetailView):
    datamodel = SQLAInterface(TokenProvider)
    related_views = [TokenModelView]

appbuilder.add_view(TokenProviderTokenView(), "TokenProvider_Token Review", icon="fa-folder-open-o", category="TokenProvider")



# Based on FK between: BillerOffering.biller_id_fk == biller.id
class BillerBillerOfferingView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [BillerOfferingModelView]

appbuilder.add_view(BillerBillerOfferingView(), "Biller_BillerOffering Review", icon="fa-folder-open-o", category="Biller")



# Based on FK between: Lga.state_id_fk == state.id
class StateLgaView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [LgaModelView]

appbuilder.add_view(StateLgaView(), "State_Lga Review", icon="fa-folder-open-o", category="State")



# Based on FK between: Agent.account_manager_id_fk == user_ext.id
class UserExtAgentView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [AgentModelView]

appbuilder.add_view(UserExtAgentView(), "UserExt_Agent Review", icon="fa-folder-open-o", category="UserExt")



# Based on FK between: Agent.agent_tier_id_fk == agent_tier.id
class AgentTierAgentView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [AgentModelView]

appbuilder.add_view(AgentTierAgentView(), "AgentTier_Agent Review", icon="fa-folder-open-o", category="AgentTier")



# Based on FK between: Agent.aggregator_id_fk == agent.id
class AgentAgentView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentModelView]

appbuilder.add_view(AgentAgentView(), "Agent_Agent Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Agent.alt_phone_country_id_fk == country.id
class CountryAgentView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [AgentModelView]

appbuilder.add_view(CountryAgentView(), "Country_Agent Review", icon="fa-folder-open-o", category="Country")



# Based on FK between: Agent.bank_id_fk == bank.id
class BankAgentView(MasterDetailView):
    datamodel = SQLAInterface(Bank)
    related_views = [AgentModelView]

appbuilder.add_view(BankAgentView(), "Bank_Agent Review", icon="fa-folder-open-o", category="Bank")



# Based on FK between: Agent.biz_lga_id_fk == lga.id
class LgaAgentView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [AgentModelView]

appbuilder.add_view(LgaAgentView(), "Lga_Agent Review", icon="fa-folder-open-o", category="Lga")



# Based on FK between: Agent.biz_state_id_fk == state.id
class StateAgentView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [AgentModelView]

appbuilder.add_view(StateAgentView(), "State_Agent Review", icon="fa-folder-open-o", category="State")



# Based on FK between: Pos.lga_id == lga.id
class LgaPosView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [PosModelView]

appbuilder.add_view(LgaPosView(), "Lga_Pos Review", icon="fa-folder-open-o", category="Lga")



# Based on FK between: Pos.return_received_by == user_ext.id
class UserExtPosView(MasterDetailView):
    datamodel = SQLAInterface(UserExt)
    related_views = [PosModelView]

appbuilder.add_view(UserExtPosView(), "UserExt_Pos Review", icon="fa-folder-open-o", category="UserExt")



# Based on FK between: Pos.state_id == state.id
class StatePosView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [PosModelView]

appbuilder.add_view(StatePosView(), "State_Pos Review", icon="fa-folder-open-o", category="State")



# Based on FK between: AgentPosLink.agent_id_fk == agent.id
class AgentAgentPosLinkView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentPosLinkModelView]

appbuilder.add_view(AgentAgentPosLinkView(), "Agent_AgentPosLink Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: AgentPosLink.pos_id_fk == pos.id
class PosAgentPosLinkView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [AgentPosLinkModelView]

appbuilder.add_view(PosAgentPosLinkView(), "Pos_AgentPosLink Review", icon="fa-folder-open-o", category="Pos")



# Based on FK between: CommRef.agent_id_fk == agent.id
class AgentCommRefView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [CommRefModelView]

appbuilder.add_view(AgentCommRefView(), "Agent_CommRef Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: CommRef.agent_tier_level == agent_tier.id
class AgentTierCommRefView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [CommRefModelView]

appbuilder.add_view(AgentTierCommRefView(), "AgentTier_CommRef Review", icon="fa-folder-open-o", category="AgentTier")



# Based on FK between: CommRef.biller_id_fk == biller.id
class BillerCommRefView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [CommRefModelView]

appbuilder.add_view(BillerCommRefView(), "Biller_CommRef Review", icon="fa-folder-open-o", category="Biller")



# Based on FK between: CommRef.biller_offering_id_fk == biller_offering.offering_id
class BillerOfferingCommRefView(MasterDetailView):
    datamodel = SQLAInterface(BillerOffering)
    related_views = [CommRefModelView]

appbuilder.add_view(BillerOfferingCommRefView(), "BillerOffering_CommRef Review", icon="fa-folder-open-o", category="BillerOffering")



# Based on FK between: CommRef.customer_segment_id_fk == customer_segment.cs_id
class CustomerSegmentCommRefView(MasterDetailView):
    datamodel = SQLAInterface(CustomerSegment)
    related_views = [CommRefModelView]

appbuilder.add_view(CustomerSegmentCommRefView(), "CustomerSegment_CommRef Review", icon="fa-folder-open-o", category="CustomerSegment")



# Based on FK between: CommRef.lga_id_fk == lga.id
class LgaCommRefView(MasterDetailView):
    datamodel = SQLAInterface(Lga)
    related_views = [CommRefModelView]

appbuilder.add_view(LgaCommRefView(), "Lga_CommRef Review", icon="fa-folder-open-o", category="Lga")



# Based on FK between: CommRef.special_promotion_id_fk == promotion.promo_id
class PromotionCommRefView(MasterDetailView):
    datamodel = SQLAInterface(Promotion)
    related_views = [CommRefModelView]

appbuilder.add_view(PromotionCommRefView(), "Promotion_CommRef Review", icon="fa-folder-open-o", category="Promotion")



# Based on FK between: CommRef.state_id_fk == state.id
class StateCommRefView(MasterDetailView):
    datamodel = SQLAInterface(State)
    related_views = [CommRefModelView]

appbuilder.add_view(StateCommRefView(), "State_CommRef Review", icon="fa-folder-open-o", category="State")



# Based on FK between: CommRef.transaction_type_id_fk == trans_type.tt_id
class TransTypeCommRefView(MasterDetailView):
    datamodel = SQLAInterface(TransType)
    related_views = [CommRefModelView]

appbuilder.add_view(TransTypeCommRefView(), "TransType_CommRef Review", icon="fa-folder-open-o", category="TransType")



# Based on FK between: Person.agent_id_fk == agent.id
class AgentPersonView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [PersonModelView]

appbuilder.add_view(AgentPersonView(), "Agent_Person Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Person.next_of_kin_id_fk == person.id
class PersonPersonView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonModelView]

appbuilder.add_view(PersonPersonView(), "Person_Person Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: Wallet.agent_id_fk == agent.id
class AgentWalletView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [WalletModelView]

appbuilder.add_view(AgentWalletView(), "Agent_Wallet Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Wallet.pos_id_fk == pos.id
class PosWalletView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [WalletModelView]

appbuilder.add_view(PosWalletView(), "Pos_Wallet Review", icon="fa-folder-open-o", category="Pos")



# Based on FK between: AgentPersonLink.agent_id_fk == agent.id
class AgentAgentPersonLinkView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentPersonLinkModelView]

appbuilder.add_view(AgentAgentPersonLinkView(), "Agent_AgentPersonLink Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: AgentPersonLink.person_id_fk == person.id
class PersonAgentPersonLinkView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [AgentPersonLinkModelView]

appbuilder.add_view(PersonAgentPersonLinkView(), "Person_AgentPersonLink Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: Contact.agent_id_fk == agent.id
class AgentContactView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [ContactModelView]

appbuilder.add_view(AgentContactView(), "Agent_Contact Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Contact.contact_type_id_fk == contact_type.id
class ContactTypeContactView(MasterDetailView):
    datamodel = SQLAInterface(ContactType)
    related_views = [ContactModelView]

appbuilder.add_view(ContactTypeContactView(), "ContactType_Contact Review", icon="fa-folder-open-o", category="ContactType")



# Based on FK between: Contact.person_id_fk == person.id
class PersonContactView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [ContactModelView]

appbuilder.add_view(PersonContactView(), "Person_Contact Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: Doc.agent_id_fk == agent.id
class AgentDocView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [DocModelView]

appbuilder.add_view(AgentDocView(), "Agent_Doc Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Doc.doc_content_type == mime_type.id
class MimeTypeDocView(MasterDetailView):
    datamodel = SQLAInterface(MimeType)
    related_views = [DocModelView]

appbuilder.add_view(MimeTypeDocView(), "MimeType_Doc Review", icon="fa-folder-open-o", category="MimeType")



# Based on FK between: Doc.doc_type_id_fk == doc_type.id
class DocTypeDocView(MasterDetailView):
    datamodel = SQLAInterface(DocType)
    related_views = [DocModelView]

appbuilder.add_view(DocTypeDocView(), "DocType_Doc Review", icon="fa-folder-open-o", category="DocType")



# Based on FK between: Doc.person_id_fk == person.id
class PersonDocView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [DocModelView]

appbuilder.add_view(PersonDocView(), "Person_Doc Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: PersonAdditionalData.citizenship_fk == country.id
class CountryPersonAdditionalDataView(MasterDetailView):
    datamodel = SQLAInterface(Country)
    related_views = [PersonAdditionalDataModelView]

appbuilder.add_view(CountryPersonAdditionalDataView(), "Country_PersonAdditionalData Review", icon="fa-folder-open-o", category="Country")



# Based on FK between: PersonAdditionalData.person_id_fk == person.id
class PersonPersonAdditionalDataView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonAdditionalDataModelView]

appbuilder.add_view(PersonPersonAdditionalDataView(), "Person_PersonAdditionalData Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: PersonAdminData.person_id_fk == person.id
class PersonPersonAdminDataView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonAdminDataModelView]

appbuilder.add_view(PersonPersonAdminDataView(), "Person_PersonAdminData Review", icon="fa-folder-open-o", category="Person")



# Based on FK between: Trans.agent_id_fk == agent.id
class AgentTransView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [TransModelView]

appbuilder.add_view(AgentTransView(), "Agent_Trans Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: Trans.agent_tier_level_id_fk == agent_tier.id
class AgentTierTransView(MasterDetailView):
    datamodel = SQLAInterface(AgentTier)
    related_views = [TransModelView]

appbuilder.add_view(AgentTierTransView(), "AgentTier_Trans Review", icon="fa-folder-open-o", category="AgentTier")



# Based on FK between: Trans.bene_bank_id_fk == bank.id
class BankTransView(MasterDetailView):
    datamodel = SQLAInterface(Bank)
    related_views = [TransModelView]

appbuilder.add_view(BankTransView(), "Bank_Trans Review", icon="fa-folder-open-o", category="Bank")



# Based on FK between: Trans.biller_id_fk == biller.id
class BillerTransView(MasterDetailView):
    datamodel = SQLAInterface(Biller)
    related_views = [TransModelView]

appbuilder.add_view(BillerTransView(), "Biller_Trans Review", icon="fa-folder-open-o", category="Biller")



# Based on FK between: Trans.biller_offering_id_fk == biller_offering.offering_id
class BillerOfferingTransView(MasterDetailView):
    datamodel = SQLAInterface(BillerOffering)
    related_views = [TransModelView]

appbuilder.add_view(BillerOfferingTransView(), "BillerOffering_Trans Review", icon="fa-folder-open-o", category="BillerOffering")



# Based on FK between: Trans.coupon_id_fk == coupon.coupon_id
class CouponTransView(MasterDetailView):
    datamodel = SQLAInterface(Coupon)
    related_views = [TransModelView]

appbuilder.add_view(CouponTransView(), "Coupon_Trans Review", icon="fa-folder-open-o", category="Coupon")



# Based on FK between: Trans.currency_id_fk == currency.id
class CurrencyTransView(MasterDetailView):
    datamodel = SQLAInterface(Currency)
    related_views = [TransModelView]

appbuilder.add_view(CurrencyTransView(), "Currency_Trans Review", icon="fa-folder-open-o", category="Currency")



# Based on FK between: Trans.customer_segment_id_fk == customer_segment.cs_id
class CustomerSegmentTransView(MasterDetailView):
    datamodel = SQLAInterface(CustomerSegment)
    related_views = [TransModelView]

appbuilder.add_view(CustomerSegmentTransView(), "CustomerSegment_Trans Review", icon="fa-folder-open-o", category="CustomerSegment")



# Based on FK between: Trans.payment_card_id_fk == payment_card.id
class PaymentCardTransView(MasterDetailView):
    datamodel = SQLAInterface(PaymentCard)
    related_views = [TransModelView]

appbuilder.add_view(PaymentCardTransView(), "PaymentCard_Trans Review", icon="fa-folder-open-o", category="PaymentCard")



# Based on FK between: Trans.pos_id_fk == pos.id
class PosTransView(MasterDetailView):
    datamodel = SQLAInterface(Pos)
    related_views = [TransModelView]

appbuilder.add_view(PosTransView(), "Pos_Trans Review", icon="fa-folder-open-o", category="Pos")



# Based on FK between: Trans.special_promotions_id_fk == promotion.promo_id
class PromotionTransView(MasterDetailView):
    datamodel = SQLAInterface(Promotion)
    related_views = [TransModelView]

appbuilder.add_view(PromotionTransView(), "Promotion_Trans Review", icon="fa-folder-open-o", category="Promotion")



# Based on FK between: Trans.trans_route_id_fk == trans_routing_thresholds.id
class TransRoutingThresholdsTransView(MasterDetailView):
    datamodel = SQLAInterface(TransRoutingThresholds)
    related_views = [TransModelView]

appbuilder.add_view(TransRoutingThresholdsTransView(), "TransRoutingThresholds_Trans Review", icon="fa-folder-open-o", category="TransRoutingThresholds")



# Based on FK between: Trans.wallet_id_fk == wallet.id
class WalletTransView(MasterDetailView):
    datamodel = SQLAInterface(Wallet)
    related_views = [TransModelView]

appbuilder.add_view(WalletTransView(), "Wallet_Trans Review", icon="fa-folder-open-o", category="Wallet")



# Based on FK between: AgentDocLink.agent_id_fk == agent.id
class AgentAgentDocLinkView(MasterDetailView):
    datamodel = SQLAInterface(Agent)
    related_views = [AgentDocLinkModelView]

appbuilder.add_view(AgentAgentDocLinkView(), "Agent_AgentDocLink Review", icon="fa-folder-open-o", category="Agent")



# Based on FK between: AgentDocLink.doc_id_fk == doc.id
class DocAgentDocLinkView(MasterDetailView):
    datamodel = SQLAInterface(Doc)
    related_views = [AgentDocLinkModelView]

appbuilder.add_view(DocAgentDocLinkView(), "Doc_AgentDocLink Review", icon="fa-folder-open-o", category="Doc")



# Based on FK between: PersonDocLink.doc_id_fk == doc.id
class DocPersonDocLinkView(MasterDetailView):
    datamodel = SQLAInterface(Doc)
    related_views = [PersonDocLinkModelView]

appbuilder.add_view(DocPersonDocLinkView(), "Doc_PersonDocLink Review", icon="fa-folder-open-o", category="Doc")



# Based on FK between: PersonDocLink.person_id_fk == person.id
class PersonPersonDocLinkView(MasterDetailView):
    datamodel = SQLAInterface(Person)
    related_views = [PersonDocLinkModelView]

appbuilder.add_view(PersonPersonDocLinkView(), "Person_PersonDocLink Review", icon="fa-folder-open-o", category="Person")


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
