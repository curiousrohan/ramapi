=====
Usage
=====

To use ramapi in a project::

    import ramapi 

This will import the ramapi package.

To use the Base class, Character Class or any other class::

	from ramapi import Base
	from ramapi import Character

To import all the classes::

	from ramapi import * 

Assuming you have imported the module successfully..

Base Class commands::

	ramapi.Base.api_info()
	ramapi.Base.schema()

Character/Location/Episode Class commands::

	ramapi.Character.get_all() 
	ramapi.Character.get_page() //Only available for character class
	ramapi.Character.get()
	ramapi.Character.filter()
	ramapi.Character.schema()

Replace Character with Location,Episode to access the corresponding properties.

All methods return json.

1. get_all() 

This method doesn't take any parameters and returns all the resulsts in a paginated way.

Example::

	ramapi.Episode.get_all()

2. get_page()

Takes page number as parameter and returns response of that page.

Example::

	ramapi.Character.get_page(3) 

3. get()

Take one or multiple parametes and returns corresponding output

Example::

	ramapi.Location(4)
	ramapi.Episode([10,28]) //Takes list as parameter

4. filter()

Takes one or more arguments and filters the results.

Example::

	ramapi.Character.filter(name='rick',status='alive') 

5. schema()

Returns the json outline for an particular class. 

Example::

	ramapi.Location.schema()


Checkout official docs at https://rickandmortyapi.com/documentation for more information.




