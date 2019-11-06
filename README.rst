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

Only works for Python3


* Free software: MIT license
* Documentation: https://ramapi.readthedocs.io.


Features
--------

All methods returns json

Base class features:
	- api_info() : api information
	- schema()   : json outline

Character,Location,Episode class featutes:
	- get_all()	 : All information in paginated way
	- get() 	 : Information regarding the passed parameter
	- filter() 	 : Filtered results
	- schema()   : json outline

For detailed information and usage instructions:
	- Read Docs at https://ramapi.readthedocs.io
	- Visit official API Docs https://rickandmortyapi.com/documentation


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
