Tumblr scripts
==============


theme_installs.py
-----------------

Prints the number of times a given theme has been installed. Both of the
following commands are valid:

    python theme_installs.py 1386
    python theme_installs.py http://tumblr.com/theme/1386

For example, here's the default theme:

    $ python theme_installs.py http://www.tumblr.com/theme/433
    1,335,971

Requires:

* [BeautifulSoup][soup]
* openanything.py (included in this directory)


tag_list.py
-----------

Prints a JSON list with all of the user's tags and their frequencies. This is
a quick 'n' dirty solution; use with care.

Requires:

* [python-tumblr][pytumblr]
* [simplejson][simplejson]


[pytumblr]: http://code.google.com/p/python-tumblr/
[simplejson]: http://pypi.python.org/pypi/simplejson/
[soup]: http://www.crummy.com/software/BeautifulSoup/
