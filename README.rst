Git Utils
=========

This is a collection of fun little scripts to give you some stats about a git
repo.

Install
-------

::

    $ pip install -e  git://github.com/honza/gitutils.git#egg=gitutils

Usage
-----

``cd`` into a git repository and run::

    $ blamer

or:

::

    $ chart

**blamer** will run through all the files git tracks, and see how many lines
each user has written/edited. You will get a number of lines and percentage.
Throughout the course of a project, you will add lines and your lines will be
deleted. This shows you how much of your code is still in the project now.

**chart** will run through all the files git track, and see how many lines each
person has touched. Unlike *blamer* this will include all lines, not just the
ones still visible.

License
-------

Sweet and short, BSD license.

