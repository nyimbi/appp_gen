# Appgen

[![PyPI](https://img.shields.io/pypi/v/appgen.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/appgen.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/appgen)][python version]
[![License](https://img.shields.io/pypi/l/appgen)][license]

[![Read the documentation at https://appgen.readthedocs.io/](https://img.shields.io/readthedocs/appgen/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/nyimbi/appgen/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/nyimbi/appgen/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/appgen/
[status]: https://pypi.org/project/appgen/
[python version]: https://pypi.org/project/appgen
[read the docs]: https://appgen.readthedocs.io/
[tests]: https://github.com/nyimbi/appgen/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/nyimbi/apppgen
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

 Welcome to `appgen`, a Python package that generates Flask-AppBuilder applications based
on an inspecte database schema!

### Introduction
----------------

`appgen` is designed to simplify the process of creating custom web applications for
PostgreSQL databases. With just a few lines of code, you can generate a fully functional
Flask-AppBuilder application that includes views for each table, MasterDetailViews for
foreign keys, and MultipleViews if a parent table has multiple foreign keys. The package
also generates a db schema viewer to allow end users to visualize the structure of the
database.

`appgen` is built on top of Flask-AppBuilder, SQLAlchemy, It supports and integrates PostgreSQL Row Level
Security (RLS) services, and makes heavy use of stored procedures and functions for data
manipulaTIon and validation. We strongly recommend using PostgreSQL as your database
engine, but `appgen` should work with other SQL databases supported by SQLAlchemY.

### Installation
---------------
TODO: Note pushed to pypi yet, still a WIP

To install `appgen`, run the following command:
```
pip install appgen
```
This will install the `appgen` package and all its dependencies, including
Flask-AppBuilder, SQLAlchemY, and psycopg2.

### Usage
-------

To use `appgen`, you can create a new Python file and import the `AppGen` class from the
`appgen` package:
```python
from appgen import AppGen
```
Then, initialize an instance of the `AppGen` class with your database connection string,
Flask-AppBuilder configuration options, and other settings:
```python
appgen = AppGen(
    db_uri='postgresql://user:password@localhost/dbname',
    appbuilder_options={
        'APPBUILDER_URL': '/admin',
        'APPBUILDER_API_URL': '/api'
    },
    use_roles=True,
    use_stored_procedures=True,
    use_db_schema_viewer=True
)
```
The `db_uri` argument is the database connection string in the format required by
SQLAlchemY. The `appbuilder_options` argument is a dictionary of Flask-AppBuilder
configuration options, including the admin URL and API URL. The `use_roles`,
`use_stored_procedures`, and `use_db_schema_viewer` arguments are optional and allow you
to customize the generated application's behavior.

Next, call the `generate()` method on the `AppGen` instance to generate the
Flask-AppBuilder application:
```python
app = appgen.generate()
```
This will return a Flask application object that you can run using the `run()` method or
a WSGI server.

### Command Line Interface
------------------------

`appgen` also provides a command line interface program that allows you to generate a
Flask-AppBuilder application from a PostgreSQL database schema.

To use the CLI, run the following command:
```
appgen <db_uri> [options]
```
Replace `<db_uri>` with your database connection string in the format required by
SQLAlchemY. The optional arguments are:

- `--appbuilder-url <url>`: The URL of the Flask-AppBuilder admin interface. Defaults to
'/admin'.
- `--api-url <url>`: The URL of the Flask-AppBuilder API interface. Defaults to '/api'.
- `--use-roles`: Enable PostgreSQL Rolw Level Security integration. Defaults to True.
- `--use-stored-procedures`: Enable stored procedure integration. Defaults to True.
- `--use-db-schema-viewer`: Enable the db schema viewer. Defaults to True.

For example, to generate a Flask-AppBuilder application with the default settings, run
the following command:
```
appgen postgresql://user:password@localhost/dbname
```
This will create a new directory called `appgen` containing the generated
Flask-AppBuilder application. You can then run the application using a WSGI server or the
`flask run` command.

### Conclusion
-------------

`appgen` is a powerful Python package that simplifies the process of creating
Flask-AppBuilder applications based on PostgreSQL databases. By using `appgen`, you can
quickly generate a fully functional web application that includes views for each table,
MasterDetailViews for foreign keys, and Multipl
## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Appgen_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/nyimbi/appgen/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/nyimbi/appgen/blob/main/LICENSE
[contributor guide]: https://github.com/nyimbi/appgen/blob/main/CONTRIBUTING.md
[command-line reference]: https://appgen.readthedocs.io/en/latest/usage.html
