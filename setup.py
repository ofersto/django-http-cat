from distutils.core import setup

setup(
    name = 'django-http-cat',
    packages = ['httpcat'],
    version = '0.1',
    description = 'Fetch pictures from http.cat as error pages',
    license = "MIT",
    author = 'Ofer Stolov',
    author_email = 'ofersto123@gmail.com',
    url = 'https://github.com/ofersto/django-http-cat',
    download_url = 'https://github.com/ofersto/django-http-cat/tarball/0.1',
    keywords = ['django', 'error handling', 'middleware', 'http.cat', 'cat'],
    install_requires = [
        "django"
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Framework :: Django",
    ],
)
