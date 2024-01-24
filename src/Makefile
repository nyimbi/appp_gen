DB_NAME := $(if $(DB),$(DB),wakala1)  # Default to "wakala1" if no parameter is provided

# Target for setting up the database, using the provided database name
db_drop:
	dropdb $(DB_NAME)
	createdb $(DB_NAME)

db_pop:
	psql wakala1 -f ../tmp/db/country.sql
	psql wakala1 -f ../tmp/db/states.sql
	psql wakala1 -f ../tmp/db/lga.sql
	psql wakala1 -f ../tmp/db/currency.sql
	psql wakala1 -f ../tmp/db/cust_segment.sql
	psql wakala1 -f ../tmp/db/doc_type.sql
	psql wakala1 -f ../tmp/db/mime_types.sql
	psql wakala1 -f ../tmp/db/mime_type_map.sql
	psql wakala1 -f ../tmp/db/tech_params.sql
	psql wakala1 -f ../tmp/db/trans_type.sql

# Other targets (no changes needed)
codegen:
	python codegen.py

test:
    # python test1.py  # Uncomment if you want to run the test

copy_files:
	cp apis.py gql.py models.py views.py view_mixins.py model_mixins.py sec.py sec_forms.py sec_views.py __init__.py  ../tmp/apg_test/app

all: db_drop codegen copy_files  # test  # Uncomment if you want to include testing
