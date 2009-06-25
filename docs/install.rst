.. _install:


Installation guide
==================

Before installing django-flashpolicies, you'll need to have a copy of
`Django <http://www.djangoproject.com>`_ already installed. Django 1.0
or later is required, and it's generally recommended that you use the
latest stable release of Django. For information on obtaining and
installing Django, consult the `Django download page
<http://www.djangoproject.com/download/>`_, which offers convenient
packaged downloads and installation instructions.

Note that older versions of Django *may* work as well, but are not
supported (and, due to the behavior of the ``APPEND_SLASH`` setting in
older Django releases, may not be able to serve cross-domain policies
from the proper URL).


Installing django-flashpolicies
-------------------------------

There are several ways to install django-flashpolicies:

* Automatically, via a Python package installer.

* Manually, by downloading a copy of the release package and
  installing it yourself.

* Manually, by performing a Mercurial checkout of the latest code.

It is also highly recommended that you learn to use `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_ for development and
deployment of Python software; ``virtualenv`` provides isolated Python
environments into which collections of software (e.g., a copy of
Django, and the necessary settings and applications for deploying a
site) can be installed, without conflicting with other installed
software. This makes installation, testing, management and deployment
far simpler than traditional site-wide installation of Python
packages.


Automatic installation via a package manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several automatic package-installation tools are available for Python;
the most popular are `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_ and `pip
<http://pip.openplans.org/>`_. Either can be used to install
django-flashpolicies.

Using ``easy_install``, type::

    easy_install django-flashpolicies

Using ``pip``, type::

    pip install django-flashpolicies


Manual installation from a downloaded package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer not to use an automated package installer, you can
download a copy of django-flashpolicies and install it manually. The
latest release package can be downloaded from `django-flashpolicies'
listing on the Python Package Index
<http://pypi.python.org/pypi/django-flashpolicies/>`_.

Once you've downloaded the package, unpack it (on most operating
systems, simply double-click; alternately, type ``tar zxvf
django-flashpolicies-1.3.tar.gz`` at a command line on Linux, Mac OS X
or other Unix-like systems). This will create the directory
``django-flashpolicies-1.3``, which contains the ``setup.py``
installation script. From a command line in that directory, type::

    python setup.py install

Note that on some systems you may need to execute this with
administrative privileges (e.g., ``sudo python setup.py install``).


Manual installation from a Mercurial checkout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you'd like to try out the latest in-development code, you can
obtain it from the django-flashpolicies repository, which is hosted at
`Bitbucket <http://bitbucket.org/>`_ and uses `Mercurial
<http://www.selenic.com/mercurial/wiki/>`_ for version control. To
obtain the latest code and documentation, type::

    hg clone http://bitbucket.org/ubernostrum/django-flashpolicies/

This will create a copy of the django-flashpolicies Mercurial
repository on your computer; you can then the ``django-flashpolicies``
directory inside the checkout your Python import path, or use the
``setup.py`` script to perform a global installation from that code.


Basic configuration and use
---------------------------

Once installed, you can take advantage of django-flashpolicies on any
Django-based site you're developing. Simply add ``flashpolicies`` to
your ``INSTALLED_APPS`` setting (django-flashpolicies provides no
models, so running ``manage.py syncdb`` is not required), and then
configure one or more appropriate URL patterns to serve your
cross-domain policy (or policies).

For most cases, you'll simply need a single pattern, in your root
URLConf, pointing the URL ``/crossdomain.xml`` (the standard location
for a cross-domain policy) to the view
:func:`flashpolicies.views.simple`, passing a list of domains from
which you'd like to allow access. For example, to enable access for
Flash content served from the domains ``media.example.com`` and
``api.example.com``, the following URL pattern in your root URLConf
would suffice::

    url(r^'crossdomain.xml$',
        'flashpolicies.views.simple',
        {'domains': ['media.example.com', 'api.example.com']}),