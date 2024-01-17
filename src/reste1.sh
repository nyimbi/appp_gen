dropdb wakala1
createdb wakala1
python codegen.py
# python test1.py
cp apis.py models.py views.py view_mixins.py model_mixins.py ../tmp/apg_test/app
