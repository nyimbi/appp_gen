from sqlalchemy import Enum
from sqlalchemy import create_engine, inspect, MetaData, FetchedValue, ForeignKey
from sqlalchemy import (
    Enum, ForeignKey, ARRAY, JSON, PickleType, LargeBinary, Boolean, Date, DateTime,
    Float, Integer, Interval, Numeric, SmallInteger, String, Text, Time, BigInteger, Unicode,
    UnicodeText, CHAR, VARBINARY, TIMESTAMP, CLOB, BLOB, NCHAR, NVARCHAR, INTEGER, TEXT, VARCHAR, NUMERIC, BOOLEAN,
    Boolean, DateTime, Date, Time, DECIMAL, Float, Integer, Interval, Numeric, SmallInteger, String, Text, Time
)
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, CITEXT, DATE, DATEMULTIRANGE,
    DATERANGE, DOMAIN, DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INT4MULTIRANGE,
    INT4RANGE, INT8MULTIRANGE, INT8RANGE, INTEGER, INTERVAL, JSON, JSONB, JSONPATH,
    MACADDR, MACADDR8, MONEY, NUMERIC, NUMMULTIRANGE, NUMRANGE, OID, REAL, REGCLASS,
    REGCONFIG, SMALLINT, TEXT, TIME, TIMESTAMP, TSMULTIRANGE, TSQUERY, TSRANGE,
    TSTZMULTIRANGE, TSTZRANGE, TSVECTOR, UUID, VARCHAR, Range
)
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.orm import relationship

import inflect
from headers import *
from utils import *
from db_utils import *
from datetime import date, datetime
import string
from marshmallow import fields


def inspect_metadata(database_uri):
    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)
    return metadata, inspector


def get_display_column(column_name_list):
    priorities = ['name', 'alias', 'title', 'label', 'display_name', 'code']

    for name in priorities:
        if name in column_name_list:
            return name

    for name in column_name_list:
        if 'name' in name.lower() or 'model' in name.lower():
            return name

    return column_name_list[0]


def gen_model_enums(metadata, inspector):
    enum_code = []
    enums = inspector.get_enums()
    for en in enums:
        enum_code.append(f"\nclass {en['name']}(enum.Enum):")
        for label in en['labels']:
            enum_code.append(f"   {label.upper()} = '{label}'")
    enum_code.append(' ')
    return enum_code


def gen_model_domains(metadata, inspector):
    domain_code = []
    # Retrieve information about domain types
    domains = inspector.get_domains()

    for domain in domains:
        domain_name = domain['name']
        base_type = domain['data_type']
        not_null = domain['not_null']
        BaseType = map_pgsql_datatypes(base_type.lower())

        domain_code.append(
            f"\nclass {domain_name}({BaseType}):  # BaseType should be replaced with the actual base type")

        # Check for default value
        if domain['default']:
            domain_code.append(f"    default = {domain['default']}")

        # Check for not null constraint
        if not_null:
            domain_code.append(f"    not_null = True")

        # Handling constraints
        for constraint in domain.get('constraints', []):
            constraint_name = constraint['name']
            constraint_check = constraint['check']
            domain_code.append(f"    # Constraint: {constraint_name}")
            domain_code.append(f"    check = '{constraint_check}'")

        # domain_code.append('    pass')

    domain_code.append(' ')
    return domain_code


def gen_models(metadata, inspector):
    model_code = []
    for table in metadata.sorted_tables:
        cols = inspector.get_columns(table.name)
        pks = inspector.get_pk_constraint(table.name)
        fks = inspector.get_foreign_keys(table.name)
        uqs = inspector.get_unique_constraints(table.name)
        cck = inspector.get_check_constraints(table.name)
        table_class = snake_to_pascal(table.name)
        t_comment = inspector.get_table_comment(table.name)

        model_code.append(f"class {table_class}(Model):")
        model_code.append(f'    __tablename__ = "{table.name}"')

        if t_comment['text']:
            model_code.append(f'    __doc__ = "{t_comment["text"]}"\n')  # Use the table comment in the docstring

        for col in inspector.get_columns(table.name):
            # String parts to compose a column definition
            # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedColumn
            c_pk, c_fk, c_autoincrement, c_comment, c_computed, c_default, c_dialect_options = "", "", "", "", "", "", ""
            c_identity, c_column_name, c_nullable, c_type, c_unique, c_ck = "", "", "", "", "", ""
            # c_sqltext = col["sqltext"]
            # column_names_list.append(col["name"])

            # check if the column is an enum type
            if isinstance(col["type"], Enum):
                model_code.append(
                    f"    {col['name']} = Column(Enum({col['name']}), name='t_{col['name']}', nullable=False)\n"
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
                        fkname = fk["name"]
                        print(fkname, end="\t")
                        referred_table = fk["referred_table"]
                        fktable = snake_to_pascal(referred_table)
                        fkref = fk["referred_columns"][0]
                        fkcol = fk["constrained_columns"][0]
                        pjoin = snake_to_pascal(table.name) + '.' + fkcol + ' == ' + fktable + '.' + fkref
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
                    # if col.default is not None:
                    #     default = col.default
                    #     if isinstance(col.default, FetchedValue):
                    #         default = '=' + rep(col.default)

                    if col['default'].startswith('nextval'):  # Means it is autoincrement and uses a sequence
                        c_autoincrement = ", autoincrement=True"
                        c_default = ""

                model_code.append(
                    f"    {col['name']} = Column({ctype}{c_fk}{c_pk}{c_unique}{c_autoincrement}{c_default}{c_comment})"
                )

        # Now generate relationships for all fks
        # constrained_columns, options, referred_columns, referred_schema, referred_table
        # https://docs.sqlalchemy.org/en/20/core/reflection.html#sqlalchemy.engine.interfaces.ReflectedForeignKeyConstraint
        for fk in fks:
            fkname = fk["name"].split('_id_')[0]
            print(fkname, end="\t")
            qsr = ""  # Quote Self Referential Table Name
            fk_ref_table = snake_to_pascal(fk["referred_table"])
            fk_ref_col = fk["referred_columns"][0]
            fkcol = fk["constrained_columns"][0]
            fkname = fkcol.split('_id')[0]
            print(fkname, end="\t")
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
                f"    {fkname} = relationship({rel_name}{back_ref}{pjoin}{rem_side})"
                # f"    {rel_name.lower()} = relationship({rel_name}{back_ref}{pjoin}{rem_side})"
            )

            print(f"    {fkname}")
        # Now write table level check constraints
        if len(cck) > 0:
            for cc in cck:
                constraint_name = cc['name']
                sql_expression = cc['sqltext']

                model_code.append(
                    f"    CheckConstraint('{sql_expression}', name={constraint_name})\n"
                )
        model_code.append("\n    def __repr__(self):\n")
        model_code.append("       return self." + get_display_column([c.name for c in table.columns]) + "\n")
        model_code.append("\n ### \n\n")

    return model_code


def get_table_schema(metadata):
    schema = {}
    for table in metadata.tables.values():
        columns = []
        for col in table.columns:
            field_type = get_field_type(col.type)

            # Handle the case where field_type is None
            if field_type is None:
                print(f"Unsupported column type: {col.type} in table {table.name}")
                continue

            if col.default is not None:
                default = col.default
                if isinstance(col.default, FetchedValue):
                    default = '=' + rep(col.default)
                field_type.default = default

            if col.server_default is not None:
                field_type.server_default = col.server_default

            if col.unique:
                field_type.unique = True

            if col.nullable == False:
                field_type.required = True

            if col.primary_key:
                field_type.primary_key = True

            # Handle computed columns.
            if col.info.get('computed'):
                field_type = fields.Func(col.name, as_string=True)

            # Handle foreign keys and relationships.
            if isinstance(col.type, ForeignKey):
                ref_table = col.foreign_keys[0].referred_table
                ref_col = [x for x in ref_table.columns if x.name == col.foreign_keys[0].column.name][0]
                field_type = relationship(ref_table.name, backref=table.name)

            # Handle enum types.
            elif isinstance(col.type, Enum):
                field_type = fields.Str()
                col_enum_values = str(col.type).split('(')[1].strip().replace("'", "")
                enum_values = [x.strip() for x in col_enum_values.split(',')]
                field_choices = [(x, x) for x in enum_values]
                setattr(field_type, 'choices', field_choices)

            # Handle column comments.
            if table.comment is not None:
                comment = col.comment or ""
                field_type.metadata['description'] = comment

            # Add every property of the ReflectedColumn to the schema.
            # for prop in dir(col):
            #     print(f'{table.name}\t col: {col.name}\t' + prop)
            # if not callable(getattr(col, prop)) and prop != 'metadata' and prop != '__weakref__':
            #     setattr(field_type, prop, getattr(col, prop))

        # Add every property of the Table to the schema.
        # for prop in dir(table):
        #     print(prop)
        # if not callable(getattr(table, prop)) and prop != 'metadata':
        #     setattr(schema[table.name], prop, getattr(table, prop))

        columns.append(field_type)
        schema[table.name] = {'columns': columns}

    return schema


if __name__ == '__main__':
    md, ip = inspect_metadata('postgresql:///wakala')
    # print(get_table_schema(md))
    s = gen_model_enums(md, ip)
    s.extend(gen_model_domains(md, ip))
    s.extend(gen_models(md, ip))
    # print("\n".join(s))

    write_file('models.py', s)
