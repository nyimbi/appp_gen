
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



# Appgen - Generate Flask Apps with Attitude

Appgen is here to kick butt and generate Flask apps. It is still a personal project, but works 90% .
All the generation code is in the src/codegen.py file.

This bad boy will hook up to your PostgreSQL database and pump out a fully loaded Flask-AppBuilder app faster than you can say "import flask." We're talking admin dashboards, API endpoints, and even a db schema viewer in case you forget wtf your database looks like.

Gone are the days of writing tedious CRUD views and configuring user auth. Appgen handles all that noise so you can focus on more important things like clicking around your new admin dashboard and pretending you're busy.

## Get Started 

Install Appgen:

```
pip install appgen
```

Fire it up:

```python
from appgen import AppGen

appgen = AppGen(
   db_uri='postgresql://blahblah',
   appbuilder_options={'ADMIN_URL': '/admin-dashboard-of-glory'},
   use_roles=True
)

app = appgen.generate()
```

Boom! App generated. Pour yourself a nice cold one and bask in all your newfound free time.

## CLI

For you terminal junkies, Appgen also has a CLI so you can feel like an elite hacker while generating apps:

```
appgen postgresql://hackedthensa
```

## Wrap Up

Appgen is here to disrupt the Flask app space with its no-nonsense, straight-to-the-point app generation. It don't mess around. Now go forth and build yourself a custom admin dashboard on that PostgreSQL db you have lying around. Live the dream!

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