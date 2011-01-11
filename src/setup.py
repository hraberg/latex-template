from setuptools import setup, find_packages
import os


setup(
    name="my-django-project",
    version="build.%s" % (os.environ.get('BUILD_NUMBER','DEV')),
    packages=find_packages(),
)

