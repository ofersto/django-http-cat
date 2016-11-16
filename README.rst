Django http.cat
===============

**Django Http.Cat** is a tiny library that lets you easily return pictures from http.cat in case of error (404, 500, etc)


Installation
------------

Just use pip

.. code::

    pip install django-http-cat


Configuration
-------------

Simply add the middleware your django ``MIDDLEWARE_CLASSES`` setting.


.. code::

    MIDDLEWARE_CLASSES = [
        ...
        'httpcat.middleware.HttpCatErrorHandler'
    ]

You don't need to include it in your ``INSTALLED_APPS``.

You can specify which status codes it should ignore by setting ``HTTP_OK_CODES`` to a list of integers with the codes to ignore (default if 200 and 304).

