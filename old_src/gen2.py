import inflect, string, enum
# from datetime import date, datetime
from sqlalchemy import Enum
from marshmallow import fields
from sqlalchemy import create_engine, inspect, MetaData, FetchedValue, ForeignKey
from sqlalchemy import (
    Enum, ForeignKey, ARRAY, JSON, PickleType, LargeBinary, Boolean, Date, DateTime, Float, Integer,
    Interval, Numeric, SmallInteger, String, Text, Time, BigInteger, Unicode, UnicodeText, CHAR,
    VARBINARY, TIMESTAMP, CLOB, BLOB, NCHAR, NVARCHAR, INTEGER, TEXT, VARCHAR, NUMERIC, BOOLEAN, Boolean, DateTime, Date,
    Time, DECIMAL, Float, Integer, Interval, Numeric, SmallInteger, String, Text, Time,
)
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, CITEXT, DATE, DATEMULTIRANGE,
    DATERANGE, DOMAIN, DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INT4MULTIRANGE, INT4RANGE, INT8MULTIRANGE, INT8RANGE, INTEGER,
    INTERVAL, JSON, JSONB, JSONPATH, MACADDR, MACADDR8, MONEY, NUMERIC, NUMMULTIRANGE, NUMRANGE, OID, REAL,
    REGCLASS, REGCONFIG, SMALLINT, TEXT, TIME, TIMESTAMP, TSMULTIRANGE, TSQUERY, TSRANGE, TSTZMULTIRANGE, TSTZRANGE, TSVECTOR, UUID, VARCHAR, Range,
)
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped


from headers import *
from utils import *
from db_utils import *


def inspect_metadata(database_uri):
    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)
    return metadata, inspector


def get_display_column(column_name_list):
    priorities = ["name", "alias", "title", "label", "display_name", "code"]

    for name in priorities:
        if name in column_name_list:
            return name

    for name in column_name_list:
        if "name" in name.lower() or "model" in name.lower():
            return name

    return column_name_list[0]


def gen_model_enums(metadata, inspector):
    enum_code = []
    enums = inspector.get_enums()
    for en in enums:
        enum_code.append(f"\nclass {en['name']}(enum.Enum):")
        for label in en["labels"]:
            enum_code.append(f"   {label.upper()} = '{label}'")
    enum_code.append(" ")
    return enum_code


def gen_model_domains(metadata, inspector):
    domain_code = []
    # Retrieve information about domain types
    domains = inspector.get_domains()

    for domain in domains:
        domain_name = domain["name"]
        base_type = domain["data_type"]
        not_null = domain["not_null"]
        BaseType = map_pgsql_datatypes(base_type.lower())

        domain_code.append(
            f"\nclass {domain_name}({BaseType}):  # BaseType should be replaced with the actual base type"
        )

        # Check for default value
        if domain["default"]:
            domain_code.append(f"    default = {domain['default']}")

        # Check for not null constraint
        if not_null:
            domain_code.append(f"    not_null = True")

        # Handling constraints
        for constraint in domain.get("constraints", []):
            constraint_name = constraint["name"]
            constraint_check = constraint["check"]
            domain_code.append(f"    # Constraint: {constraint_name}")
            domain_code.append(f"    check = '{constraint_check}'")

        # domain_code.append('    pass')

    domain_code.append(" ")
    return domain_code

def gen_model_header():
    model_header = []
    model_header.append('import datetime, enum')
    model_header.append('from flask_appbuilder import Model')
    model_header.append('from sqlalchemy import Column, Integer, Boolean, String, Float, Enum, ForeignKey, Date, DateTime, Text')
    model_header.append('from sqlalchemy.orm import relationship, backref\n')
    model_header.append(MODEL_HEADER)
    return model_header



def gen_models(metadata, inspector):
    model_code = []
    for table in metadata.sorted_tables:
        cols = inspector.get_columns(table.name)
        pks = inspector.get_pk_constraint(table.name)
        fks = inspector.get_foreign_keys(table.name)
        uqs = inspector.get_unique_constraints(table.name)
        cck = inspector.get_check_constraints(table.name)
        enums = inspector.get_enums()
        enum_names = {e['name']: e for e in enums}
        table_class = snake_to_pascal(table.name)
        t_comment = inspector.get_table_comment(table.name)

        model_code.append(f"class {table_class}(Model):")
        model_code.append(f'    __tablename__ = "{table.name}"')

        if t_comment["text"]:
            model_code.append(
                f'    __doc__ = "{t_comment["text"]}"\n'
            )  # Use the table comment in the docstring

        for col in inspector.get_columns(table.name):
            # String parts to compose a column definition
            # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedColumn
            (c_pk, c_fk, c_autoincrement, c_comment, c_computed, c_default, c_dialect_options,) = ("", "", "", "", "", "", "")
            c_identity, c_column_name, c_nullable, c_type, c_unique, c_ck = ("", "", "", "", "", "",)

            # check if the column is an enum type
            if isinstance(col["type"], Enum):
                enum_type_name = None
                # Find the enum type name from the enums list
                for enum_name, enum_info in enum_names.items():
                    if col['type'].name == enum_name:
                        enum_type_name = enum_info['name']
                        break
                if enum_type_name:
                    model_code.append(
                        f"    {col['name']} = Column(Enum({enum_type_name}), name='t_{col['name']}', nullable=False)\n"
                    )
                else:
                    model_code.append(
                    f"    {col['name']} = Column(Enum(t_{col['name']}), name='t_{col['name']}', nullable=False)\n"
                )
            else:
                ctype = col["type"].compile()
                ctype = map_pgsql_datatypes(ctype.lower())

                # First Primary Keys
                if col["name"] in pks["constrained_columns"]:
                    c_pk = ", primary_key=True"

                # The Foreign Keys
                for index, fk in enumerate(fks):
                    if col["name"] == fk["constrained_columns"][0]:
                        fkname = fk["name"]
                        # print(fkname, end="\t")
                        referred_table = fk["referred_table"]
                        fktable = snake_to_pascal(referred_table)
                        fkref = fk["referred_columns"][0]
                        fkcol = fk["constrained_columns"][0]
                        pjoin = (snake_to_pascal(table.name) + "." + fkcol + " == " + fktable + "." + fkref)
                        fkey = fk["referred_table"] + "." + fk["referred_columns"][0]

                        # Is this a self-referential column
                        if table.name == referred_table:  # means it is self-referential
                            c_pk = ""
                            c_fk = f", ForeignKey('{fkey}')"
                        else:
                            c_fk = f", ForeignKey('{fkey}')"
                        break

                # The Unique Keys
                if col["name"] in [uq["column_names"] for uq in uqs]:
                    c_unique = ", unique=True"

                # Finally all the fields from the ReflectedColumn Dictionary
                if col["nullable"] == True:
                    c_nullable = ", nullable=True"
                else:
                    c_nullable = ""  # default behaviour is nullable

                if col["autoincrement"] == True:
                    c_autoincrement = ", autoincrement=True"

                if col["comment"] != None:
                    c_comment = '\n\t\t, comment="' + col["comment"] + '"'

                if col['default'] != None:
                    c_default = f", default = {col['default']}"  # Might include sqltext, so we process further
                    if col['default'] == 'false': c_default = ', default=False'
                    if col['default'] == 'true': c_default = ', default=True'
                    if col['default'] == 'now()': c_default = ', default=func.now()'
                    if ":" in col['default']: c_default ='' # ', default = ' + col['default'].split(':')[0]

                    if col['default'].startswith('nextval'):  # Means it is autoincrement and uses a sequence
                        c_autoincrement = ", autoincrement=True"
                        c_default = ""

                model_code.append(
                    f"    {col['name']} = Column({ctype}{c_fk}{c_pk}{c_unique}{c_autoincrement}{c_default}{c_comment})\n"
                )

        # Now generate relationships for all fks
        # constrained_columns, options, referred_columns, referred_schema, referred_table
        # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedForeignKeyConstraint
        for fk in fks:
            # fkname = fk["name"].split("_id_")[0]
            # fkname = fk["name"].split("_fk")[0]
            qsr = ""  # Quote Self Referential Table Name
            fk_ref_table = snake_to_pascal(fk["referred_table"])
            fk_ref_col = fk["referred_columns"][0]
            fkcol = fk["constrained_columns"][0]
            # fkname = fkcol.split("_fk")[0]
            fkname = fkcol.split("_id")[0]
            print(fkname)
            pjoin = f", primaryjoin='{snake_to_pascal(table.name)}.{fkcol} == {fk_ref_table}.{fk_ref_col}'"
            back_ref = f", backref='{table}s_{fkname}'"
            for_keys = f", foreign_keys=[{qsr}{fk_ref_table}.{fk_ref_col}{qsr}]"
            rem_side = ""

            # We have a self-referential join, so we have to quote the table name
            if snake_to_pascal(table.name) == fk_ref_table:
                qsr = "'"
                rem_side = f", remote_side=[{fk_ref_col}]"
                for_keys = f", foreign_keys=[{fkcol}]"

            rel_name = f"{qsr}{fk_ref_table}{qsr}"

            model_code.append(
                # f"    {fk['name'].split('_id')[0]} = relationship({rel_name}{back_ref}{pjoin}{rem_side})"
                f"    {fkname} = relationship({rel_name}{back_ref}{pjoin}{rem_side})"
                # f"    {rel_name.lower()} = relationship({rel_name}{back_ref}{pjoin}{rem_side})"
            )

            # print(f"    {fkname}")
        # Now write table level check constraints
        if len(cck) > 0:
            for cc in cck:
                constraint_name = cc["name"]
                sql_expression = cc["sqltext"]

                model_code.append(
                    f"    CheckConstraint('{sql_expression}', name={constraint_name})\n"
                )
        model_code.append("\n    def __repr__(self):")
        model_code.append(
            "       return self."
            + get_display_column([c.name for c in table.columns])
            + "\n"
        )
        model_code.append("\n ### \n\n")

    mc = []
    mc.extend(gen_model_header())
    mc.extend(gen_model_enums(metadata, inspector))
    mc.extend(gen_model_domains(metadata, inspector))
    mc.extend(model_code)
    return mc


def gen_view_header():
    view_header = []
    view_header.append("from flask_appbuilder import ModelView")
    view_header.append("from flask_appbuilder.models.sqla.interface import SQLAInterface")
    view_header.append("from flask_appbuilder.views import MasterDetailView, MultipleView")
    view_header.append('from .models import *\n')
    return view_header


def gen_views(metadata, inspector):
    view_code = []
    md_views = set()

    def remove_id_columns(column_names):
        cleaned_names = []

        for name in column_names:
            if name.lower().endswith("_id_fkey"):
                # Remove _id_fkey and add
                cleaned_name = name.replace("_id_fkey", "")
                cleaned_names.append(cleaned_name)
            elif not name.endswith("_id"):
                cleaned_names.append(name)

        return cleaned_names

    view_code.append(VIEW_FILE_HEADER)
    for table in metadata.sorted_tables:
        columns = inspector.get_columns(table.name)
        fks = inspector.get_foreign_keys(table.name)
        all_field_names = []
        # Collect the column and foreign key names
        # all_field_names = [col["name"].lower() for col in columns]
        all_field_names = [col["name"] for col in columns]
        # all_field_names += [fk["name"].lower() for fk in fks]
        all_field_names += [fk["name"] for fk in fks]

        pks = inspector.get_pk_constraint(table.name)
        class_name = snake_to_pascal(table.name)
        snk_table_name = snake_to_pascal(table.name)
        col_names = [col["name"] for col in columns]
        rt_cols = []  # str(RefTypeMixin.mixin_fields())
        rt_fld_set = []  # str(RefTypeMixin.mixin_fieldset())
        # lbl_cols = [utils.snake_to_label(col["name"]) for col in columns]
        # lbl_cols = {['col': utils.snake_to_label(col.split('_id_fke')[0]) for col in all_field_names]}
        lbl_cols = {}
        for col in all_field_names:
            lbl_cols[col.split("_id_fke")[0]] = snake_to_label(col.split("_id_fke")[0])
        tbl_columns = remove_id_columns(all_field_names)

        table_title = snake_to_label(table.name)

        view_code.append(
            VIEW_BODY.format(
                class_name=class_name,
                snk_table_name=snk_table_name,
                tbl_columns=tbl_columns,
                rt_cols=rt_cols,
                rt_fld_set=rt_fld_set,
                lbl_cols=lbl_cols,
            )
        )
        view_code.append(
            VIEW_REGY.format(class_name=class_name, table_title=table_title)
        )

    for table in metadata.sorted_tables:
        columns = inspector.get_columns(table.name)
        fks = inspector.get_foreign_keys(table.name)
        detail_class_name = snake_to_pascal(table.name)
        for fk in fks:
            # print(table, fk)
            fkname = fk["name"]
            fktable = fk["referred_table"]
            fkcol = fk["constrained_columns"][0]
            fkref = fk["referred_columns"][0]
            pjoin = (
                snake_to_pascal(table.name) + "." + fkcol + " == " + fktable + "." + fkref
            )
            class_name = snake_to_pascal(fktable)
            mv_name = class_name + detail_class_name + "View"
            if mv_name not in md_views:
                view_code.append(
                    VIEW_MASTER_DETAILX.format(
                        class_name=class_name,
                        detail_class_name=detail_class_name,
                        pjoin=pjoin,
                    )
                )
                md_views.add(mv_name)
    view_code.append(VIEW_FILE_FOOTER)
    return view_code


# This is to create a marshmallow schema from a metatdata object
# Not actually used at


if __name__ == "__main__":
    md, ip = inspect_metadata("postgresql:///wakala")
    m =[]
    m = gen_models(md,ip)
    write_file("models.py", m)
    m = gen_views(md, ip)
    write_file('views.py', m)
