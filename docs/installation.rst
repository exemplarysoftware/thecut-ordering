.. _installation:

=========================
Installation instructions
=========================

1. Install via pip / pypi::

    $ pip install thecut-ordering


2. Add to your project's ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'thecut.ordering'
        # ...
    ]

3. Sync your project's migrations::

    $ python manage.py migrate ordering
