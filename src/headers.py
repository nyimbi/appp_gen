from datetime import date
from utils import *



def gen_model_header():
    model_header = []
    model_header.append(DOC_HEADER)
    model_header.append('import datetime, enum')
    model_header.append('from flask_appbuilder import Model')
    model_header.append('from sqlalchemy import Column, Integer, Boolean, String, Float, Enum, ForeignKey, Date, DateTime, Text')
    model_header.append('from sqlalchemy.orm import relationship, backref\n')
    model_header.append(MODEL_HEADER)
    return model_header


def gen_view_header():
    view_header = []
    view_header.append(DOC_HEADER)
    view_header.append(VIEW_HEADER)
    view_header.append("from flask_appbuilder import ModelView")
    view_header.append("from flask_appbuilder.models.sqla.interface import SQLAInterface")
    view_header.append("from flask_appbuilder.views import MasterDetailView, MultipleView")
    view_header.append('from .models import *\n')
    return view_header


def gen_api_header():
    api_header = []
    api_header.append(DOC_HEADER)
    api_header.append(API_HEADER)
    api_header.append(f"from flask_appbuilder.api import ModelRestApi, BaseApi, expose, rison")
    api_header.append(f"from flask_appbuilder.models.sqla.interface import SQLAInterface")
    return api_header


DOC_HEADER = f"""
# coding: utf-8
# AUTOGENERATED BY appgen 
# Copyright (C) Nyimbi Odero, {date.today().year} \n\n
 """


VIEW_HEADER = """
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
# from flask_mail import Message, Mail
# from flask.ext.babel import lazy_gettext as _
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

"""

MODEL_HEADER = """
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
    Sequence, Float, Text, BigInteger, Date, SmallInteger, BigInteger, 
    DateTime, Time, Boolean, Index, CheckConstraint, Interval, # MatchType  
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


# from .model_mixins import *

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


"""

DATA_DICTIONARY_MODELS = """
# WE geneerate the model data dictionary
# Define the app_Table, app_Column, and app_Relationship tables

class app_Tables(Base):
    __tablename__ = 'app_tables'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    schema = Column(String)
    comment = Column(String)
    columns = relationship('app_Column')
    indexes = relationship('app_Index')

class app_Columns(Base):
    __tablename__ = 'app_columns'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data_type = Column(String)
    nullable = Column(Boolean)
    primary_key = Column(Boolean)
    autoincrement = Column(Boolean)
    unique = Column(Boolean) 
    default = Column(String)
    server_default = Column(String)
    check_constraint = Column(String)
    comment = Column(String)
    foreign_key = Column(String)
    unique_constraint = Column(String)
    indexed = Column(Boolean)
    table_id = Column(Integer, ForeignKey('app_table.id'))
    table = relationship('app_Table')

class app_Relations(Base):
    __tablename__ = 'app_relations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
   
    source_table_id = Column(Integer, ForeignKey('app_tables.id'))
    source_table = relationship('app_Table', foreign_keys=[source_table_id])
    source_column_id = Column(Integer, ForeignKey('app_columns.id'))
    source_column = relationship('app_Column', foreign_keys=[source_column_id])
    referred_table_id = Column(Integer, ForeignKey('app_tables.id'))
    referred_table = relationship('app_Table', foreign_keys=[referred_table_id])
    referred_column_id = Column(Integer, ForeignKey('app_columns.id'))
    referred_column = relationship('app_Columns', foreign_keys=[referred_column_id])
    
    primary_join = Column(String)
    secondary_join = Column(String)
    secondary_table = Column(String)
    remote_side = Column(String)
    foreign_keys = Column(String)
    backref = Column(String)
    cascade = Column(String)
    post_update = Column(String)
    cascade_backrefs = Column(String)
    
class app_Indexes(Base):
    __tablename__ = 'app_indexes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unique = Column(Boolean)
    table_id = Column(Integer, ForeignKey('app_tables.id'))
    table = relationship('app_Tables')

class app_Views(Base):
    __tablename__ = 'app_views'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    definition = Column(Text)

class app_Triggers(Base):
    __tablename__ = 'app_triggers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    table_id = Column(Integer, ForeignKey('app_tables.id'))
    timing = Column(String)
    event = Column(String)
    function = Column(String)

class app_Sequences(Base):
    __tablename__ = 'app_sequences'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(Integer)
    increment = Column(Integer)
    
class app_Procedures(Base):
    __tablename__ = 'app_procedures'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    definition = Column(Text)

class app_Functions(Base):
    __tablename__ = 'app_functions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    return_type = Column(String)
    definition = Column(Text)
    
# And that's all she said
"""

API_HEADER ="""
from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_
from sqlalchemy.sql import text

from . import appbuilder, db
from .models import *
"""

VIEW_BODYX ="""
class {0}View(ModelView):# MasterDetailView, MultipleView
    # {1}
    datamodel=SQLAInterface({0}, db.session)
    # To enable Elasticsearch integration, uncomment below
    # search_vector = Text("search_vector", nullable=True)
    add_title = "Add {0}"
    list_title = "List {2}"
    edit_title = "Edit {0}"
    show_title = "Show {0}"
    #add_widget = (FormVerticalWidget|FormInlineWidget)
    show_widget = ShowBlockWidget
    #list_widget = (ListThumbnail|ListWidget)
    #base_order = ("name", "asc")
    search_exclude_columns = person_search_exclude_columns + biometric_columns + person_search_exclude_columns
    # add_exclude_columns = edit_exclude_columns = audit_exclude_columns

    # add_columns = ref_columns + {1} # person_list_columns + ref_columns + contact_columns
    # edit_columns = ref_columns + {1} # person_list_columns + ref_columns + contact_columns
    #edit_exclude_columns = {1} # person_list_columns + ref_columns + contact_columns

    # list_columns = ref_columns + {1} # person_list_columns + ref_columns + contact_columns
    #show_columns = []
    #show_exclude_columns = []
    #search_columns = []
    #search_exclude_columns = []
    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    #related_views =[]
    #show_fieldsets = person_show_fieldset + contact_fieldset
    #edit_fieldsets = add_fieldsets = \
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    #description_columns = {{'name':'your models name column','address':'the address column'}}
    #show_template = "appbuilder/general/model/show_cascade.html"
    #edit_template = "appbuilder/general/model/edit_cascade.html"

    # @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    # def muldelete(self, items):
    #     self.datamodel.delete_all(items)
    #     self.update_redirect()
    #     return redirect(self.get_redirect())

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {{"search_vector": item.search_vector}}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {{"query": {{"match": {{"search_vector": q}}}}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )
"""


VIEW_BODY = """
# class {class_name}Api(ModelRestApi):
#     datamodel = SQLAInterface({class_name})
# 
# appbuilder.add_api({class_name}Api)

class {class_name}ModelView(ModelView):
    datamodel = SQLAInterface({class_name})

    add_title = 'Add {snk_table_name}'
    # add_columns = {tbl_columns}
    # add_exclude_columns = hide_list
    # add_fieldset =  {rt_fld_set}

    list_title= '{snk_table_name} List'
    # list_columns = {tbl_columns}
    # list_exclude_columns = [] # {tbl_columns} #

    edit_title = 'Edit {snk_table_name}'
    # edit_columns = {tbl_columns}
    # edit_fieldset =  {rt_fld_set}
    # edit_exclude_columns = hide_list #

    # show_columns = {tbl_columns}
    # show_fieldset =  {rt_fld_set}
    # show_exclude_columns = hide_list


    # default_sort = [('id', True)]
    # search_columns = {rt_cols} + {tbl_columns}
    # search_exclude_columns = [] # {tbl_columns}
    # base_permissions = ['can_list', 'can_show', 'can_edit', 'can_delete', 'can_add']
#    base_order = ('name', 'asc')
#    base_filters = [['created_by', FilterEqualFunction, get_user],['name', FilterStartsWith, 'a']]
    # label_columns = {lbl_cols}
#   # label_columns=   [{{column.name: column.name for column in table.columns}} ]
#    show_template =  'appbuilder/general/model/show_cascade.html'
#    list_template = 'appbuilder/general/model/list.html'
#    add_template = 'appbuilder/general/model/add.html'
#    edit_template = 'appbuilder/general/model/edit.html'
#    add_widget = (FormVerticalWidget|FormInlineWidget)
#    show_widget = ShowBlockWidget
#    list_widget = (ListThumbnail|ListWidget)
#    list_widget= 'list_widget'
#    edit_template = "tabbed_edit.html"
#    tab_info = {{
#      "basic_info": {{
#           "title": "Basic Information",
#           "fields": {rt_cols}
#            }},
#      "advanced_settings": {{
#           "title": "Advanced Settings",
#           "fields": {tbl_columns}
#            }}
#      }}

#     def prefill_form(self, form, pk):
#        form = super({class_name}ModelView, self).prefill_form(form, pk)
#        self.update_redirect()
#        return form

# For Elasticsearch integration
#     def post_update(self, item):
#         es = Elasticsearch()
#         doc = {{"search_vector": item.search_vector}}
#         es.index(index="my_index", id=item.id, body=doc)
#
#     def post_insert(self, item):
#         self.post_update(item)
#
#     @expose("/search/")
#     def search(self):
#         q = request.args.get("q", "")
#         es = Elasticsearch()
#         search_body = {{"query": {{"match": {{"search_vector": q}}}}}}
#         results = es.search(index="my_index", body=search_body)
#         return self.render_template(
#             "search_results.html",
#             results=results["hits"]["hits"],
#             query=q,
#           )
"""

VIEW_MASTER_DETAIL ="""
class {class_name}{related_class_name}ModelView(MasterDetailView):
    datamodel = SQLAInterface({class_name})
    related_views = [{related_class_name}ModelView]
"""


VIEW_MULTIVIEW = """
class {class_name}MultipleModelView(MultipleView):")
    views = [{related_views}]
"""


CHART_VIEW_BODY = """
class ChartForm(Form):
    table = SelectField('Table', choices=[], validators=[DataRequired()])
    x_axis = SelectField('X Axis', choices=[], validators=[DataRequired()])
    y_axis = SelectField('Y Axis', choices=[], validators=[DataRequired()])
    submit = SubmitField('Draw Chart')

class ChartView(SimpleFormView):
    form = ChartForm
    form_title = 'Draw Chart'
    template = 'chart_view.html'

    def form_get(self, form):
        tables = {tbls}
        form.table.choices = tables

    def form_post(self, form):
        table_name = form.table.data
        x_axis = form.x_axis.data
        y_axis = form.y_axis.data
        table = metadata.tables[table_name]
        # Add your chart drawing logic here

        flash(f'Drawing chart for table', 'info')

"""



VIEW_REG_HEADER = """

# How to create a MasterDetailView

#class DetailView(ModelView):
#    datamodel = SQLAInterface(DetailTable, db.session)

#class MasterView(MasterDetailView):
#    datamodel = SQLAInterface(MasterTable, db.session)
#    related_views = [DetailView]


# How to create a MultipleView
#class MultipleViewsExp(MultipleView):
#    views = [GroupModelView, ContactModelView]

#View Registration
db.create_all()
fill_gender()
"""

#TODO Change to this view using the included example (chatgpt)
VIEW_MASTER_DETAILX ="""

# Based on FK between: {pjoin}
class {class_name}{detail_class_name}View(MasterDetailView):
    datamodel = SQLAInterface({class_name})
    related_views = [{detail_class_name}ModelView]

appbuilder.add_view({class_name}{detail_class_name}View(), "{class_name}_{detail_class_name} Review", icon="fa-folder-open-o", category="{class_name}")
"""

# class {detail_class_name}DetailModelView(ModelView):
#     datamodel = SQLAInterface({detail_class_name})
#     show = "detail"
#
#
# class {class_name}MasterView(MasterDetailView):
#     datamodel = SQLAInterface({class_name})
#     related_views = [{detail_class_name}DetailModelView]

# {class_name}_master_view = {class_name}MasterView()
# {detail_class_name}_detail_view = {detail_class_name}DetailModelView()
# {class_name}_master_detail_view = MasterDetailView(master={class_name}_master_view, detail={detail_class_name}_detail_view)




VIEW_MASTER_DETAILY = """
class {0}{1}DetailView(ModelView):
    datamodel = SQLAInterface({1}, db.session)
    show = 'detail'

class {0}{1}MasterView(MasterDetailView):
    datamodel = SQLAInterface({0}, db.session)
    related_views = [{0}{1}DetailView]

#appbuilder.add_view({0}{1}MasterView(), "{0}-{1}", icon="fa-folder-open-o", category="Master Detail", category_icon = "fa-envelope")
"""


VIEW_FILE_FOOTER = """
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
"""

API_BODY = """
# API
class {0}ModelApi(ModelRestApi):
    # {1}
    resource_name = '{3}'
    datamodel = SQLAInterface({0})
    add_title = "Add {0}"
    list_title = "List {2}"
    edit_title = "Edit {0}"
    show_title = "Show {0}"
    #base_order = ("name", "asc")
    # search_exclude_columns = person_search_exclude_columns + biometric_columns + person_search_exclude_columns
    # add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # add_columns = {1} # person_list_columns + ref_columns + contact_columns
    # edit_columns = {1} # person_list_columns + ref_columns + contact_columns
    #edit_exclude_columns = {1} # person_list_columns + ref_columns + contact_columns
    # list_columns = {1} # person_list_columns + ref_columns + contact_columns
    #show_columns = []
    #show_exclude_columns = []
    #search_columns = []
    #search_exclude_columns = []
    #related_views =[]
    #show_fieldsets = person_show_fieldset + contact_fieldset
    #edit_fieldsets = add_fieldsets = \
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    #description_columns = {{'name':'your models name column','address':'the address column'}}
    # Allowed order columns
    page_size = 20
    # Use this property to change default page size
    # max_page_size = -1 # : Optional[int] = None
    # class override for the FAB_API_MAX_SIZE, use special -1 to allow for any page size
    # description_columns= [] #: Optional[Dict[str, str]] = None
    #
    #     Dictionary with column descriptions that will be shown on the forms::
    #
    #         class MyView(ModelView):
    #             datamodel = SQLAModel(MyTable, db.session)
    #
    #             description_columns = {{'name':'your models name column',
    #                                     'address':'the address column'}}
    #
    # validators_columns: Optional[Dict[str, Callable]] = None
    #  Dictionary to add your own marshmallow validators

    # add_query_rel_fields = None
    #
    #     Add Customized query for related add fields.
    #     Assign a dictionary where the keys are the column names of
    #     the related models to filter, the value for each key, is a list of lists with the
    #     same format as base_filter
    #     {{'relation col name':[['Related model col',FilterClass,'Filter Value'],...],...}}
    #     Add a custom filter to form related fields::
    #
    #         class ContactModelView(ModelRestApi):
    #             datamodel = SQLAModel(Contact)
    #             add_query_rel_fields = {{'group':[['name',FilterStartsWith,'W']]}}
    #
    #
    # edit_query_rel_fields = None
    #
    #     Add Customized query for related edit fields.
    #     Assign a dictionary where the keys are the column names of
    #     the related models to filter, the value for each key, is a list of lists with the
    #     same format as base_filter
    #     {{'relation col name':[['Related model col',FilterClass,'Filter Value'],...],...}}
    #     Add a custom filter to form related fields::
    #
    #         class ContactModelView(ModelRestApi):
    #             datamodel = SQLAModel(Contact, db.session)
    #             edit_query_rel_fields = {{'group':[['name',FilterStartsWith,'W']]}}
    #
    #
    # order_rel_fields = None
    #
    #     Impose order on related fields.
    #     assign a dictionary where the keys are the related column names::
    #
    #         class ContactModelView(ModelRestApi):
    #             datamodel = SQLAModel(Contact)
    #             order_rel_fields = {{
    #                 'group': ('name', 'asc')
    #                 'gender': ('name', 'asc')
    #             }}
    #
    # list_model_schema = [] # : Optional[Schema] = None
    #  Override to provide your own marshmallow Schema for JSON to SQLA dumps
    # add_model_schema: Optional[Schema] = None
    #  Override to provide your own marshmallow Schema for JSON to SQLA dumps
    # edit_model_schema: Optional[Schema] = None
    #  Override to provide your own marshmallow Schema for JSON to SQLA dumps
    # show_model_schema: Optional[Schema] = None
    #  Override to provide your own marshmallow Schema for JSON to SQLA dumps
    # model2schemaconverter = Model2SchemaConverter
    #  Override to use your own Model2SchemaConverter (inherit from BaseModel2SchemaConverter)
"""

MODEL_EXT = """
    ## Example stuff you can add to a table
    # def __repr__(self):
    #     return self.name
    #
    # def month_year(self):
    #     date = self.birthday or mindate
    #     return datetime.datetime(date.year, date.month, 1) or mindate
    #
    # def year(self):
    #     date = self.birthday or mindate
    #     return datetime.datetime(date.year, 1, 1)
    #
    # @hybrid_property
    # def length(self):
    #     return self.end - self.start
    #
    # @hybrid_method
    # def contains(self, point):
    #     return (self.start <= point) & (point <= self.end)
    #
    #
    # @hybrid_method
    # def intersects(self, other):
    #     return self.contains(other.start) | self.contains(other.end)
"""

def gen_gql_header():

    GQL_HEADER = """
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay

from flask_appbuilder.security.sqla.models import User, Role, Permission, PermissionView, RegisterUser
from .models import *
"""
    return DOC_HEADER + GQL_HEADER # + MODEL_HEADER

GQL_IMPORT = "from .models import {0} as {0}Model"

GQL_SEC_IMPORT = "from flask_appbuilder.security.sqla.models import {0} as {0}Model"


# https://github.com/graphql-python/graphene-sqlalchemy
def gen_gql_class(table):
    GQL_CLASS = f"""
class {table}Gql(SQLAlchemyObjectType):
    class Meta:
        model = {table}
        interfaces = (relay.Node, )
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
        
"""
    return GQL_CLASS

GQL_QUERY_HDR = f"""
class Query(graphene.ObjectType):
    node = relay.Node.Field()"""

def gen_gql_query(table):
    GQL_QUERY=f"""    # Allows sorting over multiple {snake_to_pascal(table)}columns, by default over the primary key
    all_{table.lower()} = SQLAlchemyConnectionField({snake_to_pascal(table)}Gql.connection) #sort={snake_to_pascal(table)}Gql.sort_argument())"""
    return GQL_QUERY

GQL_FOOTER = f"""
schema = graphene.Schema(query=Query)
"""


VIEW_SCHEMA_CODE = """
class VuerdView(BaseView):
    default_view = 'vuerd'

    @expose('/vuerd/')
    def vuerd(self):
        return self.render_template(
            'v_erd.html'
        )

class SchemaView(BaseView):
    default_view = 'schema'

    def get_foreign_keys(self, table):
        return [fk for fk in table.foreign_keys]

    def is_association_table(self, table):
        foreign_keys = [c for c in table.columns if c.foreign_keys]
        return len(foreign_keys) == 2 and all([fk.primary_key for fk in foreign_keys])


        #Returns none is a
        #:param table:
        #:param column:
        # :return: Relationship_type, Foreign_table_name, Foreign_table_column
    def get_relationship_type(self, table, column):

        for constraint in table.constraints:
            if isinstance(constraint, ForeignKeyConstraint) and column.name in constraint.columns.keys():
                foreign_table = constraint.elements[0].column.table
                if self.is_association_table(table):
                    return "Many-to-Many", foreign_table.name, constraint.elements[0].column
                return (
                    "One-to-Many" if foreign_table != table else "One-to-One",
                    foreign_table.name,constraint.elements[0].column
                )
        return None, None, None

    @expose('/schema/')
    def schema(self):
        tables = []
        relationships = []

        for table_name, table in metadata.tables.items():
            columns = [{'name': col.name, 'type': str(col.type)} for col in table.columns]
            tables.append({'id': hash(table_name), 'name': table_name, 'columns': columns})

            foreign_keys = self.get_foreign_keys(table)
            for col in table.columns:
                rel_type, fk_table, fk_col = self.get_relationship_type(table, col)
                if rel_type is None:
                    continue
                else:
                    from_id = hash(table_name)
                    to_table = hash(fk_table)
                    to_id = hash(fk_col)
                    relationships.append({
                        'from': table_name,
                        'to': fk_col.name,
                        'fk_table': fk_table,
                        'type': rel_type.lower()
                    })

        s = self.render_template('schema_view.html', schema={'tables': tables, 'relationships': relationships})
        # print(s)
        return s
"""

AFRICAN_LANGS = {
    "af": {"flag": "za", "name": "Afrikaans"},
    "ak": {"flag": "gh", "name": "Akan"},
    "am": {"flag": "et", "name": "Amharic"},
    "amf": {"flag": "ng", "name": "Defaka"},
    "ar": {"flag": "eg", "name": "Arabic"},
    "ber": {"flag": "ma", "name": "Berber"},
    "bez": {"flag": "tz", "name": "Bena"},
    "bm": {"flag": "ml", "name": "Bambara"},
    "byn": {"flag": "er", "name": "Blin"},
    "cgg": {"flag": "ug", "name": "Chiga"},
    "dav": {"flag": "ke", "name": "Dawida"},
    "dua": {"flag": "cm", "name": "Duala"},
    "en": {"flag": "gb", "name": "English"},
    "ff": {"flag": "sn", "name": "Fula"},
    "gu": {"flag": "mu", "name": "Gujarati"},
    "ha": {"flag": "ng", "name": "Hausa"},
    "hdy": {"flag": "dj", "name": "Hadiyya"},
    "ja": {"flag": "ma", "name": "Japanese"},
    "jgo": {"flag": "cm", "name": "Ngomba"},
    "jv": {"flag": "id", "name": "Javanese"},
    "kab": {"flag": "dz", "name": "Kabyle"},
    "kam": {"flag": "ke", "name": "Kamba"},
    "khm": {"flag": "kh", "name": "Khmer"},
    "ki": {"flag": "ke", "name": "Kikuyu"},
    "kik": {"flag": "ke", "name": "Kikuyu"},
    "kin": {"flag": "cd", "name": "Kinyarwanda"},
    "kir": {"flag": "km", "name": "Kyrgyz"},
    "kln": {"flag": "ke", "name": "Kalenjin"},
    "kmb": {"flag": "ao", "name": "Kimbundu"},
    "kok": {"flag": "in", "name": "Konkani"},
    "kua": {"flag": "cd", "name": "Kuanyama"},
    "kwi": {"flag": "sd", "name": "KiKongo"},
    "lg": {"flag": "ug", "name": "Ganda"},
    "ln": {"flag": "cd", "name": "Lingala"},
    "lu": {"flag": "cd", "name": "Luba-Katanga"},
    "lua": {"flag": "cd", "name": "Luba-Lulua"},
    "luo": {"flag": "ke", "name": "Luo"},
    "luy": {"flag": "ke", "name": "Luhya"},
    "mas": {"flag": "ke", "name": "Masai"},
    "mer": {"flag": "ke", "name": "Meru"},
    "mfe": {"flag": "mu", "name": "Morisyen"},
    "mg": {"flag": "mg", "name": "Malagasy"},
    "mgh": {"flag": "mz", "name": "Makhuwa-Meetto"},
    "mne": {"flag": "ne", "name": "Mandinka"},
    "mos": {"flag": "bf", "name": "Mossi"},
    "mr": {"flag": "mu", "name": "Marathi"},
    "nd": {"flag": "zw", "name": "Northern Ndebele"},
    "nmg": {"flag": "cm", "name": "Ngumba"},
    "nnh": {"flag": "cm", "name": "Ngiemboon"},
    "nso": {"flag": "za", "name": "Sesotho sa Leboa"},
    "nus": {"flag": "sd", "name": "Nuer"},
    "ny": {"flag": "mw", "name": "Chichewa"},
    "om": {"flag": "et", "name": "Oromo"},
    "omq": {"flag": "ng", "name": "Oromo (West-Central)"},
    "or": {"flag": "et", "name": "Oromo"},
    "pa": {"flag": "za", "name": "Punjabi"},
    "rn": {"flag": "bi", "name": "Kirundi"},
    "rof": {"flag": "tz", "name": "Rombo"},
    "rw": {"flag": "rw", "name": "Kinyarwanda"},
    "rwk": {"flag": "tz", "name": "Rwa"},
    "shi": {"flag": "ma", "name": "Tachelhit"},
    "sn": {"flag": "zw", "name": "Shona"},
    "so": {"flag": "so", "name": "Somali"},
    "soq": {"flag": "bi", "name": "Kanuri"},
    "sot": {"flag": "za", "name": "Southern Sotho"},
    "ss": {"flag": "sz", "name": "Swati"},
    "ssy": {"flag": "er", "name": "Saho"},
    "sw": {"flag": "ke", "name": "Swahili"},
    "swc": {"flag": "cd", "name": "Congo Swahili"},
    "ta": {"flag": "mu", "name": "Tamil"},
    "tg": {"flag": "tj", "name": "Tajik"},
    "ti": {"flag": "er", "name": "Tigrinya"},
    "tn": {"flag": "za", "name": "Tswana"},
    "ts": {"flag": "za", "name": "Tsonga"},
    "tsi": {"flag": "za", "name": "Tshwa"},
    "tum": {"flag": "mw", "name": "Tumbuka"},
    "tzm": {"flag": "ma", "name": "Central Atlas Tamazight"},
    "ve": {"flag": "za", "name": "Venda"},
    "vun": {"flag": "tz", "name": "Vunjo"},
    "wol": {"flag": "sn", "name": "Wolof"},
    "xho": {"flag": "za", "name": "Xhosa"},
    "xog": {"flag": "ug", "name": "Soga"},
    "yao": {"flag": "mz", "name": "Yao"},
    "yav": {"flag": "cm", "name": "Yangben"},
    'hw': {'flag':'ng', 'name':'Hausa'},
    'ig': {'flag':'ng', 'name':'Igbo'},
    'yo': {'flag':'ng', 'name':'Yoruba'}
}


GEONAME_MODELS = """
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

Base = Model

class Geoname(Base):
    __tablename__ = 'geonames'

    geonameid = Column(Integer, primary_key=True)
    name = Column(String(200))
    asciiname = Column(String(200))
    alternatenames = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    fclass = Column(String(1))
    fcode = Column(String(10))
    country = Column(String(2))
    cc2 = Column(String(600))
    admin1 = Column(String(20))
    admin2 = Column(String(80))
    admin3 = Column(String(20))
    admin4 = Column(String(20))
    population = Column(Integer)
    elevation = Column(Integer)
    gtopo30 = Column(Integer)
    timezone = Column(String(40))
    moddate = Column(Date)
    the_geom = Column(Geometry(geometry_type='POINT', srid=4326))

class Alternatename(Base):
    __tablename__ = 'geonames_alternatename'

    alternatenameId = Column(Integer, primary_key=True)
    geonameid = Column(Integer, ForeignKey('geoname.geonameid'))
    isoLanguage = Column(String(7))
    alternateName = Column(String(200))
    isPreferredName = Column(Boolean)
    isShortName = Column(Boolean)
    isColloquial = Column(Boolean)
    isHistoric = Column(Boolean)

    geoname = relationship('Geoname', backref='alternatenames')

class CountryInfo(Base):
    __tablename__ = 'geonames_countryinfo'

    iso_alpha2 = Column(String(2), primary_key=True)
    iso_alpha3 = Column(String(3))
    iso_numeric = Column(Integer)
    fips_code = Column(String(3))
    name = Column(String(200))
    capital = Column(String(200))
    areainsqkm = Column(Float)
    population = Column(Integer)
    continent = Column(String(2))
    tld = Column(String(10))
    currencycode = Column(String(3))
    currencyname = Column(String(20))
    phone = Column(String(20))
    postalcode = Column(String(100))
    postalcoderegex = Column(String(200))
    languages = Column(String(200))
    geonameId = Column(Integer, ForeignKey('geoname.geonameid'))
    neighbors = Column(String(50))
    equivfipscode = Column(String(3))

    geoname = relationship('Geoname', uselist=False, backref='countryinfo')


"""

GEONAME_VIEWS = """
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Geoname, Alternatename, CountryInfo

class GeonameModelView(ModelView):
    datamodel = SQLAInterface(Geoname)
    list_columns = ['geonameid', 'name', 'asciiname', 'latitude', 'longitude', 'fclass', 'fcode', 'country']
    show_columns = list_columns
    edit_columns = list_columns
    add_columns = list_columns
    search_columns = ['geonameid', 'name', 'asciiname', 'country']

class AlternatenameModelView(ModelView):
    datamodel = SQLAInterface(Alternatename)
    list_columns = ['alternatenameId', 'geoname', 'isoLanguage', 'alternateName', 'isPreferredName']
    show_columns = list_columns
    edit_columns = list_columns
    add_columns = list_columns
    search_columns = ['geoname', 'isoLanguage', 'alternateName']

class CountryInfoModelView(ModelView):
    datamodel = SQLAInterface(CountryInfo)
    list_columns = ['iso_alpha2', 'name', 'capital', 'population', 'continent']
    show_columns = list_columns
    edit_columns = list_columns
    add_columns = list_columns
    search_columns = ['iso_alpha2', 'name', 'capital', 'continent']

def init_views(appbuilder):
    appbuilder.add_view(GeonameModelView, "Geonames", icon="fa-globe", category="Geonames")
    appbuilder.add_view(AlternatenameModelView, "Alternate Names", icon="fa-language", category="Geonames")
    appbuilder.add_view(CountryInfoModelView, "Country Info", icon="fa-flag", category="Geonames")

"""

GEONAME_LOADER = """
import os
import csv
from .models import Geoname, Alternatename, CountryInfo
from . import db

def load_data():
    # Load Geoname data
    geoname_file = 'path/to/allCountries.txt'
    if not db.session.query(Geoname).first():
        with open(geoname_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                geoname = Geoname(
                    geonameid=int(row[0]),
                    name=row[1],
                    asciiname=row[2],
                    alternatenames=row[3],
                    latitude=float(row[4]),
                    longitude=float(row[5]),
                    fclass=row[6],
                    fcode=row[7],
                    country=row[8],
                    cc2=row[9],
                    admin1=row[10],
                    admin2=row[11],
                    admin3=row[12],
                    admin4=row[13],
                    population=int(row[14]),
                    elevation=int(row[15]),
                    gtopo30=int(row[16]),
                    timezone=row[17],
                    moddate=row[18]
                )
                db.session.add(geoname)
            db.session.commit()

    # Load Alternatename data
    alternatename_file = 'path/to/alternateNames.txt'
    if not db.session.query(Alternatename).first():
        with open(alternatename_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                alternatename = Alternatename(
                    alternatenameId=int(row[0]),
                    geonameid=int(row[1]),
                    isoLanguage=row[2],
                    alternateName=row[3],
                    isPreferredName=row[4],
                    isShortName=row[5],
                    isColloquial=row[6],
                    isHistoric=row[7]
                )
                db.session.add(alternatename)
            db.session.commit()

    # Load CountryInfo data
    countryinfo_file = 'path/to/countryInfo.txt'
    if not db.session.query(CountryInfo).first():
        with open(countryinfo_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                countryinfo = CountryInfo(
                    iso_alpha2=row[0],
                    iso_alpha3=row[1],
                    iso_numeric=int(row[2]),
                    fips_code=row[3],
                    name=row[4],
                    capital=row[5],
                    areainsqkm=float(row[6]),
                    population=int(row[7]),
                    continent=row[8],
                    tld=row[9],
                    currencycode=row[10],
                    currencyname=row[11],
                    phone=row[12],
                    postalcode=row[13],
                    postalcoderegex=row[14],
                    languages=row[15],
                    geonameId=int(row[16]),
                    neighbors=row[17],
                    equivfipscode=row[18]
                )
                db.session.add(countryinfo)
            db.session.commit()

"""
