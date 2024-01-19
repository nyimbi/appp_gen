DB_NAME := $(if $(DB),$(DB),wakala1)  # Default to "wakala1" if no parameter is provided

# Target for setting up the database, using the provided database name
db:
	dropdb $(DB_NAME)
	createdb $(DB_NAME)

# Other targets (no changes needed)
codegen:
	python codegen.py

test:
    # python test1.py  # Uncomment if you want to run the test

copy_files:
	cp apis.py gql.py models.py views.py view_mixins.py model_mixins.py ../tmp/apg_test/app

all: db codegen copy_files  # test  # Uncomment if you want to include testing
