# TODO: Process _img fields in views to make them uploadable
# Conventions: PostgreSQL Database
#   - id fields should always be in id serial
#   - Foreign Keys should ALWAYS end in _id_fk
#   - association tables should end in _link, _map or _assoc
#   - Timestamps always default to func.now(), change generated code manually
#
from sqlalchemy import Enum
from sqlalchemy import create_engine, inspect, MetaData
import inflect
p = inflect.engine()

from db_utils  import *
import headers
from utils import *

## Globals
# DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'
DATABASE_URI = "postgresql:///wakala"
OUTPUT_MODELS_FILE = 'models.py'
OUTPUT_VIEWS_FILE = 'views.py'


def gen_models(metadata, inspector):
    with open("models.py", "w") as f:
        enum_names = []  # To keep track of enums so that we don't repeat
        graph = {}
        # Write the models.py header file first
        f.write(headers.MODEL_HEADER)

        cnam = []  # Temporary holder for a tables column names

        # Generate Enums first
        for t in metadata.sorted_tables:
            table = t.name
            cols = inspector.get_columns(table)
            for col in cols:
                if isinstance(col["type"], Enum):
                    enum_vals = list(col["type"].enums)
                    # enum_name = f"{table}{col['name'].capitalize()}Enum"
                    enum_name = f"{col['name'].capitalize()}"

                    if enum_name not in enum_names:
                        f.write(f"class {enum_name}(enum.Enum):\n")
                        for en_val in enum_vals:
                            f.write(f"   {en_val.upper()} = '{en_val}'\n")
                    enum_names.append(enum_name)
                    f.write("\n\n")

        # Now generate Models
        for t in metadata.sorted_tables:
            table = t.name
            column_names_list = []
            cols = inspector.get_columns(table)
            pks = inspector.get_pk_constraint(table)
            fks = inspector.get_foreign_keys(table)
            uqs = inspector.get_unique_constraints(table)
            cck = inspector.get_check_constraints(table)
            t_comment = inspector.get_table_comment(table)  # Table Comment

            table_class = snake_to_pascal(table)
            # print(table_class)
            f.write(f"class {table_class}(Model):\n")
            f.write(f'    __tablename__ = "{table}"\n\n')
            if t_comment['text']:
                f.write(f'    __doc__ = "{t_comment["text"]}"\n')  # Use the table comment in the docstring
            # Put check constraints
            # __table_args__ = ( )

            for col in cols:
                # String parts to compose a column definition
                # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedColumn
                c_pk = ""
                c_fk = ""
                c_autoincrement = ""
                c_comment = ""
                c_computed = ""
                c_default = ""
                c_dialect_options = ""
                c_identity = ""
                c_column_name = ""
                c_nullable = ""
                c_type = ""
                c_unique = ""
                c_ck = ""  # Check constraints
                column_names_list.append(col["name"])

                # check if the column is an enum type
                if isinstance(col["type"], Enum):
                    enum_vals = list(col["type"].enums)
                    # enum_name = f"{table}{col['name'].capitalize()}Enum"
                    enum_name = f"{col['name'].capitalize()}"
                    f.write(
                        f"    {col['name']} = Column(Enum({enum_name}), name='t_{col['name']}', nullable=False)\n"
                    )
                else:
                    ctype = col["type"].compile()
                    ctype = map_pgsql_datatypes(ctype.lower())

                    # First Primary Keys
                    if col["name"] in pks["constrained_columns"]:
                        c_pk = ", primary_key=True"

                    # The Foreign Keys
                    for index, fk in enumerate(fks):
                        if col['name'] == fk["constrained_columns"][0]:
                            # print(col['name'])
                            fkname = fk["name"]
                            referred_table = fk["referred_table"]
                            fktable = snake_to_pascal(referred_table)
                            fkref = fk["referred_columns"][0]
                            fkcol = fk["constrained_columns"][0]
                            pjoin = snake_to_pascal(table) + '.' + fkcol + ' == ' + fktable + '.' + fkref
                            fkey = fk["referred_table"] + "." + fk["referred_columns"][0]

                            # Is this a self-referential column
                            if table == referred_table:  # means it is self-referential
                                c_pk = ""
                                c_fk = f", ForeignKey('{fkey}')"
                            else:
                                c_fk = f", ForeignKey('{fkey}')"
                            break

                    # The Unique Keys
                    if col["name"] in [uq["column_names"] for uq in uqs]:
                        c_unique = ", unique=True"

                    # Finally all the fields from the ReflectedColumn Dictionary
                    if col['nullable'] == True:
                        c_nullable = ", nullable=True"
                    else:
                        c_nullable = ""  # default behaviour is nullable

                    if col['autoincrement'] == True:
                        c_autoincrement = ", autoincrement=True"

                    if col["comment"] != None:
                        c_comment = '\n\t\t, comment="' + col["comment"] + '"'

                    if col['default'] != None:
                        c_default = f", default = {col['default']}"  # Might include sqltext, so we process further
                        if col['default'] == 'false': c_default = ', default=False'
                        elif col['default'] == 'true': c_default = ', default=True'
                        elif col['default'] == 'now()': c_default = ', default=func.now()'
                        elif ":" in col['default']: c_default = '' #, default = ' + col['default'].split(':')[0]
                        elif col['default'].startswith('nextval'):  # Means it is autoincrement and uses a sequence
                            c_autoincrement = ", autoincrement=True"
                            c_default = ""
                        else:
                            c_default =''

                    f.write(
                        f"    {col['name']} = Column({ctype}{c_fk}{c_pk}{c_unique}{c_autoincrement}{c_default}{c_nullable}{c_comment})\n"
                    )

            # Now generate relationships for all fks
            # constrained_columns, options, referred_columns, referred_schema, referred_table
            # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedForeignKeyConstraint
            for fk in fks:
                fkname = fk["name"].split('_id_')[0]
                qsr = ""  # Quote Self Referential Table Name
                fk_ref_table = snake_to_pascal(fk["referred_table"])
                fk_ref_col = fk["referred_columns"][0]
                fkcol = fk["constrained_columns"][0]
                # fkname = fkcol.split("_fk")[0]
                # fkname = fkcol.split("_id")[0]
                pjoin = f", primaryjoin='{snake_to_pascal(table)}.{fkcol} == {fk_ref_table}.{fk_ref_col}'"
                # back_ref = f", backref='{fk_ref_table}{fkname}s'"
                back_ref = f", backref='{table}s_{fkname}'"
                for_keys = f", foreign_keys=[{qsr}{fk_ref_table}.{fk_ref_col}{qsr}]"
                rem_side = ""

                if snake_to_pascal(table) == fk_ref_table:  # We have a self-referential join, so we have to quote the table name
                    qsr = "'"
                    rem_side = f", remote_side=[{fk_ref_col}]"
                    for_keys = f", foreign_keys=[{fkcol}]"

                rel_name = f"{qsr}{fk_ref_table}{qsr}"

                f.write(
                    f"    {fkname} = relationship({rel_name}{back_ref}{pjoin}{rem_side})\n"
                    # f"    {fkname} = relationship({rel_name}{back_ref}{for_keys}{rem_side})\n"
                )
            # Now write table level check constraints
            if len(cck) > 0:
                for cc in cck:
                    constraint_name = cc['name']
                    sql_expression = cc['sqltext']

                    f.write(
                        f"    CheckConstraint('{sql_expression}', name={constraint_name})\n"
                    )
            f.write("\n    def __repr__(self):\n")
            f.write("       return self." + get_display_column(column_names_list) + "\n")
            f.write("\n ### \n\n")


def gen_views_old(metadata, inspector):
    with open('views.py', 'w') as f:
        f.write(headers.VIEW_FILE_HEADER)
        md_views = set()
        for t in metadata.sorted_tables:
            table = t.name
            columns = inspector.get_columns(table)
            fks = inspector.get_foreign_keys(table)
            all_field_names = []
            # Collect the column and foreign key names
            # all_field_names = [col["name"].lower() for col in columns]
            all_field_names = [col["name"] for col in columns]
            # all_field_names += [fk["name"].lower() for fk in fks]
            all_field_names += [fk["name"] for fk in fks]

            pks = inspector.get_pk_constraint(table)
            class_name = snake_to_pascal(table)
            snk_table_name = snake_to_pascal(table)
            col_names = [col["name"] for col in columns]
            rt_cols = []  # str(RefTypeMixin.mixin_fields())
            rt_fld_set = []  # str(RefTypeMixin.mixin_fieldset())
            # lbl_cols = [utils.snake_to_label(col["name"]) for col in columns]
            # lbl_cols = {['col': utils.snake_to_label(col.split('_id_fke')[0]) for col in all_field_names]}
            lbl_cols = {}
            for col in all_field_names:
                lbl_cols[col.split('_id_fke')[0]] = snake_to_label(col.split('_id_fke')[0])
            # print(lbl_cols)
            tbl_columns = remove_id_columns(all_field_names)

            table_title = snake_to_label(table)
            # print(class_name, col_names)
            # print("\n")

            f.write(headers.VIEW_BODY.format(
                class_name=class_name,
                snk_table_name=snk_table_name,
                tbl_columns=tbl_columns,
                rt_cols=rt_cols,
                rt_fld_set=rt_fld_set,
                lbl_cols=lbl_cols)
            )
            f.write(headers.VIEW_REGY.format(class_name=class_name, table_title=table_title))
        for table in tables:
            columns = inspector.get_columns(table)
            fks = inspector.get_foreign_keys(table)
            detail_class_name = snake_to_pascal(table)
            for fk in fks:
                # print(table, fk)
                fkname = fk["name"]
                fktable = fk["referred_table"]
                fkcol = fk["constrained_columns"][0]
                fkref = fk["referred_columns"][0]
                pjoin = snake_to_pascal(table) + '.' + fkcol + ' == ' + fktable + '.' + fkref
                class_name = snake_to_pascal(fktable)
                mv_name = class_name + detail_class_name + 'View'
                if mv_name not in md_views:
                    f.write(headers.VIEW_MASTER_DETAILX.format(
                        class_name=class_name,
                        detail_class_name=detail_class_name,
                        pjoin=pjoin
                    )
                    )
                    md_views.add(mv_name)
        f.write(headers.VIEW_FILE_FOOTER)
def gen_views(metadata, inspector):
    views = []
    view_regs = []
    views.append(headers.VIEW_HEADER)
    def gen_col_names(table):
        col_names = []
        for col in table.columns:
            if col.name == 'id': continue
            if col.name.endswith('_id_fk'):
                col_names.append(f"'col.name[:-6]'")
                continue
            col_names.append(f"'{col.name}'")
        c = ', '.join(col_names)
        return c

    # Generate ModelViews for all tables
    for table in metadata.sorted_tables:
        model_name = snake_to_pascal(table.name) #.capitalize()
        if model_name.lower().startswith('ab_'):
            continue
        views.append(f'class {model_name}ModelView(ModelView):')
        views.append(f'    datamodel = SQLAInterface({model_name})')
        c = gen_col_names(table)
        views.append(f'#    list_columns = [{c}]')

        views.append('')
        # view_regs.append(
        views.append(
                f'appbuilder.add_view({model_name}ModelView, "{p.plural(model_name)}", icon="fa-folder-open-o", category="Setup")')

    # Generate MasterDetailView for tables with foreign keys
    for table in metadata.sorted_tables:
        mviews = set()
        for fk in table.foreign_keys:
            parent_table = fk.column.table.name
            parent_model_name = snake_to_pascal(parent_table) #.capitalize()
            child_model_name = snake_to_pascal(fk.parent.table.name) #.capitalize()
            detail_view_name = f'{child_model_name}ModelView'

            # Generate a unique master-detail view class name
            master_detail_view_name = f'{parent_model_name}_{child_model_name}MasterDetailView'
            if master_detail_view_name not in mviews:
                views.append(f'class {master_detail_view_name}(MasterDetailView):')
                views.append(f'    datamodel = SQLAInterface({parent_model_name})')
                views.append(f'    related_views = [{detail_view_name}]')
                views.append(f"    show_template = 'appbuilder/general/model/show_cascade.html'")
                views.append('')
                # view_regs.append(
                views.append(
                f'appbuilder.add_view({master_detail_view_name}, "{p.plural(parent_model_name)}", icon="fa-folder-open-o", category="Review")')
                mviews.add(master_detail_view_name)

    # Generate MultipleViews for tables that have multiple Foreign Keys
    mviews = set()
    for table in metadata.sorted_tables:
        related_views = set()
        child_model_name = snake_to_pascal(table.name)
        for fk in table.foreign_keys:
            parent_table = fk.column.table.name
            parent_model_name = snake_to_pascal(parent_table)
            # child_model_name = fk.parent.table.name.capitalize()
            detail_view_name = f'{parent_model_name}ModelView'
            related_views.add(detail_view_name)

        # If there are multiple foreign keys, create a MultipleView
        if len(related_views) > 1:
            multiple_view_name = f'{parent_model_name}MultipleView'
            if multiple_view_name not in mviews:
                views.append(f'class {multiple_view_name}(MultipleView):')
                views.append(f'    datamodel = SQLAInterface({parent_model_name})')
                views.append(f'    views = [{", ".join(related_views)}]')
                views.append('')
                # view_regs.append(
                views.append(
                f'appbuilder.add_view({multiple_view_name}, "{p.plural(parent_model_name)}", icon="fa-folder-open-o", category="Inspect")')
                mviews.add(multiple_view_name)

    # views.extend(view_regs)
    views.append(headers.VIEW_FILE_FOOTER)
    return views


if __name__ == '__main__':
    engine = create_engine(DATABASE_URI)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)

    tables = inspector.get_table_names()
    mtbl = inspector.get_multi_columns()  # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.reflection.Inspector.get_multi_columns

    gen_models(metadata, inspector)
    v = gen_views(metadata, inspector)
    write_file('views.py', v)