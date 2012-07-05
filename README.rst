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


