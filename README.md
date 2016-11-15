# Django http.cat
### This tiny library lets you easily return pictures from http.cat in case of error (404, 500, etc)

## Installation
Just use pip

    pip install django-http-cat
> Not yet on Pypi, wait for tomorrow...

## Configuration
Simple add the middleware your django ```MIDDLEWARE_CLASSES``` setting.
```
MIDDLEWARE_CLASSES = [
	...
	'httpcat.middleware.HttpCatErrorHandler'
]
```
You don't need to include it in your ```INSTALLED_APPS```

You can specify which status codes it should ignore by setting ```HTTP_OK_CODES``` to a list of integers with the codes to ignore (default if 200 and 304)