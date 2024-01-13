# refaactored tool to generate flask-appbuilder models and views from a database

import inflect
from sqlalchemy import create_engine, MetaData, inspect, Enum, Identity

from utils import map_pgsql_datatypes
from headers import *

p = inflect.engine()


# Selects the best display name given a list of column names
def get_display_column(column_names):
    priorities = ['name', 'alias', 'title', 'label', 'display_name', 'code']

    for name in priorities:
        if name in column_names:
            return name

    for name in column_names:
        if 'name' in name.lower() or 'model' in name.lower():
            return name

    return column_names[0]

def inspect_metadata(database_uri):
    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)
    return metadata, inspector


def gen_model_header():
    model_header = []
    model_header.append('import datetime, enum')
    model_header.append('from flask_appbuilder import Model')
    model_header.append('from sqlalchemy import Column, Integer, Boolean, String, Float, Enum, ForeignKey, Date, DateTime, Text')
    model_header.append('from sqlalchemy.orm import relationship, backref\n')
    model_header.append(MODEL_HEADER)
    return model_header


def gen_view_header():
    view_header = []
    view_header.append("from flask_appbuilder import ModelView")
    view_header.append("from flask_appbuilder.models.sqla.interface import SQLAInterface")
    view_header.append("from flask_appbuilder.views import MasterDetailView, MultipleView")
    view_header.append('from .models import *\n')
    return view_header


def gen_api_header():
    api_header = []
    api_header.append(f"from flask_appbuilder.api import ModelRestApi, BaseApi, expose, rison")
    api_header.append(f"from flask_appbuilder.models.sqla.interface import SQLAInterface")
    return api_header


def gen_model_enums(metadata, inspector):
    enum_code = []
    enums = inspector.get_enums()
    for en in enums:
        enum_code.append(f"\nclass {en['name']}(enum.Enum):")
        for label in en['labels']:
            enum_code.append(f"   {label.upper()} = '{label}'")
    enum_code.append(' ')
    return enum_code


def gen_models(metadata):
    model = []
    for table in metadata.sorted_tables:
        model_name = table.name.capitalize()
        if model_name.lower().startswith('ab_'):
            continue
        model.append(f'class {model_name}(Model):')
        model.append(f'    __tablename__ = "{table.name}"')

        # Write columns with constraints
        for column in table.columns:
            column_args = []
            column_kwargs = {}
            print(str(column.type).lower())

            column_type = map_pgsql_datatypes(str(column.type).lower())
            if isinstance(column.type, Enum):  # ["type"], Enum):
                enum_name = f"{column.type.name}"  # ['name'].capitalize()}"
                column_type = f"Enum({enum_name})"
                column_kwargs['info'] = '{"marshmallow_enum": {"by_value": False}}'
            column_args.append(f"{column_type}")

            # Check for primary key
            if column.primary_key:
                column_kwargs['primary_key'] = True

            # Check for nullable
            if not column.nullable:
                column_kwargs['nullable'] = False

            # Check for unique constraint
            if column.unique:
                column_kwargs['unique'] = True

            # Check for default value
            # if not isinstance(column.type, Identity): # and column.server_default:
            #     column_kwargs['default'] = column.server_default.arg

            # Check for foreign keys
            for fk in column.foreign_keys:
                column_args.append(f'ForeignKey("{fk.target_fullname}")')

            # Combine column arguments and keyword arguments
            column_args_str = ', '.join(column_args)
            column_kwargs_str = ', '.join(f'{key}={value}' for key, value in column_kwargs.items())
            column_params_str = ', '.join(filter(None, [column_args_str, column_kwargs_str]))

            # Define the column
            # model.append(f'    {column.name} = Column({column_type}, {column_params_str})')
            model.append(f'    {column.name} = Column({column_params_str})')

        # Write relationships after columns
        relationships = {}
        for fk in table.foreign_keys:
            parent_table = fk.column.table.name
            parent_model_name = parent_table.capitalize()
            child_model_name = fk.parent.table.name
            # relationship_name = f'{parent_model_name}_{child_model_name}'.lower()
            # relationship_name = f'{parent_model_name}'.lower()
            # Use the column name of the ForeignKey, strip '_id_fk' if it exists
            fk_column_name = fk.parent.name
            if fk_column_name.lower().endswith('_id_fk'):
                relationship_name = fk_column_name[:-6]  # Remove '_id_fk'
            else:
                relationship_name = fk_column_name

            # Create a proper relationship name by removing '_id' or '_fk' if they exist
            if relationship_name.lower().endswith('_id'):
                relationship_name = relationship_name[:-3]
            elif relationship_name.lower().endswith('_fk'):
                relationship_name = relationship_name[:-3]

            # Check for self-referential relationship
            if parent_table == table.name:
                model.append(f'    {relationship_name} = relationship("{parent_model_name}", '
                             f'remote_side=[id], backref="subordinates")')
            else:
                # Check for multiple foreign keys to the same table
                if parent_table not in relationships:
                    relationships[parent_table] = []
                relationships[parent_table].append(relationship_name)
                model.append(f'    {relationship_name} = relationship("{parent_model_name}", '
                             f'backref="{relationship_name}")')

        # # Ensure unique backrefs for multiple foreign keys to the same table
        # for parent_table, rel_names in relationships.items():
        #     if len(rel_names) > 1:
        #         for i, rel_name in enumerate(rel_names, start=1):
        #             model.append(f'    {rel_name}.prop.backref = "{rel_name}{i}"')

        model.append('\n')

    # print(f'Models written to {output_file}')
    return model


def gen_views(metadata):
    views = []
    view_regs = []

    def gen_col_names(table):
        col_names = []
        for col in table.columns:
            if col.name == 'id': continue
            if col.name.endswith('_id_fk'):
                col_names.append(col.name[:-6])
                continue
            col_names.append(f"'{col.name}'")
        c = ', '.join(col_names)
        return c

    # Generate ModelViews for all tables
    for table in metadata.sorted_tables:
        model_name = table.name.capitalize()
        if model_name.lower().startswith('ab_'):
            continue
        views.append(f'class {model_name}View(ModelView):')
        views.append(f'    datamodel = SQLAInterface({model_name})')
        c = gen_col_names(table)
        views.append(f'    list_columns = [{c}]')


        views.append('')
        view_regs.append(
            f'appbuilder.add_view({model_name}View, "{p.plural(model_name)}", icon="fa-folder-open-o", category="Setup")')

    # Generate MasterDetailView for tables with foreign keys
    for table in metadata.sorted_tables:
        for fk in table.foreign_keys:
            parent_table = fk.column.table.name
            parent_model_name = parent_table.capitalize()
            child_model_name = fk.parent.table.name.capitalize()
            detail_view_name = f'{child_model_name}View'

            # Generate a unique master-detail view class name
            master_detail_view_name = f'{parent_model_name}{child_model_name}MasterDetailView'
            views.append(f'class {master_detail_view_name}(MasterDetailView):')
            views.append(f'    datamodel = SQLAInterface({parent_model_name})')
            views.append(f'    related_views = [{detail_view_name}]')
            views.append(f"    show_template = 'appbuilder/general/model/show_cascade.html'")
            views.append('')
            view_regs.append(
                f'appbuilder.add_view({master_detail_view_name}, "{p.plural(parent_model_name)}", icon="fa-folder-open-o", category="Review")')

    # Generate MultipleViews for tables that have multiple Foreign Keys
    for table in metadata.sorted_tables:
        related_views = set()
        child_model_name = table.name.capitalize()
        for fk in table.foreign_keys:
            parent_table = fk.column.table.name
            parent_model_name = parent_table.capitalize()
            # child_model_name = fk.parent.table.name.capitalize()
            detail_view_name = f'{parent_model_name}View'
            related_views.add(detail_view_name)

        # If there are multiple foreign keys, create a MultipleView
        if len(related_views) > 1:
            multiple_view_name = f'{parent_model_name}MultipleView'
            view_regs.append(
                f'appbuilder.add_view({parent_model_name}, "{p.plural(parent_model_name)}", icon="fa-folder-open-o", category="Inspect")')
            views.append(f'class {multiple_view_name}(MultipleView):')
            views.append(f'    datamodel = SQLAInterface({parent_model_name})')
            views.append(f'    views = [{", ".join(related_views)}]')
            views.append('')

    views.extend(view_regs)
    return views


def gen_api(metadata):
    api_classes = []
    # api_reg = []

    # Generate API classes for all tables
    for table in metadata.sorted_tables:
        model_name = table.name.capitalize()
        api_class_name = f'{model_name}Api'

        api_classes.append(f'class {api_class_name}(ModelRestApi):')
        api_classes.append(f'    resource_name = "{table.name}"')
        api_classes.append(f'    datamodel = SQLAInterface({model_name})')
        api_classes.append('')
        # api_reg.append(f'appbuilder.add_api({api_class_name})')

        # # Define the standard RESTful API methods
        # api_methods = [
        #     ('get_list', 'GET', f'"""Get list of {model_name.lower()} records."""', 'self.list()'),
        #     ('get_item', 'GET', f'"""Get {model_name.lower()} record by primary key."""', 'self.show(pk)'),
        #     ('post', 'POST', f'"""Create a new {model_name.lower()} record."""', 'self.post()'),
        #     ('put', 'PUT', f'"""Update an existing {model_name.lower()} record."""', 'self.edit(pk)'),
        #     ('delete', 'DELETE', f'"""Delete {model_name.lower()} record by primary key."""', 'self.delete(pk)')
        # ]
        #
        # for method_name, http_method, docstring, return_statement in api_methods:
        #     api_classes.append(f'    @expose("/{model_name.lower()}", methods=["{http_method}"])')
        #     if method_name == 'get_item':
        #         api_classes.append(f'    def {method_name}(self, pk):')
        #     else:
        #         api_classes.append(f'    def {method_name}(self):')
        #     api_classes.append(f'        {docstring}')
        #     api_classes.append(f'        return {return_statement}')
        #     api_classes.append('')

        # Add the API class to the Flask-AppBuilder instance
        api_classes.append(f'appbuilder.add_api({api_class_name})')
        api_classes.append('')

    return api_classes


# # Usage example
# DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'
# engine = create_engine(DATABASE_URI)
# metadata = MetaData(bind=engine)
# metadata.reflect()
#
# api_code = gen_api(metadata)
# print("\n".join(api_code))


if __name__ == '__main__':
    md, ip = inspect_metadata('postgresql:///wakala')
    m, n, a = [], [], []

    m.extend(gen_model_header())
    m.extend(gen_model_enums(md, ip))
    m.extend(gen_models(md))
    print('\n'.join(m))
    with open('models.py', 'w') as model_file:
        model_file.write('\n'.join(m))

    n.extend(gen_view_header())
    n.extend(gen_views(md))
    print('\n'.join(n))
    with open('views.py', 'w') as view_file:
        view_file.write('\n'.join(n))

    a.extend(gen_api_header())
    a.extend(gen_api(md))
    print('\n'.join(a))
    with open('api.py', 'w') as api_file:
        api_file.write('\n'.join(a))
