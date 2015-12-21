from setuptools import setup, find_packages
from dropzone import __version__


setup(
    name="django-dropzone",
    version=__version__,
    url='https://github.com/chrisvxd/django-dropzone',
    license='MIT',
    platforms=['OS Independent'],
    description="A simple django widget for dropzone.js.",
    install_requires=[
        'django>=1.8',
    ],
    long_description=open('README.rst').read(),
    author='Chris Villa',
    # author_email='',
    maintainer='Chris Villa',
    # maintainer_email='',
    packages=find_packages(),
    package_data = {
        'dropzone': [
            'static/*',
            'templates/*',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
