# TODO: Process _img fields in views to make them uploadable
# Conventions: PostgreSQL Database
#   - id fields should always end in _id
#   - association tables should end in _link, _map or _assoc
#   - Timestamps always default to func.now(), change generated code manually
#
from sqlalchemy import Enum
from sqlalchemy import create_engine, inspect, MetaData

import headers
import utils

## Globals
# DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'
DATABASE_URI = "postgresql:///wakala"
OUTPUT_MODELS_FILE = 'models.py'
OUTPUT_VIEWS_FILE = 'views.py'

engine = create_engine(DATABASE_URI)
metadata = MetaData()
metadata.reflect(bind=engine)

inspector = inspect(engine)


# Remove columns that end in _id
def remove_id_columns(column_names):
    cleaned_names = []

    for name in column_names:

        if name.lower().endswith('_id_fkey'):
            # Remove _id_fkey and add
            cleaned_name = name.replace('_id_fkey', '')
            cleaned_names.append(cleaned_name)

        elif not name.endswith('_id'):
            cleaned_names.append(name)

    return cleaned_names


# This checks if a table is an association table
# As Assoc table should only have two FKs
# if we have named to table 'assoc', 'link' or 'map'
# We can have more than those two columns, so blanking out the test for other columns
def is_association_table(table_name):
    # Get the foreign keys for the table
    foreign_keys = inspector.get_foreign_keys(table_name)

    columns = inspector.get_columns(table_name)
    if len(columns) <= 2:
        # Check for a naming convention
        if "assoc" in table_name.lower() or \
                "link" in table_name.lower() or \
                "map" in table_name.lower():
            return True

    # Check the number of foreign keys
    if len(foreign_keys) == 2:
        # Check if the foreign keys reference different tables
        referred_tables = {fk['referred_table'] for fk in foreign_keys}
        if len(referred_tables) == 2:
            return True
            # Check for additional columns
            # columns = inspector.get_columns(table_name)
            # if len(columns) == 2:  # Only the foreign keys
            #     return True

    return False


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


# In order to generate tables in topological sort order
# -  get table dependencies
# - do a Depth First search to get topological order
def get_table_dependencies():
    # Get the table dependencies using SQLAlchemy reflection
    table_dependencies = {}

    for table_name in inspector.get_table_names():
        table_dependencies[table_name] = set()
        foreign_keys = inspector.get_foreign_keys(table_name)
        for fk in foreign_keys:
            ref_table = fk['referred_table']
            table_dependencies[table_name].add(ref_table)

    return table_dependencies


def topological_sort(graph):
    sorted_list = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        sorted_list.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return sorted_list


tables = inspector.get_table_names()
mtbl = inspector.get_multi_columns()  # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.reflection.Inspector.get_multi_columns
table_dependencies = get_table_dependencies()
sorted_tables = topological_sort(table_dependencies)

# Alternative way to get the list of dependency sorted tables
# exp_list = inspector.get_sorted_table_and_fkc_names()
# print(exp_list)
# for tbl_fkc in exp_list:
#     sorted_tables.append(tbl_fkc[0])

with open("models.py", "w") as f:
    enum_names = []  # To keep track of enums so that we don't repeat
    graph = {}
    # Write the models.py header file first
    f.write(headers.MODEL_HEADER)

    cnam = []  # Temporary holder for a tables column names

    # In order to Guarantee successful generation we want to do a topological sort of tables
    table_dependencies = get_table_dependencies()
    sorted_tables = topological_sort(table_dependencies)
    # print(sorted_tables)

    # Generate Enums first
    for table in sorted_tables:
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
    for table in sorted_tables:
        column_names_list = []
        cols = inspector.get_columns(table)
        pks = inspector.get_pk_constraint(table)
        fks = inspector.get_foreign_keys(table)
        uqs = inspector.get_unique_constraints(table)
        cck = inspector.get_check_constraints(table)
        t_comment = inspector.get_table_comment(table)  # Table Comment

        table_class = utils.snake_to_pascal(table)
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
                ctype = utils.map_pgsql_datatypes(ctype.lower())

                # First Primary Keys
                if col["name"] in pks["constrained_columns"]:
                    c_pk = ", primary_key=True"

                # The Foreign Keys
                for index, fk in enumerate(fks):
                    if col['name'] == fk["constrained_columns"][0]:
                        print(col['name'])
                        fkname = fk["name"]
                        referred_table = fk["referred_table"]
                        fktable = utils.snake_to_pascal(referred_table)
                        fkref = fk["referred_columns"][0]
                        fkcol = fk["constrained_columns"][0]
                        pjoin = utils.snake_to_pascal(table) + '.' + fkcol + ' == ' + fktable + '.' + fkref
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

                if col['comment'] != None:
                    c_comment = ', comment="' + col['comment'] + '"'

                if col['default'] != None:
                    c_default = f", default = {col['default']}"  # Might include sqltext, so we process further
                    if col['default'] == 'false': c_default = ', default = False'
                    if col['default'] == 'true': c_default = ', default = True'
                    if col['default'] == 'now()': c_default = ', default = func.now()'
                    if ":" in col['default']: c_default = ', default = ' + col['default'].split(':')[0]

                    if col['default'].startswith('nextval'):  # Means it is autoincrement and uses a sequence
                        c_autoincrement = ", autoincrement=True"
                        c_default = ""

                f.write(
                    f"    {col['name']} = Column({ctype}{c_fk}{c_pk}{c_unique}{c_autoincrement}{c_default}{c_comment})\n"
                )

        # Now generate relationships for all fks
        # constrained_columns, options, referred_columns, referred_schema, referred_table
        # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedForeignKeyConstraint
        for fk in fks:
            fkname = fk["name"].split('_id_')[0]
            qsr = ""  # Quote Self Referential Tasble Name
            fk_ref_table = utils.snake_to_pascal(fk["referred_table"])
            fk_ref_col = fk["referred_columns"][0]
            fkcol = fk["constrained_columns"][0]
            pjoin = f", primaryjoin='{utils.snake_to_pascal(table)}.{fkcol} == {fk_ref_table}.{fk_ref_col}'"
            # back_ref = f", backref='{fk_ref_table}{fkname}s'"
            back_ref = f", backref='{table}s_{fkname}'"
            for_keys = f", foreign_keys=[{qsr}{fk_ref_table}.{fk_ref_col}{qsr}]"
            rem_side = ""

            if utils.snake_to_pascal(
                    table) == fk_ref_table:  # We have a self-referential join, so we have to quote the table name
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

####### Generate views #####

with open('views.py', 'w') as f:
    f.write(headers.VIEW_FILE_HEADER)
    md_views = set()
    for table in sorted_tables:
        columns = inspector.get_columns(table)
        fks = inspector.get_foreign_keys(table)
        all_field_names = []
        # Collect the column and foreign key names
        # all_field_names = [col["name"].lower() for col in columns]
        all_field_names = [col["name"] for col in columns]
        # all_field_names += [fk["name"].lower() for fk in fks]
        all_field_names += [fk["name"] for fk in fks]

        pks = inspector.get_pk_constraint(table)
        class_name = utils.snake_to_pascal(table)
        snk_table_name = utils.snake_to_pascal(table)
        col_names = [col["name"] for col in columns]
        rt_cols = []  # str(RefTypeMixin.mixin_fields())
        rt_fld_set = []  # str(RefTypeMixin.mixin_fieldset())
        # lbl_cols = [utils.snake_to_label(col["name"]) for col in columns]
        # lbl_cols = {['col': utils.snake_to_label(col.split('_id_fke')[0]) for col in all_field_names]}
        lbl_cols = {}
        for col in all_field_names:
            lbl_cols[col.split('_id_fke')[0]] = utils.snake_to_label(col.split('_id_fke')[0])
        print(lbl_cols)
        tbl_columns = remove_id_columns(all_field_names)

        table_title = utils.snake_to_label(table)
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
        detail_class_name = utils.snake_to_pascal(table)
        for fk in fks:
            # print(table, fk)
            fkname = fk["name"]
            fktable = fk["referred_table"]
            fkcol = fk["constrained_columns"][0]
            fkref = fk["referred_columns"][0]
            pjoin = utils.snake_to_pascal(table) + '.' + fkcol + ' == ' + fktable + '.' + fkref
            class_name = utils.snake_to_pascal(fktable)
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
