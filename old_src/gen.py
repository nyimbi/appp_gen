from sqlalchemy import create_engine, MetaData, inspect

# Configuration
# DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'
DATABASE_URI = 'postgresql:///wakala'
OUTPUT_MODELS_FILE = 'models.py'
OUTPUT_VIEWS_FILE = 'views.py'
OUTPUT_API_FILE = 'api.py'

def gen_models1(metadata, output_file=OUTPUT_MODELS_FILE):
    with open(output_file, 'w') as models_file:
        models_file.write('from flask_appbuilder import Model\n')
        models_file.write('from sqlalchemy import Column, Integer, String, ForeignKey\n')
        models_file.write('from sqlalchemy.orm import relationship\n\n')

        for table in metadata.sorted_tables:
            model_name = table.name.capitalize()
            models_file.write(f'class {model_name}(Model):\n')
            models_file.write(f'    __tablename__ = "{table.name}"\n')

            for column in table.columns:
                column_type = str(column.type)
                if column.foreign_keys:
                    fk = next(iter(column.foreign_keys))
                    models_file.write(f'    {column.name} = Column({column_type}, ForeignKey("{fk.target_fullname}"))\n')
                else:
                    models_file.write(f'    {column.name} = Column({column_type})\n')
                    # Write relationships

            for fk in table.foreign_key_constraints:
                referred_table = fk.referred_table.name.capitalize()
                constraint_name = fk.name if fk.name else f"{table.name}_to_{referred_table}"
                models_file.write(f'    {constraint_name} = relationship("{referred_table}")\n')

            models_file.write('\n')

    print(f'Models written to {output_file}')

def gen_models2(metadata, output_file=OUTPUT_MODELS_FILE):
    with open(output_file, 'w') as models_file:
        models_file.write('from flask_appbuilder import Model\n')
        models_file.write('from sqlalchemy import Column, Integer, String, ForeignKey\n')
        models_file.write('from sqlalchemy.orm import relationship\n\n')

        for table in metadata.sorted_tables:
            model_name = table.name.capitalize()
            models_file.write(f'class {model_name}(Model):\n')
            models_file.write(f'    __tablename__ = "{table.name}"\n')

            # Write columns with constraints
            for column in table.columns:
                column_type = str(column.type)
                column_args = []
                column_kwargs = {}

                # Check for primary key
                if column.primary_key:
                    column_kwargs['primary_key'] = True

                # Check for nullable
                if not column.nullable:
                    column_kwargs['nullable'] = False

                # Check for unique constraint
                if column.unique:
                    column_kwargs['unique'] = True

                # Combine column arguments and keyword arguments
                column_args_str = ', '.join(column_args)
                column_kwargs_str = ', '.join(f'{key}={value}' for key, value in column_kwargs.items())
                column_params_str = ', '.join(filter(None, [column_args_str, column_kwargs_str]))

                # Define the column
                models_file.write(f'    {column.name} = Column({column_type}, {column_params_str})\n')

            # # Write relationships after columns
            # for fk in table.foreign_keys:
            #     parent_table = fk.column.table.name
            #     parent_model_name = parent_table.capitalize()
            #     child_model_name = fk.parent.table.name
            #     relationship_name = f'{parent_model_name}_{child_model_name}'.lower()
            #     models_file.write(f'    {relationship_name} = relationship("{parent_model_name}")\n')

            # Write relationships after columns
            relationships = {}
            for fk in table.foreign_keys:
                parent_table = fk.column.table.name
                parent_model_name = parent_table.capitalize()
                child_model_name = fk.parent.table.name
                relationship_name = f'{parent_model_name}_{child_model_name}'.lower()

                # Check for self-referential relationship
                if parent_table == table.name:
                    models_file.write(f'    {relationship_name} = relationship("{parent_model_name}", '
                                      f'remote_side=[id], backref="subordinates")\n')
                else:
                    # Check for multiple foreign keys to the same table
                    if parent_table not in relationships:
                        relationships[parent_table] = []
                    relationships[parent_table].append(relationship_name)
                    models_file.write(f'    {relationship_name} = relationship("{parent_model_name}", '
                                      f'backref="{relationship_name}")\n')

            # Ensure unique backrefs for multiple foreign keys to the same table
            for parent_table, rel_names in relationships.items():
                if len(rel_names) > 1:
                    for i, rel_name in enumerate(rel_names, start=1):
                        models_file.write(f'    {rel_name}.prop.backref = "{rel_name}{i}"\n')

            models_file.write('\n')

    print(f'Models written to {output_file}')

def gen_models(metadata, output_file=OUTPUT_MODELS_FILE):
    with open(output_file, 'w') as models_file:
        models_file.write('from flask_appbuilder import Model\n')
        models_file.write('from sqlalchemy import Column, Integer, String, ForeignKey\n')
        models_file.write('from sqlalchemy.orm import relationship\n')
        models_file.write('from sqlalchemy.ext.declarative import declared_attr\n\n')

        for table in metadata.sorted_tables:
            model_name = table.name.capitalize()
            models_file.write(f'class {model_name}(Model):\n')
            models_file.write(f'    __tablename__ = "{table.name}"\n')

            # Write columns with constraints
            for column in table.columns:
                column_type = str(column.type)
                column_args = []
                column_kwargs = {}

                # Check for primary key
                if column.primary_key:
                    column_kwargs['primary_key'] = True

                # Check for nullable
                if not column.nullable:
                    column_kwargs['nullable'] = False

                # Check for unique constraint
                if column.unique:
                    column_kwargs['unique'] = True

                # Check for foreign keys and add relationship
                if column.foreign_keys:
                    fk = next(iter(column.foreign_keys))
                    column_args.append(f'ForeignKey("{fk.target_fullname}")')
                    rel_name = f'{fk.column.table.name}_{column.name}'.lower()
                    models_file.write(f'    @declared_attr\n')
                    models_file.write(f'    def {rel_name}(cls):\n')
                    models_file.write(f'        return relationship("{fk.column.table.name.capitalize()}")\n')

                # Combine column arguments and keyword arguments
                column_args_str = ', '.join(column_args)
                column_kwargs_str = ', '.join(f'{key}={value}' for key, value in column_kwargs.items())
                column_params_str = ', '.join(filter(None, [column_args_str, column_kwargs_str]))

                models_file.write(f'    {column.name} = Column({column_type}, {column_params_str})\n')
                # Write relationships
                for fk in table.foreign_key_constraints:
                    referred_table = fk.referred_table.name.capitalize()
                    constraint_name = fk.name if fk.name else f"{table.name}_to_{referred_table}"
                    models_file.write(f'    {constraint_name} = relationship("{referred_table}")\n')

            models_file.write('\n')

    print(f'Models written to {output_file}')

def gen_views(metadata, output_file=OUTPUT_VIEWS_FILE):
    with open(output_file, 'w') as views_file:
        views_file.write('from flask_appbuilder import ModelView\n')
        views_file.write('from flask_appbuilder.models.sqla.interface import SQLAInterface\n')
        views_file.write('from . import appbuilder, db\n')
        views_file.write('from .models import *\n\n')

        for table in metadata.sorted_tables:
            model_name = table.name.capitalize()
            columns = table.columns
            list_columns = [column.name for column in columns]
            label_columns = {column.name: column.name.capitalize().replace('_', ' ') for column in columns}
            show_fieldsets = [
                (None, {'fields': list_columns})
            ]

            views_file.write(f'class {model_name}View(ModelView):\n')
            views_file.write(f'    datamodel = SQLAInterface({model_name})\n')
            views_file.write(f'    list_columns = {list_columns}\n')
            views_file.write(f'    label_columns = {label_columns}\n')
            views_file.write(f'    show_fieldsets = {show_fieldsets}\n\n')

            views_file.write(f'appbuilder.add_view({model_name}View, "{model_name}", category="Menu")\n\n')

    print(f'Views written to {output_file}')

def gen_api(metadata, output_file=OUTPUT_API_FILE):
    with open(output_file, 'w') as api_file:
        api_file.write('from flask_appbuilder.api import BaseApi, expose\n')
        api_file.write('from flask_appbuilder.models.sqla.interface import SQLAInterface\n')
        api_file.write('from . import appbuilder, db\n')
        api_file.write('from .models import *\n\n')

        for table in metadata.sorted_tables:
            model_name = table.name.capitalize()
            api_file.write(f'class {model_name}RestApi(BaseApi):\n')
            api_file.write(f'    resource_name = "{table.name}"\n')
            api_file.write(f'    datamodel = SQLAInterface({model_name})\n\n')
            api_file.write('    @expose("/", methods=["GET"])\n')
            api_file.write('    def get_list(self):\n')
            api_file.write('        """Get list of records."""\n')
            api_file.write('        return self.list()\n\n')
            api_file.write('    @expose("/<pk>", methods=["GET"])\n')
            api_file.write('    def get_item(self, pk):\n')
            api_file.write('        """Get record by primary key."""\n')
            api_file.write('        return self.show(pk)\n\n')
            api_file.write('    @expose("/", methods=["POST"])\n')
            api_file.write('    def post(self):\n')
            api_file.write('        """Create a new record."""\n')
            api_file.write('        return self.post()\n\n')
            api_file.write('    @expose("/<pk>", methods=["PUT"])\n')
            api_file.write('    def put(self, pk):\n')
            api_file.write('        """Update existing record."""\n')
            api_file.write('        return self.edit(pk)\n\n')
            api_file.write('    @expose("/<pk>", methods=["DELETE"])\n')
            api_file.write('    def delete(self, pk):\n')
            api_file.write('        """Delete record by primary key."""\n')
            api_file.write('        return self.delete(pk)\n\n')

            api_file.write(f'appbuilder.add_api({model_name}RestApi)\n\n')

    print(f'APIs written to {output_file}')

# Connect to the PostgreSQL database
engine = create_engine(DATABASE_URI)
metadata = MetaData()
metadata.reflect(bind=engine)
insp = inspect(engine)

# Generate the files
gen_models2(metadata)
gen_views(metadata)
gen_api(metadata)
