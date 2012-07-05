Django Setup
============================================

is my default setup I use for many projects. As such I always run
through the same steps to setup the basics, from django, over S3 for
statics, HTML5 + Twitter-Bootstrap for the frontend up to many django
contribs I use like South, Userena and the gunicorn environment around
it.

So I started this repository with the basic setup to reuse and share. It
contains all the things making life much easier and setup (for AWS) what
it is supposed to be: a one second thing.

Pre-Setup
---------
This repository relies on a few submodules to include and derive from.
So don't forget to run:

    $ git submodule init

    $ git submodule update


Setting up
----------
The setup runs in a virtualenv environment. So you should first run

    $ virtualenv .

    $ source bin/activate
    
    $ pip -r requirements.txt

Time for a first test run!

    $ python app/manage.py runserver

And you should be able to access a simple Webpage at

  http://localhost:8000/


Settings
--------

Now, you might want to change the config in app/settings.py . Please
take care that the app/settings_debug.py might overwrites some data in
order to make the manage.py script better locally.

Running for real
----------------

Before you can start developing, don't forget to sync the database.

    $ python app/manage.py syncdb

and migrate some script

    $ python app/manage.py migrate

Now you can actually see the database when you try to go to /admin


Understading Less and JS
------------------------

In order to develop with this repository correctly, you might want to
understand the underlying ideas and structures. For as many things as
possible this repository just pulls in external data and inkludes them
via symlink. You can see that at app/less and at app/static/js/lib/ .

Let's take a short look at the app/less. You'll find two files not
symlinked:
 - styles.less
 - variables.less

The first is there to allow you to modify the loading of the bootstrap
and add your own styles - it is the only style file referenced from the
HTML.

The variables.less allows you to overwrite any variables set for
bootstrap, while containing an upstream compatible inklude model. The
first thing that file does is inkluding the original variables file. In
order to show this, the variables.less is currently setting a different
background color.

Understanding the Django-Setup
------------------------------

The Django setup inkludes alread many contribs, like S3 and South, as
you've probably noticed when adapting the settings-file. This setup also
ships with a few helpers inside the base-project. One of them being a
very basic Userena UserProfile-Model (setup by default) and some handy
context processor and helpers in the utils module. Read them, they are
good helpers!

The templates can be found in app/templates. Don't forget to include the
site.html. The base.html is inkluded by many contribs (like Userena) and
allows you to set a slightly different style for those (for e.g. put a
box around the content).


Have fun!

