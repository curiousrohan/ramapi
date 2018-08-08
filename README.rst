======
ramapi
======


.. image:: https://img.shields.io/pypi/v/ramapi.svg
        :target: https://pypi.python.org/pypi/ramapi

.. image:: https://img.shields.io/travis/curiousrohan/ramapi.svg
        :target: https://travis-ci.org/curiousrohan/ramapi

.. image:: https://readthedocs.org/projects/ramapi/badge/?version=latest
        :target: https://ramapi.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python implementation for the Rick and Morty API https://rickandmortyapi.com/


* Free software: MIT license
* Documentation: https://ramapi.readthedocs.io.


Features
--------
All methods returns json

Base features:
	- api_info() returns api information
	- schema() returns the json outline

Character,Location,Episode featutes:
	- get_all() returns all values
	- get() Takes a perimeter and returns a value
	- filter() Returns filtered results
	- schema() Returns json outline

For detailed information and usage instrustions:
	- Read Docs at https://ramapi.readthedocs.io
	- Visit official API Docs https://rickandmortyapi.com/documentation


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
